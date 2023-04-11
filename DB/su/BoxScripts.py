from colorama import *
import time
import os
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
print(" 1. htop(Monitoring) \n 2. iftop(View traffic) \n 3. nginx(Create a site page) \n 4. Speed Test(download / upload) \n 5. Hidden IP(CF Script) \n 6. Exit \n")

debug=input("What script do you want to install??")

if debug == '1' :
    print (" OK, the operation has started ")
    os.system('apt install htop')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif debug == '2' :
    print (" OK, the operation has started ")
    os.system('apt install iftop')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif debug == '3' :
    print (" OK, the operation has started ")
    os.system('apt install nginx')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)  

elif debug == '4' :
    print (" OK, the operation has started ")
    os.system('curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(4)
elif debug == '5' :
    print (" OK, the operation has started ")
    os.system('curl https://raw.githubusercontent.com/badafans/better-cloudflare-ip/master/shell/cf.sh -o cf.sh && chmod +x cf.sh && ./cf.sh')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif debug == '6' :
    exit
    time.sleep(2)
    
else : 
    print("Error !! ")   

print(Fore.WHITE, "ok. Return to the main menu")
time.sleep(3)

path = os.path.dirname(__file__)   
path = os.path.join(path, "Run.py")
exec(open(path).read())