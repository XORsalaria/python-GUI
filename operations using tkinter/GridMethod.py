from tkinter import *
myGui = Tk()
myGui.title("Python-GUI")
myGui.geometry("500x500+100+50")
myLabel1 = Label(text='label one',fg='red').grid(row=0,column=0)
myLabel2 = Label(text='label two',fg='green',bg='black')
myLabel2 .grid(row=2,column=0)
myGui.mainloop()
