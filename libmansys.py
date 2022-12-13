#Import mysql_connector for MYSQL connectivity and sys for exit
import mysql.connector
import sys


#Import tkinter, getpass, pillow for GUI
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from getpass import getpass
from functools import partial


#Establish connection with MYSQL
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin123",
    database = "library"
)


#All functions definitions
def addbook():
    bcode = int(input("Enter code: "))
    btitle = input("Enter title: ")
    bauthor = input("Enter author: ")
    bgenre = input("Enter genre: ")
    data = (bcode, btitle, bauthor, bgenre)
    sql = "insert into book_records(code,title,author,genre) values(%s,%s, %s, %s);"
    a = mydb.cursor()
    a.execute(sql, data)
    mydb.commit()
    print("Book addition successfull!")
    main()



def issuebook():
    regid = int(input("Enter your registeration ID: "))
    admin  = int(input("Enter your admission number: "))
    bcode = int(input("Enter book code: "))
    idate = input("Enter date of issuing (YYYY-MM-DD): ")
    data =(regid,admin,bcode,idate)
    sql ="insert into issued(regid,admin, code,idate) values (%s, %s, %s, %s)"
    b = mydb.cursor()
    b.execute(sql,data)
    mydb.commit()
    print("Book issued to :",admin)
    print()
    print("Book issued!")
    main()
    


def submitbook():
    regid = int(input("Enter your registeration ID: "))
    admin  = int(input("Enter your admission number: "))
    bcode = int(input("Enter book code: "))
    sdate = input("Enter date of submission (YYYY-MM-DD): ")
    data = (regid,admin,bcode,sdate)
    sql = "insert into submitted(regid,admin,code,sdate) values(%s,%s,%s,%s)"
    a = mydb.cursor()
    a.execute(sql,data)
    sql1="delete from issued where regid = %s"
    data1=(regid,)
    c = mydb.cursor()
    c.execute(sql1, data1)    
    mydb.commit()
    print("Book submitted from :",admin)
    main()



def display_issued():
    sql = "select * from issued"
    c = mydb.cursor()
    c.execute(sql)
    output = c.fetchall()
    for i in output:
        print("Registeration ID: ",i[0])
        print("Admission Number: ",i[1])
        print("Book Code: ",i[2])
        print("Issue Date: ",i[3])
        print("----------------------------")
    main()


def display_submitted():
    sql = "select * from submitted"
    c = mydb.cursor()
    c.execute(sql)
    output = c.fetchall()
    for i in output:
        print("Registeration ID: ",i[0])
        print("Admission Number: ",i[1])
        print("Book Code: ",i[2])
        print("Submission Date: ",i[3])
        print("----------------------------")
    main()


def admin_issue():
    admin = int(input("Enter your admission number: "))
    sql = "select regid, code, idate from issued where admin = %s"
    data = (admin,)
    a = mydb.cursor()
    a.execute(sql,data)
    output = a.fetchall()
    for i in output:
        print("Registeration ID: ",i[0])
        print("Book Code: ",i[1])
        print("Issue Date: ",i[2])
        print("----------------------------")
    main()


def admin_submit():
    admin = int(input("Enter your admission number: "))
    sql = "select regid, code, sdate from submitted where admin = %s"
    data = (admin,)
    a = mydb.cursor()
    a.execute(sql,data)
    output = a.fetchall()
    for i in output:
        print("Registeration ID: ",i[0])
        print("Book Code: ",i[1])
        print("Submission Date: ",i[2])
        print("----------------------------")
    main()
    


def deletebook():
    dbook = input("Enter book code: ")
    sql = "delete from book_records where code = %s"
    data = (dbook,)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("Book deleted successfully!")
    main()


def displaybook():
    sql = "select * from book_records"
    c = mydb.cursor()
    c.execute(sql)
    output = c.fetchall()
    for i in output:
        print("Book Code: ",i[0])
        print("Book Title: ",i[1])
        print("Book Author: ",i[2])
        print("Book Genre: ",i[3])
        print("----------------------------")
    main()



