# -*- coding: utf-8 -*-
"""
@author: heythomas
"""

import tkinter as tk
import clipboard
       
class window():
    def __init__(self, master):
        self.master = master
        master.title("CleverNotes")
        
        self.watcher_launched = False
        
        self.textarea = tk.Text(self.master)
        self.textarea.pack()
        
        self.text_button = tk.StringVar(self.master, 'Start Gathering')
        self.gathering_button = tk.Button(master, textvariable=self.text_button, command=self.toggle)
        self.gathering_button.pack()
        
        self.save_button = tk.Button(master, text='Save as', command=self.save)
        self.save_button.pack()
        
    def save(self):
        self.soon = tk.Tk()
        self.soon.title("Not yet :P")
        self.label_soon = tk.Label(self.soon, text='Coming soon, just paste in a .txt file for the moment')
        self.label_soon.config(font=("Arial", 15))
        self.label_soon.pack()
        self.soon.mainloop()
        
    def toggle(self):
        if self.watcher_launched:
            self.text_button.set('Gathering is Off')
            self.watcher_launched = False
        else:
            self.text_button.set('Gathering is On')
            self.watcher_launched = True
        
    def paste(self):
        global data
        if self.watcher_launched:
            self.textarea.insert('end', data+'\n')


def watcher() :
   global data
   new_data = clipboard.paste()
   # print(data, new_data)
   if new_data != data:
      data = new_data
      main_window.paste()

def watcher_loop():
    watcher()
    root.after(300, watcher_loop)

data = ''

root = tk.Tk()
main_window = window(root)
root.after(300, watcher_loop)
root.mainloop()