import mysql.connector
from tkinter import *

# establishing SQL connection

db = mysql.connector.connect(host="localhost", user ="root", password = "1245", database ="tkinterData")
mycur = db.cursor()

# mycur.execute("create database tkinterData")
# for x in mycur:
#     print(x)

# mycur.execute("show databases ")
# for x in mycur:
#     print(x)

# creating table 
# mycur.execute("create table marks(roll int(4), name varchar(20), physics float(20), maths float(20), science float(20), IT float(20)) ")

# mycur.execute("show tables")
# for x in mycur:
#     print(x)

#  Playing with Tkinter

window =Tk()
window.title("Submit Your Marks")
window.geometry('550x550')

head = Label(window,text = "Enter your Credentials ", fg ="blue",font= "comicsansms 19 bold",pady = "18")
head.grid(row=0, column= 4)  # Any randow value for now

l1 = Label(window,text ="Roll: ", fg ="purple",font= "comicsansms 15 bold",pady = "2")
l2 = Label(window,text ="Name: ", fg ="purple",font= "comicsansms 15 bold",pady = "2")
l3 = Label(window,text ="Physics: ", fg ="purple",font= "comicsansms 15 bold",pady = "2")
l4 = Label(window,text ="Maths: ", fg ="purple",font= "comicsansms 15 bold",pady = "2")
l5 = Label(window,text ="Science: ", fg ="purple",font= "comicsansms 15 bold",pady = "2")
l6 = Label(window,text ="IT: ", fg ="purple",font= "comicsansms 15 bold",pady = "2")


l1.grid(row = 1, column =3)
l2.grid(row = 2, column =3)
l3.grid(row = 3, column =3)
l4.grid(row = 4, column =3)
l5.grid(row = 5, column =3)
l6.grid(row = 6, column =3)

# Creating Entrys

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)
e5 = Entry(window)
e6 = Entry(window)

e1.grid(row = 1, column =4)
e2.grid(row = 2, column =4)
e3.grid(row = 3, column =4)
e4.grid(row = 4, column =4)
e5.grid(row = 5, column =4)
e6.grid(row = 6, column =4)

#  Writing Fucntion of insert and view :)

def insert():
    n1 = int(e1.get())
    n2 = e2.get()
    n3 = float(e3.get())
    n4 = float(e4.get())
    n5 = float(e5.get())
    n6 = float(e6.get())

    #  Writing SQL conditions
    sqlL = "insert into marks value (%s,%s,%s,%s,%s,%s)"
    valL = (n1,n2,n3,n4,n5,n6)
    mycur.execute(sqlL, valL)
    db.commit()

def view():
    mycur.execute("select * from marks")
    valV = mycur.fetchall()

    TxtG = Text(window ,height = 14, width = 23) # Random opp
    TxtG.grid(row = 10, column = 4)

    TxtG.insert(INSERT,valV)

#  creating buttons to fetch 

b1 = Button(text = 'insert', command =insert,font ="comicsansms 10 bold",fg ="red", bg ="grey")
b2 = Button(text = 'view', command = view,font ="comicsansms 10 bold",fg ="red", bg ="grey")

b1.grid(row = 7, column = 4)
b2.grid(row = 7, column = 6)


window.mainloop()

# hurray done Addind Some styleing

# Done Code Available in github:)
