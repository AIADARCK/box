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
print(T1)
time.sleep(1)
T2 = os.system('iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination %s' % IPiran)
print(T2)
time.sleep(1)
T3 = os.system('iptables -t nat -A PREROUTING -j DNAT --to-destination %s' % Ipkharej)
print(T3)
time.sleep(1)
T4 = os.system('iptables -t nat -A POSTROUTING -j MASQUERADE')
print(T4)
time.sleep(2)


print(Fore.WHITE,"""

***********************************************************

    Your tunnel has been completed successfully.
    --------------------------------------------
    Change your subdomain IP from the main 
    server IP(Your server) to the 
    tunneling IP server IP(Iran:%s).  #CluodFlare
  
***********************************************************
""" % IPiran )

time.sleep(12)
print(Fore.WHITE, "ok. Return to the main menu")
time.sleep(2)
