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
    use_nikto = "nikto -D on -h " + target_ip
    use_enum = "enum4linux -s " +target_ip

    os.system("gnome-terminal -e 'bash -c \"nmap -p- --min-rate=1000 -T4 -sV -sC -v " + target_ip +"; bash\"'"); os.system("gnome-terminal -e 'bash -c \"msfdb-blackarch run; bash\"'"); os.system("gnome-terminal -e 'bash -c \"nikto -D on -h " + target_ip+"; bash\"'"); os.system("gnome-terminal -e 'bash -c \"enum4linux -a " + target_ip+"; bash\"'")

    # go into preferences on terminal and find under "Command", "When command exits" and set to "hold the terminal open"
    #subprocess.Popen(nmap_terminal, shell = True)

    # nmap_output = subprocess.getoutput(use_nmap); nikto_out = subprocess.getoutput(use_nikto); enum_out = subprocess.getoutput(use_enum)
    # nmap_output = subprocess.run(['nmap', '-p-', '--min-rate=1000', '-T4', '-sV', '-sC', '-v'+ target_ip], stdout=subprocess.PIPE, text=True)
    nmap_output = subprocess.run(use_nmap, stdout=subprocess.PIPE, text=True, shell=True)

    #print(nmap_output.stdout)

    # CHECK FOR PORTS AND EXECUTE MORE RECON
    ssh_port = "22"

    if ssh_port in nmap_output.stdout:
        clear()
        print (nmap_output.stdout)
        print("Port 22 open, starting some vulnerability testing.\n")
        print("Please Wait...")
    else:
        clear()
        print (nmap_output.stdout)
        print("NO GOOD PORTS TO TEST")

main()
