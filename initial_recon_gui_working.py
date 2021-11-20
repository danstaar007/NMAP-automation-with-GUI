# This is my attempt for initial recon on a target using a GUI

import os
from tkinter import *
import tkinter
import subprocess
import sys
from tkinter import ttk
import time
import threading
import numpy as np

#create root frame
root = Tk()
root.title('Recon Tool')
root.geometry('800x500')

#global variables
target_ip = ['']
checkbox_nikto = IntVar()
checkbox_enum = IntVar()

#create tabs
parent_tab = ttk.Notebook(root)
main_tab = ttk.Frame(parent_tab)
nmap_tab = ttk.Frame(parent_tab)
#nikto_tab = ttk.Frame(parent_tab)
#enum_tab = ttk.Frame(parent_tab)
ftp_tab = Frame(parent_tab)
post_tab = Frame(parent_tab)
ssh_tab = Frame(parent_tab)
telnet_tab = Frame(parent_tab)
smtp_tab = Frame(parent_tab)
dns_tab = Frame(parent_tab)
http_tab = Frame(parent_tab)
msrpc_tab = Frame(parent_tab)
netbios_tab = Frame(parent_tab)
smb_tab = Frame(parent_tab)

#add tabs to parent
parent_tab.add(main_tab, text='Main')
parent_tab.add(nmap_tab, text='NMAP')
#parent_tab.add(nikto_tab, text='Nikto')
#parent_tab.add(enum_tab, text='enum4Linux')



#clear frames

####### run program / submit ip ######
def submit_ip():
    global target_ip 
    print(target_ip)
    both_checked = checkbox_nikto.get() + checkbox_enum.get() 
    if both_checked == 2:
            threading.Thread(target=exec_nmap).start()
            threading.Thread(target=exec_nikto).start()
            threading.Thread(target=exec_enum).start()
    elif checkbox_enum.get() == 1:
            threading.Thread(target=exec_nmap).start()
            threading.Thread(target=exec_enum).start()
    elif checkbox_nikto.get() == 1:
            threading.Thread(target=exec_nmap).start()
            threading.Thread(target=exec_nikto).start()
    else:
            threading.Thread(target=exec_nmap).start()

####### define functions ######   
def exec_nmap():
        #use nmap
    
    global target_ip
    use_nmap = "nmap -p- --min-rate=1000 -T4 -sV -sC -v " + target_ip.get() # --script=vulners/vulners.nse (if you want to see vulners associated with)
    nmap_output = subprocess.Popen(use_nmap, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, bufsize=1, universal_newlines=True)
###### enable real-time output in frame ######    
    nmap_output.poll()
    nmap_results = tkinter.Text(nmap_out_frame, wrap='word', bg='Black', fg='Green')
    #include_frame.destroy()

    while True:
       nmap_results.pack(side='top', expand=True, fill='both', padx=25, pady=25)
       output = nmap_output.stdout.readline()
       nmap_results.insert(END, output)
       nmap_results.see(END)
       nmap_results.update_idletasks()
       if not output and nmap_output.poll is not None: break
#### end real-time output ####

    # Install vulners database
    #git clone https://github.com/vulnersCom/nmap-vulners /usr/share/nmap/scripts/vulners && nmap --script-updatedb

###### check for interesting ports #########     need to check multiple inputs
# 21/FTP, 22/SSH, 23/telnet, (25, 465, 587) smtp, 53/DNS, (80,443) http, (135, 593) MSRPC, (137,138,139) NetBios, (139,445) SMB, 
    
    ftp_port = '21/tcp'; ssh_port = '22/tcp'; telnet_port = '23/tcp'; smtp_port = ['25/tcp', ' 465/tcp', '587/tcp']; dns_port = '53/tcp'
    http_port = ['80', '443']; msrpc_port = ['135', '593']; netbios_port = ['137', '138', '139']; smb_port = ['139', '445'] 
    
    #all_ports = [ftp_port, ssh_port, telnet_port, smtp_port, dns_port, http_port, msrpc_port, netbios_port, smtp_port]
    #print(all_ports[0])

### FTP port stuff
    if ftp_port in nmap_results.get('1.0', END):
        parent_tab.add(ftp_tab, text='21/FTP')
        ftp_port_label = Label(ports_frame, text='Port 21 is active').pack(anchor=W)
 ###add stuff to the tab
        test = Label(ftp_frame, text='TESTING')
        test.pack()   
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass  

### SSH port stuff    
    if ssh_port in nmap_results.get('1.0', END):   
            ssh_label = tkinter.Label(ports_frame, text='Port 22 is open, running further recon').pack(anchor=W)
            parent_tab.add(ssh_tab, text='22/SSH')
        ###add stuff to the tab
            test = Label(ssh_frame, text='TESTING')
            test.pack()    
    else:
            pass
            #ports_label = tkinter.Label(ports_frame, text='There are no good ports to test').grid(row=1, column=0, sticky='W')

