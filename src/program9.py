'''
Created on Oct 26, 2017

@author: Aditya
This function demonstrates the use of frames in tkinter
'''

import tkinter as tk
from tkinter import ttk

class DisplayApp:
    def __init__(self, master):
        self.frame = ttk.Frame(master, width = 100, height = 100)   # frame height and width are in pixel
        self.frame.pack()
        self.frame.config(relief = tk.RAISED)   # to define frame boarder
        self.button = ttk.Button(self.frame, text = 'Click for Magic')
        self.button.config(command = self.performMagic)
        self.button.grid()  # use grid geometry manager
        self.frame.config(padding = (30,15))
        
        self.lbfrm = ttk.LabelFrame(master, width = 100, height = 100)
        self.lbfrm.config(padding = (30, 15))
        self.lbfrm.config(text = "Magic Below")
        self.lbfrm.pack()
        self.label = ttk.Label(self.lbfrm, text = "Waiting for Magic")
        self.label.grid()
        
    def performMagic(self):
        if self.label['text'] == "Waiting for Magic":
            self.label.config(text = 'Magic Performed')
        else:
            self.label.config(text = "Waiting for Magic")
            
def DisplayAppLaunch():
    root = tk.Tk()
    DisplayApp(root)
    tk.mainloop()
    
if __name__ == '__main__':
    DisplayAppLaunch()