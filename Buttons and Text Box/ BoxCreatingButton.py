from tkinter import *
myGui = Tk()
myGui.title("Python-GUI")
myGui.geometry("500x500+100+50")
myLabel1 = Label(text='label one',fg='red').pack()

# Class is Button and object is myButton1

myButton1 = Button(text='enter',fg='blue',bg='green').pack()
myButton2 = Button(text='delete',fg='blue',bg='green').pack()

myGui.mainloop()
 
 
