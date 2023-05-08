from colorama import *
import subprocess
import time
import os
import re


print(Fore.GREEN,"""
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  ||                                                                   ||
  ||                    Security SSH Server                            ||
  ||                                                         @aiadarck ||
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  Box Scripts
  -----------||RUN\n        
""", Fore.RESET)
time.sleep(1)
print(" 1. Eavesdropping attack on the server(DDOS) \n 2. Listening Ports(Number Connections) \n 3. Open Ports firewall \n 4. Exit \n")

sec=input("What changes should I make in your server settings? ")
if sec == '1':
    with open('/var/log/auth.log', 'r') as f:
        content = f.readlines()
    failed_password_lines = [line for line in content if "Failed password" in line]
    ip_addresses = []
    for line in failed_password_lines:
        match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        if match:
            ip_addresses.append(match.group(0))
    ip_address_counts = {}
    for ip in ip_addresses:
        if ip in ip_address_counts:
            ip_address_counts[ip] += 1
        else:
            ip_address_counts[ip] = 1
    for ip, count in sorted(ip_address_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{count} login attempts from {ip}")
    time.sleep(10)    
elif sec == '2':
    port = input('Enter the port number: ')
    command = f"netstat -tna | grep ':{port}' | grep 'ESTABLISHED' | awk '{{print $4}}' | awk -F':' '{{print $NF}}'"
    output = subprocess.run(command, shell=True, capture_output=True, text=True)
    ssh_count = {}
    for p in output.stdout.split():
        if p in ssh_count:
            ssh_count[p] += 1
        else:
            ssh_count[p] = 1
    for p, count in ssh_count.items():
        print(f'Port {p}: {count} connections')
    time.sleep(4) 
elif sec == '3':
    subprocess.call(['sudo', 'ufw', 'enable'])
    num_ports = int(input("Enter the number of ports to open: ( ent = Entire ) "))
    ports = []
    for i in range(num_ports):
        port = input(f"Enter port {i+1}: ")
        ports.append(port)
        if port == "ent":
            break
    for port in ports:
            subprocess.call(['sudo', 'ufw', 'allow', port])
    subprocess.call(['sudo', 'ufw', 'save'])
    print("Done . All the ports you entered were registered successfully")
    time.sleep(2)
elif sec == '4':
    print("Back to the main menu")
    time.sleep(2)
    path = os.path.dirname(__file__)   
    path = os.path.join(path, "Run.py")
    exec(open(path).read())     

else :
    print("Error !!")
    exit
