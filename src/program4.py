'''
Created on Aug 20, 2017

@author: Aditya

This program demonstrates the use of button widget in tkinter
'''

import tkinter as tk
from tkinter import ttk

class ButtonApp:
    def __init__(self, master):
        self.button = ttk.Button(master, text = 'Click me')
        self.button.pack()
        self.button.config(command = self.buttonfunc)          # configure a command for button click
        
        self.btn1 = ttk.Button(master, text = 'Click on \'Click me\'', command = self.invokebutton)
        self.btn1.pack()
        
        self.btn2 = ttk.Button(master, text = 'Disable \'Click me\'', command = self.disableButton)
        self.btn2.pack()
        
        self.btn3 = ttk.Button(master, text = 'Enable \'Click me\'', command = self.enableButton)
        self.btn3.pack()
        
        self.btn4 = ttk.Button(master, text = 'Query state of \'Click me\'', command = self.queryButtonState)
        self.btn4.pack()
        
        self.button.img  = tk.PhotoImage(file = 'simple_gif.gif')
        self.button.img = self.button.img.subsample(10, 10) # take every 5th pixel in x and y direction of image
        
        self.btn5 = ttk.Button(master, text = 'Add image to \'Click me\'', command = self.addImage)
        self.btn5.pack()
        
        self.label = ttk.Label(master, text = 'No button pressed yet.')
        self.label.pack()
        
    def buttonfunc(self):
        self.label.config(text = 'Clicked!!')
    
    def invokebutton(self):
        self.button.invoke()    # invoke the button
        
    def disableButton(self):
        if self.button.instate(['disabled']):
            self.label.config(text='\'Click me\' is already disabled.')
        else:
            self.button.state(['disabled'])      # returns the previous state of button and sets the new state
            self.label.config(text = '\'Click me\' is disabled.')
        
    def queryButtonState(self):
        if self.button.instate(['disabled']):
            self.label.config(text = '\'Click me\' is in diabled state.')
        else:
            self.label.config(text = '\'Click me\' is in enabled state.')
    
    def enableButton(self):
        if self.button.instate(['!disabled']):
            self.label.config(text = '\'Click me\' is already enabled')
        else :
            self.button.state(['!disabled'])
            self.label.config(text = '\'Click me\' is enabled')
    
    def addImage(self):
        self.button.config(image = self.button.img, compound = tk.LEFT)
            
def launchButtonApp():
    root = tk.Tk()  # instantiate the main window class by creating its object
    ButtonApp(root)
    tk.mainloop()

def test():
    launchButtonApp()

if __name__ == '__main__': test()