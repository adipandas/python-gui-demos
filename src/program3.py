'''
Created on Aug 13, 2017

@author: Aditya

this program demosntrates the use of Label widgets.

'''

import tkinter as tk
from tkinter import ttk

class GreetingApp:
    
    def __init__(self, master):     # constructor method
        # define list of label texts
        self.greet_list = ('Hello, World! This is python GUI.', \
                           'Hello, This is Python GUI. Sadly, I was made to say Hello only. I will love to say so much more.')
        
        # creat label as a child of root window with some text.
        self.label = ttk.Label(master, text = self.greet_list[0])
        
        self.btn = ttk.Button(master, text = 'Greet Again', command = self.handle_text) # create a button
        
        # store image in the label obj to keep it in the scope as 
        # long as label is displayed and to avoid getting the image getting garbage collected
        imgpath = 'simple_gif.gif'
        self.label.img = tk.PhotoImage(file = imgpath)    
        self.label.config(compound = 'left') # to display image in left of text
        
        
        self.label.pack()       # pack label to the window with pack() geometry method of Label
        self.btn.pack()
        self.label.config(wraplength = 200)
        self.label.config(justify = tk.CENTER) # justify can be CENTER, RIGHT, LEFT
        self.label.config(foreground = 'blue', background = 'yellow')   # insert font color (foreground) and background color
        self.label.config(font = ('Times', 10, 'bold'))         # font = (font_name, font_size, font_type)
        
        # store image in the label obj to keep it in the scope as 
        # long as label is displayed and to avoid getting the image getting garbage collected
        imgpath = 'simple_gif.gif'
        self.label.img = tk.PhotoImage(file = imgpath)
        self.label.config(image = self.label.img)    
        self.label.config(compound = 'left') # to display image in left of text
        
    def handle_text(self):
        if self.label['text'] == self.greet_list[0]:
            self.label.config(text = self.greet_list[1])
        else:
            self.label.config(text = self.greet_list[0])
    
def test():
    root = tk.Tk()
    GreetingApp(root)
    root.mainloop()

if __name__ == '__main__': test()