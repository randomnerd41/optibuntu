#!/bin/bash

# ===========
# == runme ==
# ===========

# Made by classiccatlinux (randomnerd41)
# AGPL 3.0 - FOSS
# Version 1.1 

echo "Installing Python3 and running Optibuntu..."
sleep 3
clear
sudo apt update -y  && sudo apt install python3 -y
clear
python3 main.py
