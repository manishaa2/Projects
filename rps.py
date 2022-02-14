from tkinter import *
from tkinter import messagebox
import datetime
import random

def HIstory(): 
    try:
        with open('game.txt', 'r') as ptr:
            totalLines = '' 
            for line in (ptr.readlines()[-12:]):
                totalLines +=line
    except Exception as exc:
        with open('game.txt', 'w') as f:
            f.write('')
            
    history = Tk()
    history.title("History")
    history.geometry("600x600")
    content =Label(history, text=totalLines, font=("times",18))
    content.pack(pady = 20)

def ComputerTurn():
    global a
    num= random.randint(0,2)
    ansComp = Label(root, fg= 'green', font = ('times', 23, 'bold'))
    ansComp.place(x=250, y = 110)
    
    if num == 0:
        ansComp.config(text= f'Computer chosed: rock     ')
    elif num == 1:
        ansComp.config(text= f'Computer chosed: paper    ')
    else:
        ansComp.config(text= f'Computer chosed: scissor')
    if num == a:
        messagebox.showinfo('Result', "The game is tie")
        with open("game.txt", 'a') as ptr:
            ptr.write(f'{datetime.datetime.now()} --  The game is tie.\n')
    else:
        if num==0 and a == 1:
            messagebox.showinfo('Result', "You won")
            with open("game.txt", 'a') as ptr:
                ptr.write(f'{datetime.datetime.now()} --  You Won\n')
            
        elif num == 1 and a == 2:
            messagebox.showinfo('Result', "You won")
            with open("game.txt", 'a') as ptr:
                ptr.write(f'{datetime.datetime.now()} --  You Won\n')
        elif num == 2 and a == 0:
            messagebox.showinfo('Result', "You won")
            with open("game.txt", 'a') as ptr:
                ptr.write(f'{datetime.datetime.now()} --  You Won\n')
        else:
            messagebox.showinfo('Result', "Computer won")
            with open("game.txt", 'a') as ptr:
                ptr.write(f'{datetime.datetime.now()} --  Computer Won\n')


def Rock():
    global a
    answer.config(text= f"You chosed: rock ") 
    a = 0
    ComputerTurn()

def Paper():
    global a
    answer.config(text= f"You chosed: paper") 
    a = 1
    ComputerTurn()
   
def Scissor():
    global a
    answer.config(text= f"You chosed: scissor") 
    a = 2
    ComputerTurn()


root =Tk()
root.geometry('600x400+500+200')
root.title("Rock Paper Scissors")
rock= Button(root,text=" Rock  ", font= ('times', 40),bg="light green",command=Rock)
rock.grid(row=1,column=0,padx=3,pady=3)
paper= Button(root,text=" Paper ",font= ('times', 40),bg="red",command=Paper)
paper.grid(row=2,column=0,padx=3,pady=3)
scissor= Button(root,text="Scissor",font= ('times', 40),bg="lavender",command=Scissor)
scissor.grid(row=3,column=0,padx=3,pady=3)
answer= Label(root, fg= 'green',font = ('times', 30, 'bold'))
answer.place(x=250, y = 70)

history = Button(root,text = "History", font=('times', 20), bg= 'skyblue', command = HIstory)
history.place(x= 10, y= 340)
exitButton= Button(root,text = "Exit", font=('times', 20), bg= 'yellow', command = root.destroy)
exitButton.place(x= 500, y= 340)
root.mainloop()
