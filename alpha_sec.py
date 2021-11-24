import os
from tkinter import *
import tkinter
import subprocess
import sys
from tkinter import ttk
import time
import threading
from PIL import Image, ImageTk
sourceFileDir = os.path.dirname(os.path.abspath(__file__)) #use to set the main dir to access subs
import GUI_ports as gp

def exec_nikto():
        #use nikto
    global target_ip    
    use_nikto = "nikto -D on -h " + gp.target_ip.get()
    nikto_output = subprocess.Popen(use_nikto, stdout=subprocess.PIPE, text=True, shell=True, bufsize=1, universal_newlines=True)
###### enable real-time output in frame ###### 
    nikto_output.poll()
    nikto_results = tkinter.Text(gp.http_frame, wrap='word', bg='Black', fg='Green')

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
    use_enum = "enum4linux -a -v " + gp.target_ip.get()
    enum_output = subprocess.Popen(use_enum, stdout=subprocess.PIPE, text=True, shell=True, bufsize=1, universal_newlines=True)
    enum_output.poll()
    enum_results = tkinter.Text(gp.smb_frame, wrap='word', bg='Black', fg='Green')
    
    ###### enable real-time output in frame ###### 
    while True:
        enum_results.pack(side='top', expand=True, fill='both', padx=25, pady=25)
        output = enum_output.stdout.readline()
        enum_results.insert(END, output)
        enum_results.see(END)
        enum_results.update_idletasks()
        if not output and enum_output.poll is not None: break


    #remove text in the target_ip box
    gp.target_ip.delete(0,END)

def exec_ssh_audit():
    ssh_audit_output = subprocess.Popen("ssh-audit " + gp.target_ip.get(), stdout=subprocess.PIPE, text=True, shell=True, bufsize=1, universal_newlines=True)
## realtime output
    ssh_audit_output.poll()
    ssh_results = Text(gp.ssh_audit_frame, wrap='word', bg='Black', fg='Green')
    while True:
        ssh_results.pack(side='top', expand=True, fill='both', padx=25, pady=25)
        output_ssh = ssh_audit_output.stdout.readline() 
        ssh_results.insert(END, output_ssh)   
        ssh_results.see(END)
        ssh_results.update_idletasks
        if not output_ssh and ssh_audit_output.poll is not None: break


def exec_wordpress_map():
    wp_map_output = subprocess.Popen("cmsmap -f W -v " + gp.target_ip.get(), stdout=subprocess.PIPE, text=True, shell=True, bufsize=1, universal_newlines=True)
## realtime output
    wp_map_output.poll()
    wp_map_results = Text(gp.wp_map_frame, wrap='word', bg='Black', fg='Green')
    while True:
        wp_map_results.pack(side='top', expand=True, fill='both', padx=25, pady=25)
        output_ssh = wp_map_output.stdout.readline() 
        wp_map_results.insert(END, output_ssh)   
        wp_map_results.see(END)
        wp_map_results.update_idletasks
        if not output_ssh and wp_map_output.poll is not None: break

def load_timer():
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    test_print = tkinter.Label(gp.loading_frame, text='DONE!')
    gp.loading_frame.pack()
    gp.loading_timer.pack()
    

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        update_timer = ("\r" + animation[i % len(animation)])
        
        gp.loading_timer.create_text(25,25, text=update_timer)
        gp.loading_timer.update()
        sys.stdout.flush()
