# This is my attempt for initial recon on a target using a GUI

from os import wait
from tkinter import *
import tkinter
import subprocess
import sys
from tkinter import ttk
import time

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
parent_tab.add(main_tab, text='Main')
parent_tab.add(nmap_tab, text='NMAP')
parent_tab.add(nikto_tab, text='Nikto')
parent_tab.add(enum_tab, text='SMB')


#clear frames

#run program / submit ip
def submit_ip():
    global target_ip 
    print(target_ip)
    both_checked = checkbox_nikto.get() + checkbox_enum.get() 
    if both_checked == 2:
            exec_nmap()
            exec_nikto()
            exec_enum()
    elif checkbox_enum.get() == 1:
            exec_enum()
            exec_nmap()
    elif checkbox_nikto.get() == 1:
            exec_nmap()
            exec_nikto() 
    else:
            exec_nmap()


#define functions
    
def exec_nmap():
        #use nmap
    global target_ip
    use_nmap = "nmap -p- --min-rate=1000 -T4 -sV -sC -v " + target_ip.get()
    nmap_output = subprocess.run(use_nmap, stdout=subprocess.PIPE, text=True, shell=True)
    nmap_results = tkinter.Text(nmap_out_frame, wrap='word')
    nmap_results.insert('1.0', nmap_output.stdout)
      
    #display all results
    nmap_results.pack(side='top', expand=True, fill='both', padx=25, pady=25)

    #check for interesting ports
    ssh_port = '22'
    
    if ssh_port in nmap_output.stdout:
            ports_label = tkinter.Label(ports_frame, pady=50, text='Port 22 is open, running further recon')
            ports_label.pack()
    else:
            ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
            ports_label.pack()            

def exec_nikto():
        #use nikto
    global target_ip    
    use_nikto = "nikto -D on -h " + target_ip.get()
    nikto_output = subprocess.run(use_nikto, stdout=subprocess.PIPE, text=True, shell=True)
    nikto_results = tkinter.Text(nikto_out_frame, wrap='word')
    nikto_results.insert('1.0', nikto_output.stdout)
    nikto_results.pack(side='top', expand=True, fill='both',padx=25, pady=25)

def exec_enum():
    #use enum
    use_enum = "enum4linux -S " + target_ip.get()
    enum_output = subprocess.run(use_enum, stdout=subprocess.PIPE, text=True, shell=True)
    enum_results = tkinter.Text(enum_out_frame, wrap='word')
    enum_results.insert('1.0', enum_output.stdout)
    enum_results.pack(side='top', expand=True, fill='both', padx=25, pady=25)


    #remove text in the target_ip box
    target_ip.delete(0,END)
    

#main tab content
intro_frame = tkinter.Frame(main_tab, pady=15)
input_frame = tkinter.Frame(main_tab, padx=20, pady=10)
ports_frame = tkinter.Frame(main_tab, pady=30)
include_frame = Frame(main_tab, pady=20, highlightbackground="Black", borderwidth=2, relief=RIDGE)
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
ports_frame.pack()
include_frame.pack()
nmap_out_frame.pack(side='top', expand=True, fill='both', padx=25, pady=25)
nikto_out_frame.pack(side='top', expand=True, fill='both', pady=25, padx=25)
enum_out_frame.pack(side='top', expand=True, fill='both', pady=25, padx=25)



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
















root.mainloop()

