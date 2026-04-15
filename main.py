import os
import time
import sys
import shutil

# info:
# verson 1.2 - stable
# FOSS - AGPL 3.0 
# made by classiccatlinux (randomnerd41).

if sys.platform == "linux":
    print("starting...")
    time.sleep(2)
    os.system('clear')
else:
    print("for ubuntu/debian based (linux) systems only!")
    time.sleep(2)
    exit()

print("Welcome to optibuntu - A free and open soucre")
print("program for Debian/Ubuntu that")
print("makes your system faster.")
time.sleep(4)
os.system('clear')

in1 = input("start? (y/n): ")

if in1 == "n":
    print("exiting...")
    time.sleep(1)
    sys.exit()

elif in1 == "y":
    if shutil.which("snap"):
        os.system("sudo systemctl disable snapd && sudo systemctl stop snapd")
        os.system("sudo apt purge snapd -y && rm -rf ~/snap")
        os.system("sudo rm -rf /snap /var/snap /var/lib/snapd")
        os.system("sudo apt-mark hold snapd")
        os.system("clear")
    else:
        print("snap is not installed so not removing.")

else:
    print("you cant do that!")
    time.sleep(1)
    sys.exit()
    
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
    
in3 = input("would you like to disable animations? (FOR GNOME DESKTOP ONLY!) (y/n): ")

if in3 == "y":
    os.system("gsettings set org.gnome.desktop.interface enable-animations false")
    
elif in3 == "n":
    print("Will not disable animations.")
    time.sleep(2)
    os.system('clear')
    
else:
    print("you cant do that!")
    time.sleep(1)
    exit()

os.system("clear")
os.system("sudo apt install preload -y && echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf") 
os.system("sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt install zram-tools -y")
os.system("clear")

print("All done!")
print("github: https://github.com/randomnerd41/optibuntu")
time.sleep(4)
os.system('clear')
exit()
