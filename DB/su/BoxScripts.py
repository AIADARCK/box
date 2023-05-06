from colorama import *
import time
import os
#import requests

print(Fore.GREEN,"""
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  ||                                                                   ||
  ||                    Install Scripts SSH                            ||
  ||                                                         @aiadarck ||
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  Box Scripts
  -----------||RUN\n        
""", Fore.RESET)
time.sleep(1)
print(" 1. BBR(Complete installation of BBR with reinforcement) \n 2. Speed Test(download / upload) \n 3. Ip Scaner(CludFlare) \n 4. htop(Monitoring) \n 5. iftop(View traffic) \n 6. nginx(Create a site page) \n 7. Hidden IP(CF Script) \n 8. Exit \n")

debug=input("What script do you want to install??")
if debug == '1' :
    print("""
    1. Install BBR
    2.  Edit the server's conf network
    """)
    num = input("entar number list : ")
    if num == 1:
        print (" OK, the operation has started - Installing BBR  ")
        time.sleep(2)
        os.system('wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh" && chmod +x tcp.sh && echo 1 | ./tcp.sh && echo n | ./tcp.sh')
        print(Fore.GREEN, "Done ", Fore.RESET)
    elif num == 2:
        print (" Well, now let's edit the server's conf network  ")
        time.sleep(2)
        os.system('wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh" && chmod +x tcp.sh && echo 4 | ./tcp.sh')
        with open(' nano /etc/sysctl.conf', 'a') as file:
            file.write('fs.file-max = 51200\nnet.core.rmem_max = 67108864\nnet.core.wmem_max = 67108864\nnet.core.netdev_max_backlog = 250000\nnet.core.somaxconn = 4096\nnet.ipv4.tcp_syncookies = 1\nnet.ipv4.tcp_tw_reuse = 1\nnet.ipv4.tcp_tw_recycle = 0\nnet.ipv4.tcp_fin_timeout = 30\nnet.ipv4.tcp_keepalive_time = 1200\nnet.ipv4.ip_local_port_range = 10000 65000\nnet.ipv4.tcp_max_syn_backlog = 8192\nnet.ipv4.tcp_max_tw_buckets = 5000\nnet.ipv4.tcp_fastopen = 3\nnet.ipv4.tcp_mem = 25600 51200 102400\nnet.ipv4.tcp_rmem = 4096 87380 67108864\nnet.ipv4.tcp_wmem = 4096 65536 67108864\nnet.ipv4.tcp_mtu_probing = 1\n ')
        with open('/etc/security/limits.conf', 'a') as file:
            file.write('* soft nofile 51200\n* hard nofile 51200 ')
        with open('nano /etc/pam.d/common-session', 'a') as file:
            file.write('session required pam_limits.so\n*')
        with open('nano /etc/profile', 'a') as file:
            file.write('ulimit -n 51200\n*')
        print(Fore.GREEN, "Done ", Fore.RESET)
    else :
        print("Error !!! ")
    time.sleep(1)
elif debug == '3' :
    print (" OK, the operation has started ")
    def get_cloudflare_ips():
        url = "https://www.cloudflare.com/ips-v4"
        response = requests.get(url)
        ips_v4 = response.text.split()
        
        url = "https://www.cloudflare.com/ips-v6"
        response = requests.get(url)
        ips_v6 = response.text.split()
        
        return ips_v4 + ips_v6
    time.sleep(2)
elif debug == '4' :
    print (" OK, the operation has started ")
    os.system('apt install htop')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif debug == '5' :
    print (" OK, the operation has started ")
    os.system('apt install iftop')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif debug == '6' :
    print (" OK, the operation has started ")
    os.system('apt install nginx')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)  

elif debug == '2' :
    print (" OK, the operation has started ")
    os.system('curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(4)
elif debug == '7' :
    print (" OK, the operation has started ")
    os.system('curl https://raw.githubusercontent.com/badafans/better-cloudflare-ip/master/shell/cf.sh -o cf.sh && chmod +x cf.sh && ./cf.sh')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif debug == '8' :
    print("Back to the main menu")
    exit
    time.sleep(2)
    
else : 
    print("Error !! ")   

print(Fore.WHITE, "ok. Return to the main menu")
time.sleep(3)

path = os.path.dirname(__file__)   
path = os.path.join(path, "Run.py")
exec(open(path).read())