# This is my attempt for initial recon on a target

import sys
import os
import subprocess




# to clear screen
def clear():
    os.system('clear')
    
# create main menu

def main():
    clear()
    
 
    
    print("#############################################################################")
    print("##                                                                         ##")
    print("##                                                                         ##")
    print("##                                                                         ##")
    print("##              This program is for initial recon of a target              ##")
    print("##                                                                         ##")
    print("##                  It uses NMAP, NIKTO, and Enum4linux                    ##")
    print("##                                                                         ##")
    print("##                                                                         ##")
    print("##                                                                         ##")
    print("#############################################################################\n\n\n\n")
    
    
    
    target_ip = input("Enter the target IP address: ")
    
    use_nmap = "nmap -p- --min-rate=1000 -T4 -sV -sC -v " + target_ip
    
    nmap_terminal = "gnome-terminal -- "+ use_nmap +""
    
    nmap_output = subprocess.getoutput(use_nmap)
    # os.system("gnome-terminal -e 'bash -c \"nmap -p- --min-rate=1000 -T4 -sV -sC -v " + target_ip +"; bash\"'")
    
    # go into preferences on terminal and find under "Command", "When command exits" and set to "hold the terminal open"
    subprocess.Popen(nmap_terminal, shell = True)
    
    # print(nmap_output)
    
    
    port = "36927"
    
    if port in nmap_output:
        print("THIS ACTUALLY WORKS")
    else:
        print("NOT HERE")
    
main()