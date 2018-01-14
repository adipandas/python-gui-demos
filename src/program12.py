'''
Created on Jan 14, 2018

@author: aditya

This program shows the use of notebook in tkinter
Notebook is used to create Tabs in the application.
This enables browsing different pages in the application.

Frame widget from tkinter is used in this Application to demostrate the use of Notebook/tabs.
Please note that other widgets can also be used as per the requirement.
'''

import tkinter as tk
from tkinter import ttk

class NoteBookApp:
    def __init__(self, master):
        self.master = master
        self.notebk = ttk.Notebook(self.master)
        self.notebk.pack()
        self.frame1 = ttk.Frame(self.notebk, width = 400, height = 400, relief = tk.SUNKEN)
        self.frame2 = ttk.Frame(self.notebk, width = 400, height = 400, relief = tk.SUNKEN)
        self.notebk.add(self.frame1, text = 'One')
        self.notebk.add(self.frame2, text = 'Two')
        
        self.btn = ttk.Button(self.frame1, text='Add/Insert Tab at Position 1', command = self.AddTab)
        self.btn.pack()
        
        self.btn2 = ttk.Button(self.frame1, text='Disable Tab at Position 1', command = self.disableTab)
        self.btn2.pack()

        strdisplay = r'Tab ID:{}'.format(self.notebk.select())
        ttk.Label(self.frame1, text = strdisplay).pack()
        
        strdisplay2 = 'Tab index:{}'.format(self.notebk.index(self.notebk.select()))
        ttk.Label(self.frame1, text = strdisplay2).pack()
        
    def AddTab(self):
        if self.btn['text'] == 'Add/Insert Tab at Position 1':
            self.frame3 = ttk.Frame(self.notebk, width = 400, height = 400, relief = tk.SUNKEN)
            self.notebk.insert(1, self.frame3, text = 'Additional Tab')
            self.btn.config(text = 'Remove/Forget Tab')
        else:
            self.notebk.forget(1)
            self.btn.config(text = 'Add/Insert Tab at Position 1')
    
    def disableTab(self):
        # properties of tab - accessible by using notbook.tab(tab_id, option)
        # to see available properties - print(notbook.tab(tab_id))
        if self.btn2['text'] == 'Disable Tab at Position 1':
            self.notebk.tab(1, state = 'disabled')
            self.btn2.config(text = 'Hide Tab at Position 1')
        elif self.btn2['text'] == 'Hide Tab at Position 1':
            self.notebk.tab(1, state = 'hidden')
            self.btn2.config(text = 'Normalize Tab at Position 1')
        elif self.btn2['text']== 'Normalize Tab at Position 1':
            self.notebk.tab(1, state = 'normal')
            self.btn2.config(text = 'Disable Tab at Position 1')
        

def launchNoteBookApp():
    root = tk.Tk()
    NoteBookApp(root)
    tk.mainloop()
    

if __name__=='__main__':
    launchNoteBookApp()
    
        