from colorama import *
import time
import os


print(Fore.GREEN,"""
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  ||                                                                   ||
  ||                    Edite Settings server                          ||
  ||                                                         @aiadarck ||
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  Box Scripts
  -----------||RUN\n        
""", Fore.RESET)
time.sleep(1)
print(" 1. Change Port SSH(Panel Port) \n 2. Exit \n")

seting=input("What changes should I make in your server settings? ")
if seting == 1:  
    new_port = input("Enter Change Number servar port : ")
    command = f"sudo sed -i 's/#Port 22/Port {new_port}/g' /etc/ssh/sshd_config"
    os.system(command)
    os.system("sudo systemctl restart sshd")
    time.sleep(4)
elif seting == 2 :
    print("Back to the main menu")
    time.sleep(2)
    path = os.path.dirname(__file__)   
    path = os.path.join(path, "Run.py")
    exec(open(path).read())
else :
    print("Error !!")
    exit
