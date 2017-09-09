'''
Created on Sep 7, 2017

This program includes the demonstration of 
Checkbuttons and Radio Buttons using Tkinter

@author: Aditya
'''

import tkinter as tk
from tkinter import ttk

class Button2App():
    def __init__(self, master):
        
        # More advanced as compared to regular buttons 
        # Check buttons can also store binary values
        self.checkbutton = ttk.Checkbutton(master, text = 'Check Me!')
        self.checkbutton.pack()
        self.label = ttk.Label(master, text = 'Ready!! Nothing has happened yet.')
        self.label.pack()
        # Tkinter variable classes
        # self.boolvar = tk.BooleanVar()   # boolean type variable of tk
        # self.dblvar = tk.DoubleVar()     # double type variable of tk
        # self.intvar = tk.IntVar()        # int type variable of tk
        self.checkme = tk.StringVar()     # string type variable of tk
        self.checkme.set('NULL')            # set value for string type tkinter variable
        print('Current value of checkme variable is \'{}\''.format(self.checkme.get()))
        
        # setting of binary value for check button: 1. onvaalue and 2. offvalue
        self.checkbutton.config(variable = self.checkme, onvalue = 'I am checked!!', offvalue = 'Waiting for someone to check me!')
        self.checkbutton.config(command = self.oncheckme)
        
        
        # creating another tkinter string type variable - StringVar
        self.papertype = tk.StringVar()     # created a variable
        self.radiobutton1 = ttk.Radiobutton(master, text = 'Paper1', variable=self.papertype, value = 'Robotics Research')
        self.radiobutton1.config(command = self.onselectradio)
        self.radiobutton1.pack()
        self.radiobutton2 = ttk.Radiobutton(master, text = 'Paper2', variable=self.papertype, value = 'Solid Mechanics Research')
        self.radiobutton2.config(command = self.onselectradio)
        self.radiobutton2.pack()
        self.radiobutton3 = ttk.Radiobutton(master, text = 'Paper3', variable=self.papertype, value = 'Biology Research')
        self.radiobutton3.config(command = self.onselectradio)
        self.radiobutton3.pack()
        self.radiobutton4 = ttk.Radiobutton(master, text = 'Paper4', variable=self.papertype, value = 'SPAM Research')
        self.radiobutton4.config(command = self.onselectradio)
        self.radiobutton4.pack()
        self.radiobutton5 = ttk.Radiobutton(master, text = 'Change Checkme text', variable=self.papertype, value = 'Radio Checkme Selected')
        self.radiobutton5.pack()
        self.radiobutton5.config(command = self.onradiobuttonselect)

    def oncheckme(self):                # callback function for checkbutton
        txt = self.checkme.get()        # get the value of stringVar checkme
        self.label.config(text = txt)   # display the value of checkme in label
        
    def onradiobuttonselect(self):
        self.checkbutton.config(textvariable = self.papertype)
        
    def onselectradio(self):
        self.label.config(text = self.papertype.get())
        
def launchButton2App():
    root = tk.Tk()
    Button2App(root)
    tk.mainloop()
    
def test():
    launchButton2App()

if __name__ == '__main__':
    test()