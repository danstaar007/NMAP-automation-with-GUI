#this will install all dependencies for blackarch on an arch distro


import sys
import os
import subprocess

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


 # Clear screen before to show menu
def clear():
    os.system('clear')

# check for root
if not os.geteuid()==0:
    sys.ext("\nYou must be root to run this program!\n")
    
def get_keyring():
    import wget
    url1 = "https://www.blackarch.org/keyring/blackarch-keyring.pkg.tar.xz"
    #wget.download(url1, 'blackarch-keyring.pkg.tar.xz')
    keyring = "blackarch-keyring.pkg.tar.xz"
    
    #os.system("gnome-terminal -e 'bash -c \"yes |pacman -U blackarch-keyring.pkg.tar.xz; exec bash\"'")
    os.system("gnome-terminal -e 'bash -c \"yes |pacman -U blackarch-keyring.pkg.tar.xz; bash gpg --keyserver hkps://keyserver.ubuntu.com:443 \
       --recv-keys 4345771566D76038C7FEB43863EC0ADBEA87E4E3; bash pacman-key --populate; bash yes | pacman -Syu; exec bash\"'")
 
def main_menu():
    clear()

    choice='0'
    while choice =='0':
        print("#############################################################################")
        print("##                                                                         ##")
        print("##              Menu for adding BlackArch to your Arch Distro              ##")
        print("##             Please make sure you are running an Arch Distro             ##")
        print("##                                                                         ##")
        print("##                                                                         ##")
        print("##       1. Install ALL Categories                                         ##")
        print("##       2. Menu for Categories to install individually                    ##")
        print("##                                                                         ##")
        print("##                                                                         ##")
        print("##                                                                         ##")
        print("#############################################################################\n\n\n\n")
    
        
        
        
        choice = input ("Choose an option: ")
        
        if choice == "2":
            category_menu()
        elif choice == "1":
            get_keyring()
        else:
            print("That is not an option")
            main_menu()
           
def category_menu():
    clear()
    sub_cat_choice='0'
    while sub_cat_choice =='0':
        print("#############################################################################")
        print("##                                                                         ##")
        print("##                           Install Categories                            ##")
        print("##                                                                         ##")
        print("##                                                                         ##")
        print("##       1. TEST THIS INSTALL                                         ##")
        print("##       2. Menu for Categories to install individually                    ##")
        print("##                                                                         ##")
        print("##                                                                         ##")
        print("##                                                                         ##")
        print("#############################################################################\n\n\n\n")
    
        sub_cat_choice = input ("Choose an option: ")
        
        if sub_cat_choice == "2":
            category_menu()
        elif sub_cat_choice == "1":
            print("Installing all BlackArch Categories")
            get_keyring()
        else:
            input("\n\nThat is not an option\n\n\nPress enter to select a valid option")
            category_menu()
            

            
main_menu()
    