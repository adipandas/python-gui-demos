'''
Created on Jan 7, 2018

@author: aditya

This program demonstrates use of Toplevel windows in TKINTER
'''

import tkinter as tk
from tkinter import ttk

class TopLevelApp:
    def __init__(self, master):
        self.master = master
        master.title('Master')
        self.pop_btn = ttk.Button(master, text = 'Show Pop-up', command = self.getPop)
        self.pop_btn.pack()
        self.master.config(padx = 100, pady=50)
        
    def getPop(self):
        self.window  = tk.Toplevel(self.master)
        self.window.title('Popped')
        self.window.grab_set()
        ttk.Button(self.window, text = 'Hide Master', command = self.hideMaster).pack()
        ttk.Button(self.window, text = 'Normalize Master window', command = self.getMaster).pack()
        self.window.config(padx = 100, pady=50)
        ttk.Button(self.window, text = 'Create pop-up', command = self.getPopup).pack()
        ttk.Button(self.window, text = 'Iconify(Minimize)', command = self.iconifywindow).pack()
        
    def iconifywindow(self):
        self.window.iconify()
        
    def getPopup(self):
        self.window2  = tk.Toplevel(self.window)
        self.window2.title('Popped Up')
        self.window2.config(padx = 25, pady=25)
        self.window2.maxsize(640, 480)
        self.window2.minsize(300, 400)
        self.window2.geometry('640x480+60+60')
        self.window2.grab_set()
        ttk.Button(self.window2, text = 'Minimize', command = self.minimizePopUp).pack()
        ttk.Button(self.window2, text = 'Maximize', command = self.maximizePopUp).pack()
        ttk.Button(self.window2, text = 'Normalize', command = self.normalizePopUp).pack()
        ttk.Button(self.window2, text = 'Resize Window - TRUE', command = self.makeResizeTrue).pack()
        ttk.Button(self.window2, text = 'Resize Window - FALSE', command = self.makeResizeFalse).pack()
        ttk.Button(self.window2, text = 'Close', command = self.closewindow).pack()
    
    def makeResizeTrue(self):
        self.window2.resizable(True, True)
    
    def makeResizeFalse(self):
        self.window2.resizable(False, False)
        
    def getMaster(self):
        self.master.state('normal')
        self.window.grab_set()
        
    def hideMaster(self):
        self.master.state('withdrawn')
        
    def minimizePopUp(self):
        self.window2.state('iconic')
    
    def maximizePopUp(self):
        self.window2.state('zoomed')
        
    def normalizePopUp(self):
        self.window2.state('normal')
        
    def closewindow(self):
        self.window2.destroy()
        
def launchTopLevelApp():
    root = tk.Tk()
    TopLevelApp(root)
    tk.mainloop()
    
if __name__=='__main__':
    launchTopLevelApp()
    
    