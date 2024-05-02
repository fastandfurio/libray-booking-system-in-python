

from tkinter import *
from tkinter import messagebox
import pymysql

# Connect to MySQL
mypass = "PASS@123"
mydatabase = "hi"
try:
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    print("Connection successful!")
except pymysql.Error as e:
    print("Error:", e)

# Define table names
issueTable = "books_issued"
bookTable = "books"

# List to store all Book IDs
allBid = []

def returnn():
    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1

    bid = bookInfo1.get()

    extractBid = "SELECT bid FROM " + issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        issueSql = "DELETE FROM " + issueTable + " WHERE bid = %s"
        updateStatus = "UPDATE " + bookTable + " SET status = 'avail' WHERE bid = %s"

        if bid in allBid:
            cur.execute(issueSql, (bid,))
            con.commit()
            cur.execute(updateStatus, (bid,))
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return
    except pymysql.Error as e:
        messagebox.showinfo("Error", f"Error: {e}")

    allBid.clear()
    root.destroy()

def returnBook():
    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="slateblue1")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="slateblue2", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg='white', fg='black', font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb1 = Label(labelFrame, text="Book ID : ", bg='white', fg='black')
    lb1.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root, text="Return", bg='white', fg='black', command=returnn)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

if __name__ == "__main__":
    returnBook()






    
