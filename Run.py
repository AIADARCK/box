from colorama import *
import time
import os

print(Fore.WHITE,"""
  _______________________________________________________________________
  
+ ______________________________________________________________________ +
 |                                                                      |
 |   IIIIIIIIIII   III   IIIIIIIIIII   IIIIII   IIIIIII  IIIII   II  II |
 |  IIIII   IIIII  III  IIIII   IIIII  II    I  II   II  II  II  IIII   |
 |  IIIII   IIIII  III  IIIII   IIIII  II    I  IIIIIII  IIIII   IIII   |
 |  IIIIIIIIIIIII  III  IIIIIIIIIIIII  IIIIII   II   II  II   I  II  II |
 |  IIIII   IIIII  III  IIIII   IIIII  -------------------------------- |
 |  IIIII   IIIII  III  IIIII   IIIII  |The Most Complete V2Ray Script| |
 |______________________________________________________________________|
+ ----------------- | BOX SCRIPT |                                        +
  _______________________________________________________________________

  ++++ Script Helper Sarvar V2ray 
  Subscribe to the YouTube channel @AIADARCK                                                                      
""")
print(Fore.GREEN,"""
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#    
""", Fore.RESET)
print(" 1. Update sarver \n 2. Inestall Panels \n 3. SSL Certificate \n 4. Box scripts \n 5. Settings \n 6. Security \n 7. Debug Server \n 8. Tunnel Servar(iptables) \n 9. Exit ")
num = input("Enter Number Menu : ")


if num == '1':
    path = os.path.join(os.path.dirname(__file__), "DB/su/UpdateCod.py")
    exec(open(path).read())
elif num == '2':
    path = os.path.join(os.path.dirname(__file__), "DB/su/Panels.py")
    exec(open(path).read())
elif num == '3':
    path = os.path.join(os.path.dirname(__file__), "DB/su/SSL.py")
    exec(open(path).read())
elif num == '4':
    path = os.path.join(os.path.dirname(__file__), "DB/su/BoxScripts.py")
    exec(open(path).read())
elif num == '5':
    path = os.path.join(os.path.dirname(__file__), "DB/su/Settings.py")
    exec(open(path).read())
elif num == '6':
    path = os.path.join(os.path.dirname(__file__), "DB/su/Tunnel.py")
    exec(open(path).read())        
elif num == '7':
    path = os.path.join(os.path.dirname(__file__), "DB/su/Debug.py")
    exec(open(path).read())
elif num == '8':
    path = os.path.join(os.path.dirname(__file__), "DB/su/Tunnel.py")
    exec(open(path).read())    
elif num == '9':
    print(Fore.RED, "Use'Control + C'to exit", Fore.RESET)
    print("Good luck")
else :
    ("Error!!")
       

