from colorama import *
import time
import os


print(Fore.GREEN,"""
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  ||                                                                   ||
  ||                    Set SSL Certificate                            ||
  ||                                                         @aiadarck ||
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  SSL Certificate
  ---------------||RUN\n        
""", Fore.RESET)
time.sleep(1)
subdomin =input("Enter your SubDomain :")
time.sleep(2)
print ("1. Also install curl and socat ")
os.system('apt install curl socat -y')
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(2)
print ("2. Install Acme Script ")
os.system('curl https://get.acme.sh | sh')
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(2)
print ("3. Install Acme Script ")
os.system('curl https://get.acme.sh | sh')
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(2)
print ("4. Set the default provider to Lets Encrypt ")
os.system('~/.acme.sh/acme.sh --set-default-ca --server letsencrypt')
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(2)
print ("5. actual Email Address")
os.system('~/.acme.sh/acme.sh --register-account -m xxxx@xxxx.com')
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(2)
print ("6. set SSL certificate")
os.system('~/.acme.sh/acme.sh --issue -d %s --standalone' % subdomin)
print(Fore.GREEN, "Done", Fore.RESET)
time.sleep(1)
print(Fore.WHITE,"***********************************************")
print("""
A list of things that have been done for you  :
---------------------------------------------
 1. Also install curl and socat
 2. Install Acme Script
 3. Set the default provider to Lets Encrypt
 4. actual Email Address (xxxx@xxxx.com)
 5. set SSL certificate
---------------------------------------------
Enter these two keys in your panel :

 Certificate = /root/cert.crt
 Key = /root/private.key
""")
print(Fore.WHITE,"***********************************************")
time.sleep(10)
print(Fore.WHITE, "ok. Return to the main menu")
time.sleep(1)




path = os.path.dirname(__file__)   
path = os.path.join(path, "Run.py")
exec(open(path).read())