import os
import keyboard

print (" OK, the operation has started ")
ports=input("What port should I replace the main port of your server? :")
os.system('nano /etc/ssh/sshd_config')
os.system('Port %s' % ports)
save=keyboard.press_and_release('Ctrl + v', 'Enter')
os.system('service sshd restart ')


path = os.path.dirname(__file__)   
path = os.path.join(path, "Run.py")
exec(open(path).read())