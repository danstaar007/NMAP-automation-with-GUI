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
import GUI_setup as gs
import alpha_sec as f

###### check for interesting ports #########     need to check multiple inputs
# 21/FTP, 22/SSH, 23/telnet, (25, 465, 587) smtp, 53/DNS, (80,443) http, (135, 593) MSRPC, (137,138,139) NetBios, (139,445) SMB, 
    
ftp_port = '21/tcp'; ssh_port = '22/tcp'; telnet_port = '23/tcp'; smtp_port = ['25/tcp', ' 465/tcp', '587/tcp']; dns_port = '53/tcp'
http_port = ['80', '443', 'sent']; msrpc_port = ['135', '593']; netbios_port = ['137', '138', '139']; smb_port = ['139', '445'] 
    
    #all_ports = [ftp_port, ssh_port, telnet_port, smtp_port, dns_port, http_port, msrpc_port, netbios_port, smtp_port]
    #print(all_ports[0])

### FTP port stuff
if ftp_port in gs.nmap_results.get('1.0', END):
    gs.parent_tab.add(gs.ftp_tab, text='FTP')

    #change port to green 
    gs.ftp_port_label.configure(image=gs.green)
    gs.ftp_port_label.image=gs.green
    
### add stuff to the tab
    test = Label(gs.ftp_frame, text='TESTING')
    test.pack()   
    
else:
    #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
    pass  

### SSH port stuff    
if ssh_port in gs.nmap_results.get('1.0', END):   
        gs.parent_tab.add(gs.ssh_audit_tab, text='SSH Audit')

        #change port to green 
        gs.ssh_label.configure(image=gs.green)
        gs.ssh_label.image=gs.green
    ###add stuff to the tab
        threading.Thread(target=f.exec_ssh_audit).start()
        
else:
        pass
        #ports_label = tkinter.Label(ports_frame, text='There are no good ports to test').grid(row=1, column=0, sticky='W')

#### Word press
if 'WordPress' in gs.nmap_results.get('1.0', END):
        gs.parent_tab.add(gs.wp_map_tab, text='WP Audit')

        #change port to green 
        gs.wp_audit_label.configure(image=gs.green)
        gs.wp_audit_label.image=gs.green
#### add stuff to tab
        threading.Thread(target=f.exec_wordpress_map).start()        


#### Telnet port stuff
if telnet_port in gs.nmap_results.get('1.0', END):
        gs.parent_tab.add(gs.telnet_tab, text='Telnet')

        #change port to green 
        gs.telnet_label.configure(image=gs.green)
        gs.telnet_label.image=gs.green
    ###add stuff to the tab
        test = Label(gs.telnet_tab, text='TESTING')
        test.pack()   
else:
    #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
    pass  

#### SMTP port stuff
for port in smb_port:
    if port in gs.nmap_results.get('1.0', END):
            gs.parent_tab.add(gs.smtp_tab, text='SMTP')
            #change port to green 
            gs.smtp_label.configure(image=gs.green)
            gs.smtp_label.image=gs.green
        ###add stuff to the tab
            test = Label(gs.smtp_tab, text='TESTING')
            test.pack()   
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass   

#### DNS port stuff
if dns_port in gs.nmap_results.get('1.0', END):
        gs.parent_tab.add(gs.dns_tab, text='DNS')
        #change port to green 
        gs.dns_label.configure(image=gs.green)
        gs.dns_label.image=gs.green
        ###add stuff to the tab
        test = Label(gs.dns_tab, text='TESTING')
        test.pack()   
else:
    #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
    pass  

#### http port stuff
for port in http_port:
    if port in gs.nmap_results.get('1.0', END):
            gs.parent_tab.add(gs.http_tab, text='Nikto')
            #change port to green 
            gs.http_label.configure(image=gs.green)
            gs.http_label.image=gs.green
            ### add stuff to the tab
            threading.Thread(target=f.exec_nikto).start()

else:
    #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
    pass     

#### msrpc port stuff
for port in msrpc_port:
    if port in gs.nmap_results.get('1.0', END):
            gs.parent_tab.add(gs.msrpc_tab, text='MSRPC')
            #change port to green 
            gs.msrpc_label.configure(image=gs.green)
            gs.msrpc_label.image=gs.green
            ###add stuff to the tab
            test = Label(gs.msrpc_tab, text='TESTING')
            test.pack()   
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass 

#### netbios port stuff
for port in netbios_port:
    if port in gs.nmap_results.get('1.0', END):
            gs.parent_tab.add(gs.netbios_tab, text='Netbios')
            #change port to green 
            gs.netbios_label.configure(image=gs.green)
            gs.netbios_label.image=gs.green
            ###add stuff to the tab
            test = Label(gs.netbios_tab, text='TESTING')
            test.pack()   
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass     

#### smb port stuff
for port in smb_port:
    if port in gs.nmap_results.get('1.0', END):
            gs.parent_tab.add(gs.smb_tab, text='SMB')
            #change port to green 
            gs.smb_label.configure(image=gs.green)
            gs.smb_label.image=gs.green
            ###add stuff to the tab
            threading.Thread(target=f.exec_enum).start()  
    else:
        #ports_label = tkinter.Label(ports_frame, pady=50, text='There are no good ports to test')
        pass     

    

