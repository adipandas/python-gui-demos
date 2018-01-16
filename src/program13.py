'''
Created on Jan 14, 2018

@author: aditya

Tkinter Text Widget demo
Text widget is complex and very useful. It can have multiple lines 
and various kind of manipulations on text are possible
Uses: Data logging, user instructions, message display, text input from user in survey like forms.

Please refer tk documentation for text widget details for more information

Indexing in text widget:
- Lines are numbered starting with '1'.
- Characters are numbered starting with '0'.
    example - Base string, '1.0', refers to the first character in the first line of text box.
- 'end' refers to the position after the last character of a line
- Please refer the indices section of tkinter documentation of Text Widget for more details

Tags can be created in text widget to modify words/text at various locations with some logic.
Tags are mapped to the specified locations/indices of text in Text widget.
So it is possible to use these tags for text modification instead of text indices. 
Therefore, making it convenient for programming.


'''

import tkinter as tk
from tkinter import ttk


class App(object):

    def __init__(self, master):
        self.master = master
        self.text = tk.Text(self.master, width = 50, height = 20)
        self.text.pack()
        self.text.config(wrap = 'word')     # wrap = 'word' or 'none' or 'char' - default is 'char'
        
        self.btn0 = ttk.Button(self.master, text ='Insert random Text in TExt field', command=self.randomTextEntry)
        self.btn0.pack()
        
        self.btn1 = ttk.Button(self.master, text = 'Get all text in line 1', command = self.getline1text)
        self.btn1.pack()
        
        self.btn2 = ttk.Button(self.master, text = 'Get All Text', command = self.getAllText)
        self.btn2.pack()
        
        self.btn3 = ttk.Button(self.master, text = 'Insert "My Name is \nAdi" on 3rd Line', command = self.putTextat3rdLine)
        self.btn3.pack()
        
        self.btn4 = ttk.Button(self.master, text = 'Delete First Character of Text', command = self.deleteFirst)
        self.btn4.pack()
        
        self.btn5 = ttk.Button(self.master, text = 'Delete from 5 to 7 of line 3', command = self.delete5to8on3)
        self.btn5.pack()
        
        self.btn6 = ttk.Button(self.master, text = 'Delete first 3 lines', command = self.deleteFirst3Lines)
        self.btn6.pack()
        
        self.btn7 = ttk.Button(self.master, text = 'Replace line 1 with random text', command = self.replaceRandom)
        self.btn7.pack()
    
        self.btn8 = ttk.Button(self.master, text = 'Disable Text Field', command = self.disableEnable)
        self.btn8.pack()
        
        self.lbl1 = ttk.Label(self.master, text = 'Waiting to display TEXT....')
        self.lbl1.pack()
        
        
        self.btn9 = ttk.Button(self.master, text = 'Create tag named \'myTag\' at line 2', command = self.tagDemo)
        self.btn9.pack()
        
    def tagDemo(self):
        if self.btn9['text']=='Create tag named \'myTag\' at line 2':
            self.btn9.config(text = 'Remove Tag')
            self.text.tag_add('myTag', '2.0', '2.0 lineend')
            
            self.btn10 = ttk.Button(self.master, text = 'Change myTag background to yellow', command = self.tagbgyellow)
            self.btn10.pack()
            
            self.btn11 = ttk.Button(self.master, text = 'Remove tag from 1st word of line 2', command = self.tagrm21word)
            self.btn11.pack()
            
            self.btn12 = ttk.Button(self.master, text = 'myTag Span', command = self.getTagSpan)
            self.btn12.pack()
            
            self.btn13 = ttk.Button(self.master, text = 'Show all Tags in Text widget', command = self.displayAllTags)
            self.btn13.pack()
            
        else:
            self.btn9.config(text = 'Create tag named \'myTag\' at line 2')
            self.text.tag_delete('myTag')
            self.btn10.destroy()
            self.btn11.destroy()
            self.btn12.destroy()
            self.btn13.destroy()
            
    def getTagSpan(self):
        self.lbl1.config(text = self.text.tag_ranges('myTag'))
        
    def displayAllTags(self):
        self.lbl1.config(text = self.text.tag_names())
        
    def tagrm21word(self):
        self.text.tag_remove('myTag', '2.0', '2.0 wordend')
    def tagbgyellow(self):
        self.text.tag_configure('myTag', background = 'yellow')
        
    def randomTextEntry(self):
        text = '''Random Text
It real sent your at. 
Amounted all shy set why followed declared. 
Repeated of endeavor mr position kindness offering ignorant so up. 
Simplicity are melancholy preference considered saw companions.
Disposal on outweigh do speedily in on. Him ham although thoughts entirely drawings.
Acceptance unreserved old admiration projection nay yet him.
Lasted am so before on esteem vanity oh. 

Moments its musical age explain.
But extremity sex now education concluded earnestly her continual. 
Oh furniture acuteness suspected continual ye something frankness.
Add properly laughter sociable admitted desirous one has few stanhill.
Opinion regular in perhaps another enjoyed no engaged he at.
It conveying he continual ye suspected as necessary.
Separate met packages shy for kindness. 

For norland produce age wishing. 
To figure on it spring season up.
Her provision acuteness had excellent two why intention.
As called mr needed praise at. 
Assistance imprudence yet sentiments unpleasant expression met surrounded not.
Be at talked ye though secure nearer. 

So by colonel hearted ferrars.
Draw from upon here gone add one. 
He in sportsman household otherwise it perceived instantly.
Is inquiry no he several excited am.
Called though excuse length ye needed it he having.
Whatever throwing we on resolved entrance together graceful.
Mrs assured add private married removed believe did she. 

Prepared is me marianne pleasure likewise debating.
Wonder an unable except better stairs do ye admire.
His and eat secure sex called esteem praise.
So moreover as speedily differed branched ignorant.
Tall are her knew poor now does then.
Procured to contempt oh he raptures amounted occasion.
One boy assure income spirit lovers set. 
'''
        self.text.insert('1.0', text)
    
    def disableEnable(self):
        if self.btn8['text']=='Disable Text Field':
            self.btn8.config(text='Enable Text Field')
            self.text.config(state = 'disabled')
        else:
            self.btn8.config(text='Disable Text Field')
            self.text.config(state = 'normal')
    
    def replaceRandom(self):
        self.text.replace('1.0', '1.0 lineend', 'This is random line 1.')
        
    def deleteFirst3Lines(self):
        self.text.delete('1.0', '3.0 lineend + 1 chars')
    
    def delete5to8on3(self):
        self.text.delete('3.5', '3.8')
        
    def deleteFirst(self):
        self.text.delete('1.0')   

    def putTextat3rdLine(self):
        self.text.insert('1.0 + 2 lines lineend', '. My Name is \nAdi. And Yo \nAnd Yo...')
        
    def getline1text(self):
        if self.btn1['text']== 'Get all text in line 1':
            self.lbl1.config(text = self.text.get('1.0', '1.end'))
            self.btn1.config(text = 'Refresh')
        else:
            self.lbl1.config(text = 'Waiting to display TEXT....')
            self.btn1.config(text = 'Get all text in line 1')    
        
    def getAllText(self):
        if self.btn2['text']=='Get All Text':
            self.lbl1.config(text = self.text.get('1.0', 'end'))
            self.btn2.config(text = 'Refresh')
        else:
            self.lbl1.config(text = 'Waiting to display TEXT....')
            self.btn2.config(text = 'Get All Text')
            
def launchApp():
    root = tk.Tk()
    App(root)
    tk.mainloop()
    
if __name__=='__main__':
    launchApp()