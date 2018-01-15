'''
Created on Oct 21, 2017

@author: Aditya
This program demonstrates the use of spinbox and combobox in tkinter
'''

import tkinter as tk
from tkinter import ttk
import datetime
import calendar

class simpleCalender:
    '''
    This class creates a simple date of birth app using tkinter
    '''
    def __init__(self, master):
        ttk.Label(master, text = 'DATE OF BIRTH').pack()
        #####################################################################
        
        ttk.Label(master, text = 'Select Year').pack()
        self.year = tk.StringVar()
        self.spinbxyear = tk.Spinbox(master, from_ = 1900, 
                                 to = datetime.datetime.now().year,
                                 textvariable = self.year)
        self.spinbxyear.pack()
        
        #####################################################################
        
        ttk.Label(master, text = 'Select Month').pack()
        self.month = tk.StringVar()
        self.combobox = ttk.Combobox(master, textvariable = self.month) # textvariable - variable tied to value selected in combobox
        self.combobox.pack()
        
        # values which combobox can take
        self.combobox.config(values = ('January', 'February', 'March', 'April',
                                       'May', 'June', 'July', 'August', 'September',
                                       'October', 'November', 'December'))
        self.combobox.set('January')
        
        #####################################################################
        
        ttk.Label(master, text = 'Select Date').pack()
        self.dateofmonth = tk.StringVar()
        self.lastday = 31
        self.spinbxday = tk.Spinbox(master, from_ = 1, to = 31,
                                     textvariable = self.dateofmonth)
        self.spinbxday.pack()
        
        #####################################################################
        
        ttk.Button(master, text = "Get Date of Birth", command = self.getDOB).pack()
        
        #####################################################################
        # Display Date of Birth
        self.displaydob = ttk.Label(master, text = "Please select a date")
        self.displaydob.pack()
        
    ################ METHODS ####################################################
    def getyear(self):
        if int(self.year.get()) in range(int(self.spinbxyear['from']), int(self.spinbxyear['to']+1)):
            return int(self.year.get())
        else:
            return -1
    
    def getmonth(self):
        if self.month.get() in self.combobox['values']:
            return self.month.get()
        else:
            return -1
        
    def getdate(self):
        if int(self.dateofmonth.get()) in range(1, 32):
            return int(self.dateofmonth.get())
        else:
            return -1

    def getDOB(self):
        year = self.getyear()
        month = self.getmonth()
        
        if calendar.isleap(year) and month=='February':
            self.lastday =  29
        elif not calendar.isleap(year) and month=='February':
            self.lastday = 28
        elif month in ('January', 'March', 'May', 'July', 'August', 'October', 'December'):
            self.lastday = 31
        elif month in ('April', 'June', 'September', 'November'):
            self.lastday = 30
        else:
            self.lastday = -1
        
        if self.getdate() > self.lastday or self.getdate()<1 or self.lastday == -1:
            date = -1
        else:
            date = self.getdate()
        
        if year != -1 and month != -1 and date != -1:
            self.displaydob.config(text = '{0} {1}, {2}'.format(month, date, year))
        else:
            self.displaydob.config(text = "Invalid Date")

def launchSimpleCalenderApp():
    root = tk.Tk()
    simpleCalender(root)
    tk.mainloop()

def test():
    launchSimpleCalenderApp()

if __name__ == '__main__': test()