# This is my attempt for initial recon on a target using a GUI

from tkinter import *
import tkinter
import subprocess
import sys
from tkinter import ttk

#create root frame
root = Tk()
root.title('Recon Tool')
root.geometry('500x500')

#some variables

use_nikto = "nikto -D on -h "
use_enum = "enum4linux -s "

#create tabs
parent_tab = ttk.Notebook(root)
main_tab = ttk.Frame(parent_tab)
nmap_tab = ttk.Frame(parent_tab)
nikto_tab = ttk.Frame(parent_tab)
enum_tab = ttk.Frame(parent_tab)
parent_tab.add(main_tab, text='Main')

#put frame on screen
intro_frame.pack()
input_frame.pack()
output_frame.pack()

#define functions

def submit_ip():
    global target_ip 
    use_nmap = "nmap -p- --min-rate=1000 -T4 -sV -sC -v" +target_ip.get()
    nmap_output = subprocess.run(use_nmap, stdout=subprocess.PIPE, text=True, shell=True)
    nmap_results = tkinter.Text(output_frame, wrap='word')
    nmap_results.insert('1.0', nmap_output.stdout)
    
    nmap_results.pack()

    #remove text in the target_ip box
    target_ip.delete(0,END)

submit_ip = tkinter.Button(input_frame, text='Submit', command=submit_ip)
submit_ip.grid(row=1, column=1, padx=15)


#pass parameter with lambda

#create other frames for application

intro_frame = tkinter.Frame(root, pady=15)
input_frame = tkinter.Frame(root, padx=20, pady=10)
output_frame = tkinter.Frame(root)

#put frame on screen
intro_frame.pack()
input_frame.pack()
output_frame.pack()

#define labels 
intro_1 = Label(intro_frame, text="This program conducts initial recon on a target.")
intro_2 = Label(intro_frame, text="The program uses NMAP, Nikto, and Enum4Linux.")
input_text = tkinter.Label(input_frame, text='What is the IP address to the target')
input_text.grid(row=0, column=0)

#put labels onto screen
intro_1.grid(row=0, column=0)
intro_2.grid(row=1, column=0)

#input frame
input_text.grid(row=0, columnspan=2, pady=10, padx=5, sticky='WE')
target_ip = tkinter.Entry(input_frame, width=15)
target_ip.grid(row=1, column=0, ipady=3)

submit_ip = tkinter.Button(input_frame, text='Submit', command=submit_ip)
submit_ip.grid(row=1, column=1, padx=15)


#pass parameter with lambda














root.mainloop()

