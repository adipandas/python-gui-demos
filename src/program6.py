'''
Created on Sep 17, 2017

@author: Aditya

This code demonstrates the use of text entry widget in tkinter
'''

import tkinter as tk
from tkinter import ttk

class entryApp:

    def __init__(self, master):
        self.label = ttk.Label(master, text='Enter the text below')
        self.label.pack()
        
        self.entry = ttk.Entry(master, width = 30)  # number of characters along the width
        self.entry.pack()
        
        self.button = ttk.Button(master, text = "Get Entry")
        self.button.pack()
        self.tkstrvar = tk.StringVar()  # create tk string variable
        self.tkstrvar.set('Nothing is done yet!')   # set the value of tk string variable
        self.button.config(command = self.getEntry)
        
        self.msg = ttk.Label(master, text = self.tkstrvar.get())    # get the value of string variable
        self.msg.pack()
        
        self.btn1 = ttk.Button(master, text='Delete the entry', command = self.btn1func)
        self.btn1.pack()
        
        self.crypt = tk.StringVar()
        self.crypt.set('Encrypt')
        self.btn2 = ttk.Button(master, text = "{} Text in Entry Field".format(self.crypt.get()), command = self.changecrypt)
        self.btn2.pack()
        #self.entryText = ttk.Entry(master, width=30)
        
        ttk.Button(master, text = 'Disable Entry Field', command = self.btn3func).pack()
        ttk.Button(master, text = 'Enable Entry Field', command = self.btn4func).pack()
        ttk.Button(master, text = 'Readonly Entry Field', command = self.btn5func).pack()
        ttk.Button(master, text = 'Edit Entry Field', command = self.btn6func).pack()
    
    def changecrypt(self):
        if self.crypt.get()=='Encrypt':
            self.entry.config(show='*')
            self.crypt.set('Decrypt')
            self.btn2.config(text = "{} Text in Entry Field".format(self.crypt.get()))
        else:
            self.entry.config(show='')
            self.crypt.set('Encrypt')
            self.btn2.config(text = "{} Text in Entry Field".format(self.crypt.get()))
    
    def btn3func(self):
        self.entry.state(['disabled'])
    
    def btn4func(self):
        self.entry.state(['!disabled'])
        
    def btn5func(self):
        self.entry.state(['readonly'])
        
    def getEntry(self):
        self.tkstrvar.set(self.entry.get())     # get entry widget content and store it in tk_string variable
        self.msg.config(text = self.tkstrvar.get())   # set msg as value of string variable
        
    def btn1func(self):
        self.entry.delete(0, tk.END)    # delete all from 0 to END character in Entry Widget

    def btn6func(self):
        self.entry.state(['!readonly'])


def launchEntryApp():
    root = tk.Tk()
    entryApp(root)
    tk.mainloop()


def test():
    launchEntryApp()
            
if __name__ == '__main__': test()