#### Telnet port stuff
    if telnet_port in nmap_results.get('1.0', END):
            parent_tab.add(telnet_tab)
            telnet_label = Label(ports_frame, text='Port 23 is open').pack(anchor=W)
            ###add stuff to the tab
            test = Label(telnet_tab, text='TESTING')
            test.pack()   
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass  

#### SMTP port stuff
    if '25/tcp' or ' 465/tcp'or '587/tcp' in nmap_results.get('1.0', END):
            parent_tab.add(smtp_tab, text='SMTP')
            telnet_label = Label(ports_frame, text='SMTP is open').pack(anchor=W)
            ###add stuff to the tab
            test = Label(smtp_tab, text='TESTING')
            test.pack()   
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass   

#### DNS port stuff
    if dns_port in nmap_results.get('1.0', END):
            parent_tab.add(dns_tab)
            telnet_label = Label(ports_frame, text='Port 53 is open').pack(anchor=W)
            ###add stuff to the tab
            test = Label(dns_tab, text='TESTING')
            test.pack()   
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass  

#### http port stuff
    if '80/tcp' or ' 443/tcp'or '8080/tcp' in nmap_results.get('1.0', END):
            parent_tab.add(http_tab, text='Nikto')
            telnet_label = Label(ports_frame, text='HTTP is open').pack(anchor=W)
            ###add stuff to the tab
            threading.Thread(target=exec_nikto).start()   
    elif '80/tcp' or ' 443/tcp'or '8080/tcp' in nmap_results.get('1.0', END):
            parent_tab.add(http_tab, text='Nikto')
            telnet_label = Label(ports_frame, text='HTTP is open').pack(anchor=W)
            ###add stuff to the tab
            threading.Thread(target=exec_nikto).start()  
    
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass     

#### msrpc port stuff
    if '135/tcp' or ' 593/tcp' in nmap_results.get('1.0', END):
            parent_tab.add(msrpc_tab, text='MSRPC')
            telnet_label = Label(ports_frame, text='MSRPC is open').pack(anchor=W)
            ###add stuff to the tab
            test = Label(msrpc_tab, text='TESTING')
            test.pack()   
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass 

#### netbios port stuff
    if '137/tcp' or ' 138/tcp' or '139/tcp' in nmap_results.get('1.0', END):
            parent_tab.add(netbios_tab, text='Netbios')
            telnet_label = Label(ports_frame, text='Netbios is open').pack(anchor=W)
            ###add stuff to the tab
            test = Label(netbios_tab, text='TESTING')
            test.pack()   
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass 

    ports_frame.pack()
    ftp_frame.pack(side='top', expand=True, fill='both')
    ssh_frame.pack(side='top', expand=True, fill='both')
    telnet_frame.pack(side='top', expand=True, fill='both')
    smtp_frame.pack(side='top', expand=True, fill='both')
    dns_frame.pack(side='top', expand=True, fill='both')
    http_frame.pack(side='top', expand=True, fill='both')
    msrpc_frame.pack(side='top', expand=True, fill='both')
    netbios_frame.pack(side='top', expand=True, fill='both')
    smtp_frame.pack(side='top', expand=True, fill='both')
    parent_tab.add(post_tab, text='Post Exploit')
    
#### smb port stuff
    if '139/tcp' or ' 445/tcp' in nmap_results.get('1.0', END):
            parent_tab.add(smb_tab, text='SMB')
            telnet_label = Label(ports_frame, text='SMB is open').pack(anchor=W)
            ###add stuff to the tab
            threading.Thread(target=exec_enum).start()  
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass     

    ports_frame.pack()
    ftp_frame.pack(side='top', expand=True, fill='both')
    ssh_frame.pack(side='top', expand=True, fill='both')
    telnet_frame.pack(side='top', expand=True, fill='both')
    smtp_frame.pack(side='top', expand=True, fill='both')
    dns_frame.pack(side='top', expand=True, fill='both')
    http_frame.pack(side='top', expand=True, fill='both')
    msrpc_frame.pack(side='top', expand=True, fill='both')
    netbios_frame.pack(side='top', expand=True, fill='both')
    smb_frame.pack(side='top', expand=True, fill='both')

def exec_nikto():
        #use nikto
    global target_ip    
    use_nikto = "nikto -D on -h " + target_ip.get()
    nikto_output = subprocess.Popen(use_nikto, stdout=subprocess.PIPE, text=True, shell=True, bufsize=1, universal_newlines=True)
