from colorama import *
import time
import os

print(Fore.GREEN,"""
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  ||                                                                   ||
  ||                    UPDATE SERVER SSH                              ||
  ||                                                         @aiadarck ||
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  Wait until the fry is finished ....
  ---------------||RUN\n        
""", Fore.RESET)
time.sleep(2)
print ("1. Fix Error Update Server (broken)")
os.system('apt --fix-broken install -y')
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(2)
print ("2. Update ")
os.system('apt update')
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(2)
print ("3. Update Surse Server ")
os.system('apt list --upgradable && apt list --upgradable -a ')
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(2)
print ("4. Upgrade Server ")
os.system('apt upgrade -y')
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(2)
quit1 = input("If you installed X-UI on your server, should I restart the panel? (y/n) : ")
if quit1 == 'y':
    print ("5. ok. Restart x-ui ")
    os.system('x-ui restart')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
    print("ok. Return to the main menu")
elif quit1 == 'n':
    print("ok. Return to the main menu")
else :
    exit            
print ("6. Installing important scripts ")
os.system('apt install curl socat -y && curl https://get.acme.sh | sh  ')
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(1)
print(Fore.WHITE,"***********************************************")
print("""
A list of things that have been done for you  :
---------------------------------------------
 1. Fix Error Update Server (broken)
 2. Update Server
 3. Update Surse Server 
 4. Upgrade Server
 5. Restart x-ui
 6. Installing important scripts 
---------------------------------------------

""")
print(Fore.WHITE,"***********************************************")
time.sleep(6)
print(Fore.WHITE, "ok. Return to the main menu")
time.sleep(1)
path = os.path.dirname(__file__)   
path = os.path.join(path, "Run.py")
exec(open(path).read())