'''
Created on Oct 24, 2017

@author: Aditya

Program for demonstrating use of Progress bar and Scale Widget in tkinter

'''

import tkinter as tk
from tkinter import ttk


class ControlledProgress:
    def __init__(self, master):
        ttk.Label(master, text = "PROGRESS CONTROL").pack()
        
        # Inderterminant Progressbar
        ttk.Label(master, text = 'Inderterminant Progress').pack()
        self.prgrsbr_indtr = ttk.Progressbar(master, orient = tk.HORIZONTAL, length = 300, mode = 'indeterminate')
        self.prgrsbr_indtr.pack()
        self.checkpbi = tk.StringVar()
        self.checkpbi.set("Start")
        
        # Button
        self.btn1 = ttk.Button(master, text = "{} Inderterminant Progress Bar".format(self.checkpbi.get()), command = self.btn1cmd)
        self.btn1.pack()

        # Derterminant progress
        ttk.Label(master, text = 'Derterminant Progress').pack()
        self.prgrsbr_dtr = ttk.Progressbar(master, orient=tk.HORIZONTAL, length = 300, mode = 'determinate')
        self.prgrsbr_dtr.pack()
        self.prgrsbr_dtr.config(maximum = 10.0, value = 2.0)    # notice both these properties have float values
        
        # Button
        ttk.Button(master, text = 'Reset Progress Bar to zero', command = self.resetProgressBarVal).pack()
        
        # Button
        ttk.Button(master, text = 'Increase Progress Bar by 2', command = self.shift2ProgressBarVal).pack()
        
        # create double variable
        self.prgrsBrVal = tk.DoubleVar()
        
        self.prgrsbr_dtr.config(variable = self.prgrsBrVal) # set variable property of progressbar to look at DoubleVar()
        
        # Scale widget
        self.scalebar = ttk.Scale(master, orient = tk.HORIZONTAL, length = 400, variable=self.prgrsBrVal, from_ = 0.0, to= 10.0)
        self.scalebar.pack()
        
        # Label to display current value of scalebar
        ttk.Label(master, text = "Current value of Progress Bar is as below:").pack()
        self.scalebar_label = ttk.Label(master, textvariable = self.prgrsBrVal)
        self.scalebar_label.pack()
        
    def btn1cmd(self):
        if self.checkpbi.get() == "Start":
            self.checkpbi.set("Stop")
            self.btn1.config(text = "{} Inderterminant Progress Bar".format(self.checkpbi.get()))
            self.prgrsbr_indtr.start()
        else:
            self.checkpbi.set("Start")
            self.btn1.config(text = "{} Inderterminant Progress Bar".format(self.checkpbi.get()))
            self.prgrsbr_indtr.stop()
    
    
    def resetProgressBarVal(self):
        #self.prgrsbr_dtr.config(value = 0.0)
        self.prgrsBrVal.set(0.0)
        
    def shift2ProgressBarVal(self):
        self.prgrsbr_dtr.step(2)
        
def ControlledPorgressApp():
    root = tk.Tk()
    ControlledProgress(root)
    tk.mainloop()
    
def test():
    ControlledPorgressApp()
    
if __name__ == '__main__': test()