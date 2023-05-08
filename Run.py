import os
from typing import Dict, Callable

from colorama import Fore



print(Fore.WHITE, """
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
""")
print(Fore.GREEN, """
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#
  #-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-#    
""", Fore.RESET)

print(" 1. Update server \n 2. Install Panels \n 3. SSL Certificate \n 4. Box scripts \n 5. Settings \n 6. Security \n 7. Debug Server \n 8. Tunnel Server(iptables) \n 9. Exit ")
choice = input("Enter Menu Number: ")

if choice == '9':
    print(Fore.RED, "Press 'Control + C' to exit.", Fore.RESET)
    print("Good luck!")
    

    try:
        options[choice]()
    except KeyError:
        print("Error: Invalid choice. Try again.")


def update_server() -> None:
    path = os.path.join(os.path.dirname(__file__), "DB/su/UpdateCod.py")
    exec(open(path).read())


def install_panels() -> None:
    path = os.path.join(os.path.dirname(__file__), "DB/su/Panels.py")
    exec(open(path).read())


def ssl_certificate() -> None:
    path = os.path.join(os.path.dirname(__file__), "DB/su/SSL.py")
    exec(open(path).read())


def box_scripts() -> None:
    path = os.path.join(os.path.dirname(__file__), "DB/su/BoxScripts.py")
    exec(open(path).read())


def settings() -> None:
    path = os.path.join(os.path.dirname(__file__), "DB/su/Settings.py")
    exec(open(path).read())


def security() -> None:
    path = os.path.join(os.path.dirname(__file__), "DB/su/security.py")
    exec(open(path).read())


def debug_server() -> None:
    path = os.path.join(os.path.dirname(__file__), "DB/su/Debug.py")
    exec(open(path).read())


def tunnel_server() -> None:
    path = os.path.join(os.path.dirname(__file__), "DB/Tunnel.py")