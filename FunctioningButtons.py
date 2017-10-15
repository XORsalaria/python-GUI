from tkinter import *
myGui = Tk()
def Hello():
            myLabel3 = Label(text='Hello, Bot!',fg='white',bg='black').pack()

def Bye():
            myLabel4 = Label(text='Bye, Bot!').pack()


myGui.title("Python-GUI")
myGui.geometry("500x500+100+50")
myLabel1 = Label(text='Label One',fg='red',font=30).pack()

# Class is Button and object is myButton1

myButton1 = Button(text='enter',font=30,command = Hello).pack()
myButton2 = Button(text='delete',font=30,command = Bye).pack()

myGui.mainloop()
 
 