def main():
    print("""............LIBRARY MANAGEMENT SYSTEM.............
    1.Display all books
    2.Add a book
    3.Issue a book
    4.Submit issued book
    5.Display books issued by a particular student
    6.Display books submitted by a particular student
    7.Display list of all present issued books
    8.Display list of all submitted books
    9.Delete a book record
    10. Exit
    """)
    choice = input("Enter task no: ")
    print("............................")
    if(choice == '1'):
        displaybook()
    elif(choice == '2'):
        addbook()
    elif(choice == '3'):
        issuebook()
    elif(choice == '4'):
        submitbook()
    elif(choice == '5'):
        admin_issue()
    elif(choice == '6'):
        admin_submit()
    elif(choice == '7'):
        display_issued()
    elif(choice == '8'):
        display_submitted()
    elif(choice == '9'):
        deletebook()
    elif(choice == '10'):
        myWin = Tk()
        obj=Exit(myWin)
        myWin.mainloop()
    else:
        print("Invalid Choice!")
        main()

        

#Tkinter code for Sign in GUI
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1920x1075")
        #----IMAGE----
        self.bg=ImageTk.PhotoImage(file = "E:/School/01 Tanisha Sharma XII-Z (Library Management System)/download1.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        #----LOGIN-FRAME---
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x = 30, y = 160, height = 350, width = 400)

        title = Label(Frame_login, fg = "green",bg = "white", text = "Sign in", font = ("Impact", 35, "bold")).place(x = 80, y = 20)
        desc = Label(Frame_login, fg = "black",bg = "white" ,text = "Administrator Access", font = ("Courier New", 12, "bold")).place(x = 80, y = 78)
        title = Label(Frame_login, text = "Username", font = ("Courier New", 12, "bold"), fg="gray", bg = "white").place(x = 80, y = 110)
        self.txt_user=Entry(Frame_login, font = ("Times New Roman", 12), bg = "light gray")
        self.txt_user.place(x=80, y=140, width = 250, height = 35)
        ep=""
        title = Label(Frame_login, text = "Password", font = ("Courier New", 12, "bold"), fg="gray", bg = "white").place(x = 80, y = 180)
        self.txt_pass=Entry(Frame_login, textvariable = ep, show = "*", font = ("Times New Roman", 12), bg = "light gray")
        self.txt_pass.place(x=80, y=210, width = 250, height = 35)
        Login_btn = Button(self.root,command = self.sign_in, text = "Sign in", bg = "Green", fg = "White", bd = 0, font = ("Times New Roman", 12)).place(x = 310, y = 420, width = 50, height = 25)

    def sign_in(self):
       if self.txt_user.get()=="" or self.txt_pass.get()=="":
           messagebox.showerror("Error", "All fields are required!", parent = self.root)
       elif self.txt_user.get()!="admin" or self.txt_pass.get()!="lib123":
           messagebox.showerror("Error", "Invalid Username or Password!", parent = self.root)
       else:
           messagebox.askokcancel(message = "Welcome!")
           self.root.destroy()
           main()



#Tkinter Code for Exit/Continue in GUI 
class Exit:
    def __init__(self, myWin):
        self.myWin = myWin
        self.myWin.title("Thank you!")
        self.myWin.configure(background = "white")
        self.myWin.geometry("300x150")

        #--EXIT-FRAME--
        Frame_exit = Frame(self.myWin, bg = "white")
        Frame_exit.place(x = 0, y = 0, height = 450, width = 500)

        title = Label(Frame_exit, text = "Do you wish to sign in again or exit?", bg = "white", fg = "black", font = "Times 14").place(x = 5, y = 20)
        Exit_Button = Button(self.myWin, command = self.exit_, text = "Exit", bg = "grey", fg = "black", bd = 0, font = "Times 12").place(x = 10, y = 65, width = 50, height = 20)
        Re_Sign_in_Button = Button(self.myWin, command = self.continue_, text = "Continue", bg = "grey", fg = "black", bd = 0, font = "Times 12").place(x = 80, y = 65, width = 50, height = 20)

    def exit_(self):
        self.myWin.destroy()
        sys.exit("See you soon!")


    def continue_(self):
        self.myWin.destroy()



#Execution of tkinter root window           
root = Tk()
obj=Login(root)
root.mainloop()



#Execution of main program
main()




    
