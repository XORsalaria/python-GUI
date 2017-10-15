from tkinter import *
myGui = Tk()
myGui.title("Python-GUI")
myGui.geometry("500x500+100+100")
myLabel1 = Label(text='label one',fg='red').pack() # pack places the label in center
myLabel2 = Label(text='label two',fg='green',bg='black')
myLabel2 .pack()
myGui.mainloop()
 
 
