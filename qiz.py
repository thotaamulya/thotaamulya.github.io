from tkinter import *
from time import sleep
import time
import tkinter.messagebox as messagebox
import tkinter as tk
import tkinter.font as font
class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter,view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Right!",bg="white",font=("forte",20),fg="green")
            right += 1
        else:
            label = Label(view, text="Wrong!",bg="white",font=("forte",20),fg="red")
        label.pack()
        view.after(1000, lambda *args: self.unpackview(view))


    def getview(self, window):
        view=Canvas(window,bg="darkmagenta")
        Label(view,width=50, text=self.question,fg="white",bg="darkmagenta",font=("forte",20)).pack()
        Button(view, text=self.answers[0],width=50,height=5,bg="white",fg="black",font=("forte",15),command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1],width=50,height=5,bg="white",fg="black",font=("forte",15),command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2],width=50,height=5,bg="white",fg="black",font=("forte",15),command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3],width=50,height=5,bg="white",fg="black",font=("forte",15),command=lambda *args: self.check("D", view)).pack()
        nxt=Button(view,text="next",width=25,height=3,font=("forte",10),activebackground="pink",bg="white",fg="red",command=lambda *args: self.nextto(view)).pack(side=RIGHT)
        prev=Button(view,text="previous",width=25,height=3,font=("forte",10),activebackground="pink",bg="white",fg="red",command=lambda *args: self.previousto(view)).pack(side=LEFT)
        time.sleep(0.5)
        return view

    def unpackview(self,view):
        view.pack_forget()
        askQuestion()
    def nextto(self,view):
        view.after(1000, lambda *args:self.unpackview(view) )
    def previousto(self,view):
        global index,prev
        if(index==0):
            prev.pack_forget()
        
        index -= 2
        view.after(1000, lambda *args: self.unpackview(view))
    
def askQuestion():
    global questions,window,button,index,right,p,q,number_of_questions
    if(len(questions) == index + 1):
        p=Label(window, text="Thank you for answering the questions. ",fg="navyblue",font=("forte",20)) 
        q=Label(window,text="your score is "+ str(right) + " out of " + str(number_of_questions),fg="deeppink",font=("forte",20))
        p.pack()
        q.pack()
        p.after(5000,p.destroy)
        q.after(5000,q.destroy)
        index=-1
        right=0
        return
    button.pack_forget()
    index += 1
    questions[index].getview(window).pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

def inst():
    global t
    t =Label(window, text="All you need to do is just answer each question by \nclicking on the respective button' or the actual word\n1.given questions are multichoice questions\n2.if your choosen option is correct you will score 1 point\n3.if you want to exit the game you can click EXIT button")
    myFont = font.Font(family='forte',size=16)
    t['font']=myFont
    t.pack()
    t.after(10000,t.destroy)
def mQuit():
    mExit = messagebox.askyesno(title="Quit",message="Are you sure?")
    if mExit > 0:
        window.destroy()
        return

    
window = tk.Tk()
window.title('QUIZ')
window.configure(background="green")
C = Canvas(window,height=2500, width=5000,bg="green")
filename = PhotoImage(file = "que7.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Label(window, text = 'QUIZ GAME',fg="red",font =( 
  'forte', 50)).pack(side = TOP, pady = 10)
window.state('zoomed')
myFont = font.Font(family='forte',size=30)
button = Button(window, text="START",fg="black",bg="white",command=askQuestion)
button['font']=myFont
button.pack()
button.place(relx=0.5, rely=0.4, anchor=CENTER)
button = Button(window, text="INSTRUCTIONS",fg="black",bg="white",command=inst)
button['font']=myFont
button.pack()
button.place(relx=0.5, rely=0.6, anchor=CENTER)
button= Button(window, text="EXIT",fg="black",bg="white",command=mQuit)
button['font']=myFont
button.pack()
button.place(relx=0.5, rely=0.8, anchor=CENTER)
window.mainloop()
