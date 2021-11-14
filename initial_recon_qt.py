# This is my attempt for initial recon on a target using a GUI

from tkinter import *

root = Tk()

intro_1 = Label(root, text="This program conducts initial recon on a target.").grid(row=0, column=0)
intro_2 = Label(root, text="The program uses NMAP, Nikto, and Enum4Linux.").grid(row=1, column=0)

target_ip = Entry(root, width=30).grid(row=2, column=0)

target_button = Button(root, text="Submit").grid(row=2, column=1)













root.mainloop()