from tkinter import *
myGui = Tk()
NewWin = Tk()
def Hello():
   
            myLabel3 = Label(myGui,text=a,fg='white',bg='black').pack()

def Bye():
            d = a.get()
            myLabel4 = Label(NewWin,text=d).pack()

a = StringVar()



myGui.title("Python-GUI version1")
NewWin.title("Python-GUI version2")

myGui.geometry("400x400+600+50")
NewWin.geometry("400x400+600+50")

myLabel1 = Label(text='Label One',fg='red',font=30).pack()

# Class is Button and object is myButton1

myButton1 = Button(myGui,text='Enter Your Story! :)',font=30,command = Hello).pack()
text1 = Entry(myGui,textvariable=a).pack()

myButton2 = Button(NewWin,text='Show Stories!',font=30,command = Bye).pack()

myGui.mainloop()
