import mysql.connector
from tkinter import *
from tkinter import messagebox

mycon=mysql.connector.connect( host="localhost",password="Sh!p",user='root',database='emailbot')
mydb=mycon
baseWindow=Tk()

def registration_fuction():
    username=enteruser.get()
    email=enteremail.get()
    try:
        mycursor = mydb.cursor()
        dataGui=(username,email)
        print(dataGui)
        sql = "insert into subscribers(USERNAME,EMAIL_adress) values('%s','%s')" % (dataGui[0],dataGui[1])
        mycursor.execute(sql)
        mydb.commit()
        messagebox.showinfo("Authentication","You Have Successful Subscribed!!!!!")
        baseWindow.withdraw()

    except mysql.connector.Error as err:
        print("ERROR OCCURED - More Details : {}".format(err))
    
baseWindow.title("SUBSCRIBE TO GET UDTATES")
baseWindow.geometry('1600x700+0+0')
titleLogin=Label(baseWindow,text="DAILY UPDATES OF DOGECOIN", compound=CENTER,\
font=('times new roman',55,'bold'),bg='steelblue',fg='turquoise',bd=30,relief=GROOVE) 
titleLogin.place(x=0,y=10,relwidth=1)
Login_Frame=Frame(baseWindow,bg='paleturquoise1')
Login_Frame.place(x=150,y=200)
lbluser=Label(Login_Frame,text='USERNAME',compound=LEFT,bg='paleturquoise1',font=('times new roman',20,'bold'))\
.grid(row=5,column=2,pady=30,padx=20,sticky=NE)
lblemail=Label(Login_Frame,text='EMAIL',compound=LEFT,bg='paleturquoise1',font=('times new roman',20,'bold'))\
.grid(row=6,column=2,pady=30,padx=20,sticky=E)
enteruser=Entry(Login_Frame,bg='white',fg='black',font=('times new roman',30,'bold'))
enteruser.grid(row=5,column=3,padx=20,pady=30,sticky=E)
enteremail=Entry(Login_Frame,bg='white',fg='black',font=('times new roman',30,'bold'))
enteremail.grid(row=6,column=3,padx=20,pady=30,sticky=E)
btlogin=Button(Login_Frame,text='SUBSCRIBE',command=registration_fuction,bg='darkslategray3',fg='gray3',font=('times new roman',20,'bold'))
btlogin.grid(row=11,column=4)    

baseWindow.mainloop()
