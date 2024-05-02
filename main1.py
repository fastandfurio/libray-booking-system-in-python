from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

mypass = "PASS@123"
mydatabase = "cb"


try:
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    print("Connection successful!")
except pymysql.Error as e:
    print("Error:", e)


root = Tk()
root.title("svkm Library")
root.minsize(width=800,height=400)
root.geometry("600x500")




root.configure(bg='slateblue1')
headingFrame1 = Frame(root,bg="slateblue3",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.7,relheight=0.16)

headingLabel = Label(headingFrame1, text=  "  WELCOME TO \n  SVKM'S Library ", bg='white', fg='RED', font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='white', fg='RED', command=addBook,font=("Arial", 12))
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='white', fg='RED', command=delete,font=("Arial", 12))
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='white', fg='RED', command=View,font=("Arial", 12))
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='white', fg='RED', command = issueBook,font=("Arial", 12))
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='white', fg='RED', command = returnBook,font=("Arial", 12))
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
