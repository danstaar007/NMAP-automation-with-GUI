# This is my attempt for initial recon on a target using a GUI

from tkinter import *
import tkinter

#create root frame
root = Tk()
root.title('Recon Tool')
root.geometry('500x500')

#define functions
def submit_ip():
    text = tkinter.Label(output_frame, text=target_ip.get())
    text.pack()

    #remove text in the target_ip box
    target_ip.delete(0,END)

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