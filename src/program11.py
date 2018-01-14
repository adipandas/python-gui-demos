'''
Created on Jan 7, 2018

@author: aditya

This program demonstrates the use of Paned Window from Tkinter
'''

import tkinter as tk
from tkinter import ttk

class PanedWindowApp:
    def __init__(self, master):
        self.master = master
        self.panedWindow = ttk.Panedwindow(self.master, orient = tk.HORIZONTAL)  # orient panes horizontally next to each other
        self.panedWindow.pack(fill = tk.BOTH, expand = True)    # occupy full master window and enable expand property
        
        self.frame1 = ttk.Frame(self.panedWindow, width = 100, height = 300, relief = tk.SUNKEN)
        self.frame2 = ttk.Frame(self.panedWindow, width = 400, height = 400, relief = tk.SUNKEN)
        
        self.panedWindow.add(self.frame1, weight = 1)
        self.panedWindow.add(self.frame2, weight = 3)
        
        self.button = ttk.Button(self.frame1, text = 'Add frame in Paned Window', command = self.AddFrame)
        self.button.pack()
        
        
        
    def AddFrame(self):
        if self.button['text']=='Add frame in Paned Window':
            self.frame3 = ttk.Frame(self.panedWindow, width = 50, height=400, relief = tk.SUNKEN)
            self.panedWindow.insert(1, self.frame3)     # default weight=0
            self.button.config(text = 'Remove/Forget Added Frame')
        else:
            self.panedWindow.forget(1)
            self.button.config(text = 'Add frame in Paned Window')
            
def launchPanedWindowApp():
    root = tk.Tk()
    PanedWindowApp(root)
    tk.mainloop()

if __name__=='__main__':
    launchPanedWindowApp()
        
        
        
        