import os
import time
import sys
import shutil

# info:
# Version 1.0_beta
# FOSS - AGPL 3.0 
# made by classiccatlinux (randomnerd41).

# OS check
if sys.platform == "linux":
    print("welcome...")
    time.sleep(2)
    os.system('clear')
else:
    print("for ubuntu/debian based (linux) systems only!")
    time.sleep(2)
    exit()

# Start
print("== Optibuntu == ")
in1 = input("start? (y/n): ")
os.system('clear')

if in1 == "n":
    print("exiting...")
    time.sleep(1)
    sys.exit()

elif in1 == "y":
    print("starting...")
    time.sleep(1)
    os.system('clear')

# Snap
print("== Snap ==")   
print("options:")
print("1. Remove snap if its installed.")
print("2. Keep snap if its installed.")
print("3. quit")
print("///////////////////")
inS = input("1, 2, or 3: ")

if inS == "1":
    if shutil.which("snap"):
        os.system("sudo systemctl disable snapd && sudo systemctl stop snapd")
        os.system("sudo apt purge snapd -y && rm -rf ~/snap")
        os.system("sudo rm -rf /snap /var/snap /var/lib/snapd")
        os.system("sudo apt-mark hold snapd")
        os.system("clear")
    else:
        print("Snap is not installed, skipping to next step...")
        time.sleep(2)
        os.system('clear')

elif inS == "2":
    print("Will not remove snap!")
    time.sleep(2)
    os.system('clear')
elif inS == "3":
    print("Quiting...")
    os.system('clear')
    time.sleep(2)
    exit()

else:
    print("Not a command at this time!")
    time.sleep(2)
    exit()

# Printing/Bluetooth
print("== Printing/bluetooth ==")
print("Would you like to turn off bluetooth/printing?")
print("Options:")
print("yes.")
print("no.")
print("///////////////////")
in2 = input("yes or no: ")

if in2 == "yes":
    os.system("sudo systemctl disable bluetooth && sudo systemctl disable cups")
    time.sleep(3)
    os.system('clear')
    
elif in2 == "no":
    print("Will not disable bluetooth and printing.")
    time.sleep(2)
    os.system('clear')
    
else:
    print("Not a command at this time!")
    time.sleep(2)
    exit()

# Gnome
print("== Gnome animations ==")   
print("Would you like to turn off gnomes animations?")
print("Options:")
print("yes.")
print("no.")
print("///////////////////")
in3 = input("yes or no: ")

if in3 == "Yes":
    os.system('clear')
    os.system("gsettings set org.gnome.desktop.interface enable-animations false")
    time.sleep(2)
    os.system('clear')
    
elif in3 == "no":
    print("Will not disable animations.")
    time.sleep(2)
    os.system('clear')
    
else:
    print("Not a command at this time!")
    time.sleep(1)
    exit()

# Fastfetch
print("== Fastfetch ==")
print("Would you like to install fastfetch?")
print("Options:")
print("yes.")
print("no.")
print("///////////////////")
ff = input("yes or no: ")

if ff == "yes":
    os.system("sudo apt install fastfetch -y")
    time.sleep(2)
    os.system('clear')
elif ff == "no":
    print("Will not install fastfetch.")
    time.sleep(2)
    os.system('clear')
else:
    print("Not a command at this time!")

# Updating
print("== Updating system ==")
print("this may take some time...")
print("///////////////////")
time.sleep(2)
os.system('clear')
os.system('sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y')
time.sleep(3)
os.system('clear')

# End
os.system('clear')
print("== Optibuntu ==")
os.system("fastfetch")
print("/////////////////////////////////////////////////////////////////")
print("All done!")
print("thank you for using my program!")
exit()
