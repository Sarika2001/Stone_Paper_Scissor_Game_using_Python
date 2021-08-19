import tkinter
from tkinter import *#GUI Library
from PIL import Image,ImageTk
from random import randint #To generate random choice from computer
import tkinter.font as font

#Main window
root=Tk()
root.title("Sarika")
root.config(background='black')

#Images
crock=Image.open('cs.png').resize((300, 250), Image.ANTIALIAS)
crock = ImageTk.PhotoImage(crock)

cscissor = Image.open('csr.png').resize((300, 250), Image.ANTIALIAS)
cscissor = ImageTk.PhotoImage(cscissor)

cpaper = Image.open('cp.png').resize((300, 250), Image.ANTIALIAS)
cpaper = ImageTk.PhotoImage(cpaper)

urock = Image.open('us.png').resize((300, 250), Image.ANTIALIAS)
urock = ImageTk.PhotoImage(urock)

upaper = Image.open('up.png').resize((300, 250), Image.ANTIALIAS)
upaper = ImageTk.PhotoImage(upaper)

uscissor = Image.open('usr.png').resize((300, 250), Image.ANTIALIAS)
uscissor = ImageTk.PhotoImage(uscissor)

#Insert Images- Images that you want to display on root screen
user=Label(root,image=upaper,bg="black")
user.grid(row=1,column=4)
com=Label(root,image=crock,bg="black")
com.grid(row=1,column=0)

#Indicators
user_indicator=Label(root,text="User",bg="black",font=100,fg="white").grid(row=0,column=4)
com_indicator=Label(root,text="Computer",bg="black",font=100,fg="white").grid(row=0,column=0)

#Winner decision
def winner(user,comp):
    if user==comp:
        updateresult("TIE!")
    elif user=="paper":
        if comp=="scissor":
            updateresult("COMPUTER WINS!")
        else:
            updateresult("YOU WIN")
    elif user=="rock":
        if comp=="paper":
            updateresult("COMPUTER WINS!")
        else:
            updateresult("YOU WIN")
    elif user=="scissor":
        if comp=="rock":
            updateresult("COMPUTER WINS!")
        else:
            updateresult("YOU WIN")
    else:
        pass

#Buttons
#To pass arg in function we use lambda
buttonFont = font.Font(family='Arial', size=10)
rock=Button(root,width=25,height=3,bg="#FF69B4",text="ROCK",fg="black",font=buttonFont,
            command=lambda:updateimage("rock")).grid(row=2,column=1)
paper=Button(root,width=25,height=3,bg="#FAD02E",text="PAPER",fg="black",font=buttonFont,
             command=lambda: updateimage("paper")).grid(row=2,column=2)
scissor=Button(root,width=25,height=3,bg="#0ABDE3",text="SCISSOR",fg="black",font=buttonFont,
               command=lambda: updateimage("scissor")).grid(row=2,column=3)

#Changing the pictures of user& computer side as we press buttons
choice=["rock","paper","scissor"]
def updateimage(x):
    #Computer logic
    compchoice=choice[randint(0,2)]#Computer will randomly pick index from choice list
    if compchoice=="rock":
        com.configure(image=crock)
    elif compchoice=="paper":
        com.configure(image=cpaper)
    else:
        com.configure(image=cscissor)

    #User logic
    if x=="rock":
        user.configure(image=urock)
    elif x=="paper":
        user.configure(image=upaper)
    else:
        user.configure(image=uscissor)
    winner(x,compchoice)

# result
result = Label(root, font=50, bg="black", fg="white")
result.grid(row=3, column=2)

# updateresult
def updateresult(x):
    result['text'] = x

root.mainloop()
