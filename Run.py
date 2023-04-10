import time
from sys import executable
from subprocess import run

#menu_tolbar
print (".  ___        ___ \n  //_\\   ||  //_\\   \n /// \\\  || /// \\\ DARCK \n ----------------- | BOX SCRIPT  \n\n++++ Script Helper Sarvar V2ray \nSubscribe to the YouTube channel @AIADARCK \n\n ")
print(" 1. Update sarver v2ray \n 2. Install all script Sarver \n 3. Box panel V2ray \n 4. Install SSL Certificate \n 5. Box scripts V2ray \n 6. Exit\n")
num = input ("Enter Number Menu : ")
if num == 1 :
    run('\su\UpdateCod') 
elif num == 2 :
    run('\su\ScriptRun.py')
elif num == 3 :
     run('\su\ Panels.py')
elif num == 4 :
     run('\su\SSL.py')
elif num == 5 :
     run('\su\BoxScripts.py')
elif num == 6 :
    exit
else:
    time.sleep(2)
    run('\..\Run.py')
        