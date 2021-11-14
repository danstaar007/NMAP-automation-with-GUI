# This is my attempt for initial recon on a target

import sys
import os
import subprocess
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QMenu, QToolBar, QSpinBox
from PyQt5.QtGui import QIcon, QKeySequence

# main





target_ip = input("Enter the target IP address: ")

use_nmap = "nmap -p- --min-rate=1000 -T4 -sV -sC -v " + target_ip
use_nikto = "nikto -D on -h " + target_ip
use_enum = "enum4linux -s " +target_ip



    # nmap_output = subprocess.getoutput(use_nmap); nikto_out = subprocess.getoutput(use_nikto); enum_out = subprocess.getoutput(use_enum)

nmap_output = subprocess.run(use_nmap, stdout=subprocess.PIPE, text=True, shell=True)

    #print(nmap_output.stdout)

    # CHECK FOR PORTS AND EXECUTE MORE RECON
ssh_port = "22"

#    if ssh_port in nmap_output.stdout:
#        clear()
#        print (nmap_output.stdout)
#        print("Port 22 open, starting some vulnerability testing.\n")
#        print("Please Wait...")
#    else:
#        print (nmap_output.stdout)
#        print("NO GOOD PORTS TO TEST")
