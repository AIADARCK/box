from colorama import *
import time
import os

print(Fore.GREEN,"""
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  ||                                                                   ||
  ||                        Debug Server                               ||
  ||                                                         @aiadarck ||
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  Wait until the fry is finished ....
  ---------------||RUN\n        
""", Fore.RESET)
time.sleep(2)
print(" 1. Could not get lock /var/lib/dpkg/lock' Error \n 2. Connection timed out \n 3. Forgot | username/password/port | Panel loghin \n 4. Google Reacha Fix \n 5. Change SSH Port \n 6. Back \n")
debug=input("What is wrong with your server?")
if debug == '1' :
    print ("1. On lock ")
    os.system('sudo lsof /var/lib/dpkg/lock')
    os.system('sudo lsof /var/lib/apt/lists/lock')
    os.system('sudo lsof /var/cache/apt/archives/lock')
    time.sleep(2)
    process_id=input("Write the process_id Line Above : ")
    print ("2. kill Lock ")
    os.system('sudo kill -9 %s' %(process_id))
    time.sleep(2)
    print ("3. Remove locks in conficg ")
    os.system('sudo rm /var/lib/apt/lists/lock')
    os.system('sudo rm /var/cache/apt/archives/lock')
    os.system('sudo rm /var/lib/dpkg/lock')
    time.sleep(2)
    print ("4. After that, reconfigure the packages")
    os.system('sudo dpkg --configure -a')
    time.sleep(2)
    print ("5. Update Servar ")
    os.system('apt update')
    time.sleep(2)
    print ("6. Restart Panel x-ui ")
    os.system('x-ui restart')
    time.sleep(2)
    print(Fore.GREEN, "Done", Fore.RESET)
elif debug == '2' :
    print ("1. ufw disable ")
    os.system('sudo ufw disable')
    time.sleep(2)
    print ("2. Rest Ufw ")
    os.system('sudo ufw reset')
    time.sleep(2)
    print ("3. Restart Panel x-ui ")
    os.system('x-ui restart')
    time.sleep(2)
    print(Fore.GREEN, "Done", Fore.RESET)
elif debug == '3' :
    print ("1. Change info Panel Servar ")
    os.system('passwd root')
    time.sleep(2)
    print ("3. Restart Panel x-ui ")
    os.system('x-ui restart')
    time.sleep(2)
    print(Fore.GREEN, "Done", Fore.RESET)
elif debug == '4' :
    print ("1. Change info Panel Servar ")
    os.system('passwd root')
    time.sleep(2)
    print ("3. Restart Panel x-ui ")
    os.system('x-ui restart')
    time.sleep(2)
    print(Fore.GREEN, "Done", Fore.RESET)
elif debug == '5' :
    print ("It will be added in the next version")
    time.sleep(4)
    print(Fore.GREEN, "Done", Fore.RESET)
elif debug == '6' :
    path = os.path.dirname(__file__)   
    path = os.path.join(path, "Run.py")
    exec(open(path).read())

else :
    print("Not Fund Error !!!")

time.sleep(2)
print(Fore.WHITE, "ok. Return to the main menu")
time.sleep(1) 

path = os.path.dirname(__file__)   
path = os.path.join(path, "Run.py")
exec(open(path).read())