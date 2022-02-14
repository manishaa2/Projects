import tkinter
from tkinter import*
import random
from tkinter import messagebox 
from random import shuffle

root= tkinter.Tk()
root.title("Jumble Word Game")
root.geometry("600x600")
answer=["lavender", "sulphur", "telecom", "colony", "british", "bhatbhateni", "tesla", "suitcase"]
words=[]

for i in answer:
    word=list(i)
    shuffle(word)
    words.append(word)
num = random.randint(0, len(words)-1)

def initial():
    global words, answer, num
    lb1.configure(text=words[num])
def ans_check():
    global words, answer, num
    player_input = e1.get()
    if player_input==answer[num]:
        messagebox.showinfo("result","correct next one please")
        reset()
    else:
        messagebox.showinfo("result","try again!")
        e1.delete(0, END)
    
def reset():
    global words, answer, num
    num = random.randint(0, len(words)-1)
    lb1.configure(text=words[num])
    e1.delete(0,END)

lb1=Label(root, font='times 20')
lb1.pack(pady=30, ipadx=10, ipady=10)

answers=StringVar

e1=Entry(root, textvariable=answer)
e1.pack(ipady=5, ipadx=5)
b1=Button(root, text="Check", width=20, command=ans_check, bg="green")
b1.pack(pady=40)
b2=Button(root, text="Reset", width=20, command=reset, bg="sky blue")
b2.pack()
initial()
root.mainloop()