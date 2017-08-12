'''
Created on Aug 12, 2017

@author: Aditya
'''

import tkinter as tk
from tkinter import ttk

class Helloapp:
    def __init__(self, master):
        # display label in main window master
        self.label = ttk.Label(master, text = 'Hello, World and This is Python3.6 speaking')
        
        # place the label using grid method in the main window
        self.label.grid(row =0, column =0, columnspan=2)  
        
        # Create and place button below label
        ttk.Button(master, text = 'Delhi', command = self.delhi_hello).grid(row=1, column=0)
        ttk.Button(master, text = 'Pune', command = self.pune_hello).grid(row=1, column=1)
        
    def delhi_hello(self):
        self.label.config(text = 'Namaste Duniya, main Python hu.')

    def pune_hello(self):
        self.label.config(text = 'Bhava, hey Python3.6 ahe.')
        
        

def HelloAppLaunch():
    root = tk.Tk()
    Helloapp(root)
    root.mainloop()
    
def test():
    HelloAppLaunch()

if __name__ == '__main__':test()