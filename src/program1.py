'''
Created on Aug 12, 2017

@author: Aditya
'''
import tkinter as tk
from tkinter import ttk

def sayhello():
    root = tk.Tk()      # call Tk constructor method to create new top level widget (main window)
    
    # Below statement creates a label with text as a 
    # child of root window and use pack geometry management method to put text on window
    tk.Label(root, text = 'Hello Python GUI').pack()
    
    # ttk = themed tk widgets
    # create button using 'themed tk widgets' (ttk)
    # parent widget of button-widget is defined as 'root' variable
    # text displayed on button defined as text = 'Click Me'
    button = ttk.Button(root, text = 'Click ME')
    button.pack()                                       # pack the button
    
    
    # find value of property from widget object
    prop_text = button['text']
    print('Value of \'{}\' property in button_obj is {}'.format('text', prop_text))
     
    # change value on button : (Note values stored as dictionary in object)
    button['text'] = 'Press ME'
     
    # use config command
    button.config(text = 'Push ME')
     
    # To print the value of all propertise of widget object
    print(button.config())
     
    # underlying TK name of the widget:
    # tkinter generates random number as a unique identifier (name) for each widget created
    print(str(button))
    print(str(root))    # 'rood window is identified as a '.' by tkinter (underlying name)
    
    
    root.mainloop()         # run mainloop method for run window
    
def test():
    sayhello()
if __name__ == '__main__':test()