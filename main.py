import os
import time
import sys

# info:
# verson 1.1 - stable
# FOSS - AGPL 3.0
# made by classiccatlinux (randomnerd41)

if sys.platform == "linux":
    print("starting...")
    time.sleep(2)
    os.system('clear')
else:
    print("for ubuntu/debian based (linux) systems only!")
    time.sleep(2)
    exit()

print("Welcome to optibuntu (1.1) - A free and open soucre")
print("program for ubuntu and other debian based distros")
print("that makes your system faster!")
time.sleep(5)
os.system('clear')
print("Please read the README.md file!")
print("This program will remove snap if its installed!")
print("And is for debian based linux distros only,")
print("but works best on ubuntu based.")
time.sleep(6)
os.system('clear')

in1 = input("start? (y/n): ")

if in1 == "n":
    print("exiting...")
    time.sleep(1)
    exit()
    
elif in1 == "y":
    os.system("sudo systemctl disable snapd && sudo systemctl stop snapd")
    os.system("sudo apt purge snapd -y && rm -rf ~/snap")
    os.system("sudo rm -rf /snap /var/snap /var/lib/snapd")
    os.system("sudo apt-mark hold snapd")
    os.system('clear')
    
else:
    print("you cant do that!")
    time.sleep(1)
    exit()
    
in2 = input("would you like to turn off bluetooth and printer support? (y/n): ")

if in2 == "y":
    os.system("sudo systemctl disable bluetooth && sudo systemctl disable cups")
    
elif in2 == "n":
    print("Will not disable bluetooth and printing")
    time.sleep(2)
    os.system('clear')
    
else:
    print("you cant do that!")
    time.sleep(1)
    exit()
    
in3 = input("would you like to disable animations? (y/n): ")

if in3 == "y":
    os.system("gsettings set org.gnome.desktop.interface enable-animations false")
    
elif in3 == "n":
    print("Will not disable animations")
    time.sleep(2)
    os.system('clear')
    
else:
    print("you cant do that!")
    time.sleep(1)
    exit()
    
os.system("sudo apt install preload -y && echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf") 
os.system("sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt install zram-tools -y")
os.system("clear")

print("All done!")
print("github: https://github.com/randomnerd41/optibuntu")
print("info: FOSS - made by classiccatlinux (randomnerd41) - python")
time.sleep(6)
os.system('clear')
exit()
