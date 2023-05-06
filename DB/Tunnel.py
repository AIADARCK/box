from colorama import *
import time
import os

print(Fore.GREEN,"""
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  ||                                                                   ||
  ||                  Tunnel Server iptables                           ||
  ||                                                         @aiadarck ||
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  Box Scripts
  -----------||RUN\n        
""", Fore.RESET)

IPiran= input("Enter the ip server of your tunnel(iran):")
Ipkharej= input("Enter your main server IP(Your server):")
T1 = os.system('sysctl net.ipv4.ip_forward=1')
print("1/4")
time.sleep(1)
T2 = os.system('iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination %s' % IPiran)
print("2/4")
time.sleep(1)
T3 = os.system('iptables -t nat -A PREROUTING -j DNAT --to-destination %s' % Ipkharej)
print("3/4")
time.sleep(1)
T4 = os.system('iptables -t nat -A POSTROUTING -j MASQUERADE')
print("4/4")
print("Done . Edite File /etc/rc.local wait ...  ")
time.sleep(2)
os.system("nano /etc/rc.local")
with open('/etc/rc.local', 'a') as f:
    f.write(f'\n{T1}\n{T2}\n{T3}\n{T4}\n exit0')
os.system("sudo systemctl daemon-reload")
os.system("chmod +x  /etc/rc.local")
time.sleep(2)
os.system("The tunnel was done successfully.")



print(Fore.WHITE,"""

***********************************************************

    Your tunnel has been completed successfully.
    --------------------------------------------
    Change your subdomain IP from the main 
    server IP(Your server) to the 
    tunneling IP server IP(Iran:%s).  #CluodFlare
  
***********************************************************
""" % IPiran )

time.sleep(15)
print(Fore.WHITE, "ok. Return to the main menu")
time.sleep(2)
