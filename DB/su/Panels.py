from colorama import *
import time
import os

print(Fore.GREEN,"""
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  ||                                                                   ||
  ||                  Inestall Panels V2ray                            ||
  ||                                                         @aiadarck ||
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-# 
  Box Scripts
  -----------||RUN\n        
""", Fore.RESET)
print(" 1. X-ui (chin) \n 2. MHSanaei (3x-ui) \n 3. Kafka \n 4. hiddify \n 5. V2bord \n 6. vaxilu \n 7. ShadowsocksR \n 8. Hexa \n  9. Exit")
panels=input("What script do you want to install??")
if panels == '1' :
    print (" OK, the operation has started ")
    os.system('bash <(curl -Ls https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh)')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif panels == '2' :
    print (" OK, the operation has started ")
    os.system('bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif panels == '3' :
    print (" OK, the operation has started ")
    os.system('bash <(curl -Ls https://raw.githubusercontent.com/FranzKafkaYu/x-ui/master/install_en.sh)')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif panels == '4' :
    print (" OK, the operation has started ")
    os.system('sudo bash -c "$(curl -Lfo- https://raw.githubusercontent.com/hiddify/hiddify-config/main/common/download_install.sh)"')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif panels == '5' :
    print (" OK, the operation has started ")
    os.system('bash <(curl -Ls https://cdn.jsdelivr.net/gh/missuo/AutoApplyCert/apply.sh)')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif panels == '6' :
    print (" OK, the operation has started ")
    os.system('bash <(curl -Ls  https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh)')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif panels == '7' :
    print (" OK, the operation has started ")
    os.system('wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssrmu.sh && chmod +x ssrmu.sh && ./ssrmu.sh')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)
elif panels == '8' :
    print (" OK, the operation has started ")
    os.system('bash <(curl -Ls https://raw.githubusercontent.com/HexaSoftwareTech/x-ui/master/install.sh)')
    print(Fore.GREEN, "Done", Fore.RESET)
    time.sleep(2)    
elif panels == '9' :
    exit
else :
    print("Error !! ") 

print(Fore.WHITE, "ok. Return to the main menu")
time.sleep(3)

path = os.path.dirname(__file__)   
path = os.path.join(path, "Run.py")
exec(open(path).read())