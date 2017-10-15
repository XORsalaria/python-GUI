from tkinter import *
myGui = Tk()
def Hello():
            b = a.get()
            myLabel3 = Label(text=b,fg='white',bg='black').pack()

def Bye():
            d = c.get()
            myLabel4 = Label(text='Bye, Bot!').pack()

a = StringVar()
c = StringVar()
myGui.title("Python-GUI")
myGui.geometry("500x500+100+50")
myLabel1 = Label(text='Label One',fg='red',font=30).pack()

# Class is Button and object is myButton1

myButton1 = Button(text='enter username',font=30,command = Hello).pack()
text1 = Entry(textvariable=a).pack()
myButton2 = Button(text='enterpassword',font=30,command = Bye).pack()
text2 = Entry(textvariable=c).pack()
myGui.mainloop()
 
 
