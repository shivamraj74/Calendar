from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
import pyshorteners
import webbrowser


def logic():
     s=pyshorteners.Shortener()
     a=s.tinyurl.short("https://shivamraj.herokuapp.com/")
     messagebox.showinfo("This is your URL",a)

def callback():
     url="www.google.com"
     webbrowser.open_new(url)

top=ThemedTk(theme="scidgrey")
top.title("AK url shortner")
top.geometry("500x500")
filename=PhotoImage(file="A:\Edits\Link.png")
background_label=Label(top,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

b1=ttk.Button(top,text="Click to the open the Link",command=callback).pack()
b2=ttk.Button(top,text="Click to shorten the Url",command=logic).pack()

top.mainloop()
