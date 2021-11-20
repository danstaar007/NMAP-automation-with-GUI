# This is my attempt for initial recon on a target using a GUI

import os
from tkinter import *
import tkinter
import subprocess
import sys
from tkinter import ttk
import time
import threading

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
nikto_tab = ttk.Frame(parent_tab)
enum_tab = ttk.Frame(parent_tab)
more_tab = Frame(parent_tab)
post_tab = Frame(parent_tab)

#add tabs to parent
parent_tab.add(main_tab, text='Main')
parent_tab.add(nmap_tab, text='NMAP')
parent_tab.add(nikto_tab, text='Nikto')
parent_tab.add(enum_tab, text='enum4Linux')
parent_tab.add(more_tab, text='Ports Output')
parent_tab.add(post_tab, text='Post Exploit')


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

###### check for interesting ports ########
    ssh_port = 'a'
    
    if ssh_port in nmap_output.stdout:
            ports_label = tkinter.Label(ports_frame, pady=50, text='Port 22 is open, running further recon')
            ports_label.pack()
            

    else:
            ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
            ports_label.pack()   

    ports_frame.pack()
    



def exec_nikto():
        #use nikto
    global target_ip    
    use_nikto = "nikto -D on -h " + target_ip.get()
    nikto_output = subprocess.Popen(use_nikto, stdout=subprocess.PIPE, text=True, shell=True, bufsize=1, universal_newlines=True)
###### enable real-time output in frame ###### 
    nikto_output.poll()
    nikto_results = tkinter.Text(nikto_out_frame, wrap='word', bg='Black', fg='Green')

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
    enum_results = tkinter.Text(enum_out_frame, wrap='word', bg='Black', fg='Green')
    
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
include_frame = Frame(main_tab, pady=20, highlightbackground="Black", borderwidth=2, relief=RIDGE)
loading_frame = Frame(main_tab)
loading_timer = Canvas(loading_frame, height=100, width=100)

#define labels 
intro_1 = Label(intro_frame, text="This program conducts initial recon on a target.")
intro_2 = Label(intro_frame, text="The program uses NMAP, Nikto, and Enum4Linux.")
input_text = tkinter.Label(input_frame, text='What is the IP address to the target')

#include checkboxes for nikto and enum
include_label =Label(include_frame, text='Would you like to include:')
include_nikto = Checkbutton(include_frame, text='Nikto', variable=checkbox_nikto)
include_enum = Checkbutton(include_frame, text='Enum4Linux', variable=checkbox_enum)

#nmap tab content
nmap_out_frame = tkinter.Frame(nmap_tab)

#nikto tab content
nikto_out_frame = tkinter.Frame(nikto_tab)

#enum tab content
enum_out_frame = tkinter.Frame(enum_tab)

#put frame on screen
parent_tab.pack(expand=1, fill='both')
intro_frame.pack()
input_frame.pack()
include_frame.pack()
nmap_out_frame.pack(side='top', expand=True, fill='both')
nikto_out_frame.pack(side='top', expand=True, fill='both')
enum_out_frame.pack(side='top', expand=True, fill='both')

#put main tab labels onto screen
intro_1.grid(row=0, column=0)
intro_2.grid(row=1, column=0)
include_label.grid(row=2, column=0, rowspan=2, padx=10)
include_nikto.grid(row=2, column=1, pady=[0,5], sticky='W')
include_enum.grid(row=3, column=1, sticky='W', padx=[0,10])

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