###### enable real-time output in frame ###### 
    nikto_output.poll()
    nikto_results = tkinter.Text(http_frame, wrap='word', bg='Black', fg='Green')

    while True:
        nikto_results.pack(side='top', expand=True, fill='both', padx=25, pady=25)
        output = nikto_output.stdout.readline()
        nikto_results.insert(END, output)
        nikto_results.see(END)
        nikto_results.update_idletasks()
        if not output and nikto_output.poll is not None: break
    ##  look at ports, nikto only runs on port 80 unless you specify using "-p"

def exec_enum():
    #use enum
    use_enum = "enum4linux -a -v " + target_ip.get()
    enum_output = subprocess.Popen(use_enum, stdout=subprocess.PIPE, text=True, shell=True, bufsize=1, universal_newlines=True)
    enum_output.poll()
    enum_results = tkinter.Text(smb_frame, wrap='word', bg='Black', fg='Green')
    
    ###### enable real-time output in frame ###### 
    while True:
        enum_results.pack(side='top', expand=True, fill='both', padx=25, pady=25)
        output = enum_output.stdout.readline()
        enum_results.insert(END, output)
        enum_results.see(END)
        enum_results.update_idletasks()
        if not output and enum_output.poll is not None: break


    #remove text in the target_ip box
    target_ip.delete(0,END)
    
def load_timer():
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    test_print = tkinter.Label(loading_frame, text='DONE!')
    loading_frame.pack()
    loading_timer.pack()
    

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        update_timer = ("\r" + animation[i % len(animation)])
        
        loading_timer.create_text(25,25, text=update_timer)
        loading_timer.update()
        sys.stdout.flush()

    test_print.pack()    
    ports_frame.pack()   


######## main tab content ##########
intro_frame = tkinter.Frame(main_tab, pady=15)
input_frame = tkinter.Frame(main_tab, padx=20, pady=10)
ports_frame = tkinter.Frame(main_tab, pady=30)
#include_frame = Frame(main_tab, pady=20, highlightbackground="Black", borderwidth=2, relief=RIDGE)
loading_frame = Frame(main_tab)
loading_timer = Canvas(loading_frame, height=100, width=100)

#define labels 
intro_1 = Label(intro_frame, text="This program conducts initial recon on a target.")
intro_2 = Label(intro_frame, text="The program uses NMAP, Nikto, and Enum4Linux.")
input_text = tkinter.Label(input_frame, text='What is the IP address to the target')

#include checkboxes for nikto and enum
#include_label =Label(include_frame, text='Would you like to include:')
#include_nikto = Checkbutton(include_frame, text='Nikto', variable=checkbox_nikto)
#include_enum = Checkbutton(include_frame, text='Enum4Linux', variable=checkbox_enum)

#nmap tab content
nmap_out_frame = tkinter.Frame(nmap_tab)

#nikto tab content
#nikto_out_frame = tkinter.Frame(nikto_tab)

#enum tab content
#enum_out_frame = tkinter.Frame(enum_tab)

#ports tab content
ftp_frame = Frame(ftp_tab)
ssh_frame = Frame(ssh_tab)
telnet_frame = Frame(telnet_tab)
smtp_frame = Frame(smtp_tab)
dns_frame = Frame(dns_tab)
http_frame = Frame(http_tab)
msrpc_frame = Frame(msrpc_tab)
netbios_frame = Frame(netbios_tab)
smb_frame = Frame(smb_tab)

#put frame on screen
parent_tab.pack(expand=1, fill='both')
intro_frame.pack()
input_frame.pack()
#include_frame.pack()
nmap_out_frame.pack(side='top', expand=True, fill='both')
#nikto_out_frame.pack(side='top', expand=True, fill='both')
#enum_out_frame.pack(side='top', expand=True, fill='both')


#put main tab labels onto screen
intro_1.grid(row=0, column=0)
intro_2.grid(row=1, column=0)
#include_label.grid(row=2, column=0, rowspan=2, padx=10)
#include_nikto.grid(row=2, column=1, pady=[0,5], sticky='W')
#include_enum.grid(row=3, column=1, sticky='W', padx=[0,10])

#input on main tab
input_text.grid(row=0, columnspan=2, pady=10, padx=5, sticky='WE')
target_ip = tkinter.Entry(input_frame, width=15)
target_ip.grid(row=1, column=0, ipady=3)

#buttons
submit_ip = tkinter.Button(input_frame, text='Submit', command=submit_ip)
submit_ip.grid(row=1, column=1, padx=15)

#menu bar
menubar = Menu(root, activebackground='Black', activeforeground='White')
file = Menu(menubar, tearoff=1, activebackground='Black', activeforeground='White')
file.add_command(label='New')
file.add_command(label='Save')
menubar.add_cascade(label='File', menu=file)





root.config(menu=menubar)
root.mainloop()

