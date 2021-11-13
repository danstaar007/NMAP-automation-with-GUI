# This is my attempt for initial recon on a target

import sys
import os
import subprocess

test


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
    use_nikto = "nikto -D on -h " + target_ip
    use_enum = "enum4linux -s " +target_ip

    os.system("gnome-terminal -e 'bash -c \"nmap -p- --min-rate=1000 -T4 -sV -sC -v " + target_ip +"; bash\"'"); os.system("gnome-terminal -e 'bash -c \"msfdb-blackarch run; bash\"'"); os.system("gnome-terminal -e 'bash -c \"nikto -D on -h " + target_ip+"; bash\"'"); os.system("gnome-terminal -e 'bash -c \"enum4linux -a " + target_ip+"; bash\"'")
     #nmap_terminal = "gnome-terminal -- "+ use_nmap +""
    # go into preferences on terminal and find under "Command", "When command exits" and set to "hold the terminal open"
    #subprocess.Popen(nmap_terminal, shell = True)
    # print(nmap_output)
    nmap_output = subprocess.getoutput(use_nmap); nikto_out = subprocess.getoutput(use_nikto); enum_out = subprocess.getoutput(use_enum)


    # CHECK FOR PORTS AND EXECUTE MORE RECON
    ssh_port = "22"

    if ssh_port in nmap_output:
        clear()
        print("This has port 22 open")
    else:
        clear()
        print("NOT HERE")

main()
