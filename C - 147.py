#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 12:35:51 2023

@author: apple
"""

from tkinter import *
from tkmacosx import *
root = Tk()
root.title("ascii")
root.geometry("400x400")
root.configure(background="aqua")

word = Entry(root)
word.place(relx=0.5,rely=0.4,anchor=CENTER)
label = Label(root, text = "name in ascii:", fg="black", bg="light-grey")
def asciiConverter():
    input_word = word.get()
    for letter in input_word :
        label["text"] += str(ord(letter))+ " "
        
btn = Button(root, text="show name in ascii", command=asciiConverter, bg= "gold", fg="black")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)
          
          

root.mainloop()