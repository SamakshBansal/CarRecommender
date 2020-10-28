import random
import tkinter
from tkinter import *
import pandas as pd



questions =[
    "What's your budget in car ? ",
    "How much seating capacity in car ?",
    "What's your fuel preference in car ?",
    "what's your preference in body type of car ?",
    "What's your preference in color of car ?",
]

answers_choice = [
    ["Below 5 Lakhs"," Below 10 Lakhs"," Below 20 Lakhs"," Below 30 Lakhs","Below 40 Lakhs"],
    ["4","5","6","7","8"],
    ["Petrol","Diesel","Electric","Hybrid","Petrol + LPG"],
    ["Hatchback","Sedan","SUV","MVP / MUV","Convertible"],
    ["White","Black","Blue","Red","Grey"],
]

ans = [
    [500000,1000000,2000000,3000000,4000000,],
    [4,5,6,7,8],
    ["Petrol","Diesel","Electric","Hybrid","Petrol + LPG"],
    ["Hatchback","Sedan","SUV","MVP / MUV","Convertible"],
    ["White","Black","Blue","Red","Grey"],
]




def output():
    a1 = ans[0][user_answer[0]]
    a2 = ans[1][user_answer[1]]
    a3 = ans[2][user_answer[2]]
    a4 = ans[3][user_answer[3]]
    a5 = ans[4][user_answer[4]]

    df = pd.read_excel('cardatabase.xlsx')
   

    global lblTop
    lblTop = Label(
        root,
        text = 'Cars we recommend :',
        font = ("Consolas",18),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",

    )
    lblTop.pack(pady=(50,30))

    lblBottom   = Label(
        root,
        
        text = df.loc[(df['Price']<=a1) & (df['Seat']==a2) & (df['Fuel']==a3) & (df['Car Type']==a4) & (df['Color']==a5)],
        font = ("Helvetica",15),
        width = 700,
        justify = "center",
        background = "#ffffff",

    )
    lblBottom.pack(pady=(0,30))




def show():
    global lblQuestions,r1,r2,r3,r4,r5

    lblQuestions.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    r5.destroy()
    output()


user_answer= []
indexes = [0,1,2,3,4]
ques = 1

def selected():
    global radiovar,answer
    global lblQuestions,r1,r2,r3,r4,r5
    global ques
    x = radiovar.get()
    user_answer.append(x)
    if ques < 5:
        lblQuestions.config(text = questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        r5['text'] = answers_choice[indexes[ques]][4]
        
        ques+=1
    else:
        show()

    
        




def start():
    global lblQuestions
    lblQuestions = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas",20),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",

    )
    lblQuestions.pack(pady=(100,30))


    global radiovar,r1,r2,r3,r4,r5
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times",16),
        value = 0,
        variable = radiovar,
        background = "#ffffff",
        command = selected,

    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times",16),
        value = 1,
        variable = radiovar,
        background = "#ffffff",
        command = selected,

    )
    r2.pack(pady=5)
    
    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times",16),
        value = 2,
        variable = radiovar,
        background = "#ffffff",
        command = selected,

    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text =answers_choice[indexes[0]][3],
        font = ("Times",16),
        value = 3,
        variable = radiovar,
        background = "#ffffff",
        command = selected,
    )
    r4.pack(pady=5)

    r5 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][4],
        font = ("Times",16),  
        value = 4,
        variable = radiovar,
        background = "#ffffff",
        command = selected,

    )
    r5.pack(pady=5)
    



def startIsPressed():
    lableimage.destroy(),
    labeltext.destroy(),
    lblinstruction.destroy(),
    lblrules.destroy(),
    btnstart.destroy(),
    start(),
   



root = tkinter.Tk()
root.title(" Car Recommender System ")
root.geometry("800x700")
root.config(background="#ffffff")
root.resizable(0,0)

img1 = PhotoImage(file="logo.png")
lableimage = Label(
    root,
    image = img1,
    background= "#ffffff"

)
lableimage.pack(pady=(30,0))


labeltext = Label(
    root,
    text=" Welcome To Car Recommender ",
    font=("Comic sans MS",24,"bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0,30))

img2 = PhotoImage(file="Frame.png")
btnstart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command = startIsPressed,
)
btnstart.pack(pady=(0,20))

lblinstruction = Label(
    root,
    text= " Read How to Use\nClick Start to begin ",
    background="#ffffff",
    font=("Consolas,14"),
    justify = "center",
)
lblinstruction.pack(pady=(0,100))

lblrules = Label(
    root,
    text="Answer the questions according to your preference\nOnly one option can be choosen\nYou can't go back once choosen an option\nIf you choose an option it will be consider as final choice\nAt end we will recommend you cars according to your preference",
    width=100,
    font=("Times",20),
    background="#000000",
    foreground="#ffffff",

)
lblrules.pack()


root.mainloop()

