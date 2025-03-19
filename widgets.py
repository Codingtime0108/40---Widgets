from tkinter import *
from datetime import date

root = Tk()
root.title("Learn about widgets")
root.geometry("400x300")

lbl = Label(text="Hey There!", fg="white", bg="#09e6ed", height=1, width = 300) 

name_lbl = Label(text="Full Name", bg="#3895D3" )
name_entry = Entry()

def display():

    name = name_entry.get()
    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello "+name+"\n"
    text_box.insert(END, greet) 
    text_box.insert(END, message) 
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="Begin", command=display, height=1, bg="#ed0959", fg= "pink")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()