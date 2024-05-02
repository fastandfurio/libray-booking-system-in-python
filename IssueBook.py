from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "PASS@123"
mydatabase = "hi"

try:
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    print("Connection successful!")
except pymysql.Error as e:
    print("Error:", e)


# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books"
    
#List To store all Book IDs
allBid = [] 

# def issue():
#     global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status
    
#     bid = inf1.get()
#     issueto = inf2.get()

#     issueBtn.destroy()
#     labelFrame.destroy()
#     lb1.destroy()
#     inf1.destroy()
#     inf2.destroy()

#     extractBid = "select bid from " + bookTable
#     try:
#         cur.execute(extractBid)
#         con.commit()
#         allBid.clear()  # Clear allBid list before repopulating
#         for i in cur:
#             allBid.append(i[0])

#         if bid in allBid:
#             checkAvail = "select status from " + bookTable + " where bid = '" + bid + "'"
#             cur.execute(checkAvail)
#             con.commit()
#             for i in cur:
#                 check = i[0]

#             if check == 'avail':
#                 status = True
#             else:
#                 status = False
#                 messagebox.showinfo("Message", "Book Already Issued")  # Moved here to display message
#                 root.destroy()
#                 return  # Return to stop further execution

#         else:
#             messagebox.showinfo("Error", "Book ID not present")
#             root.destroy()
#             return  # Return to stop further execution
            
#     except pymysql.Error as e:
#         messagebox.showinfo("Error", f"Error: {e}")
#         root.destroy()
#         return  # Return to stop further execution

#     issueSql = "insert into " + issueTable + " values ('" + bid + "','" + issueto + "')"
#     updateStatus = "update " + bookTable + " set status = 'issued' where bid = '" + bid + "'"
#     try:
#         if status:
#             cur.execute(issueSql)
#             cur.execute(updateStatus)
#             con.commit()
#             messagebox.showinfo('Success', "Book Issued Successfully")
#         else:
#             messagebox.showinfo("Message", "Book Already Issued")
#     except pymysql.Error as e:
#         messagebox.showinfo("Error", f"Error: {e}")

#     allBid.clear()

def issueBook(): 
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="slateblue2")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="slateblue1", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='white', fg='black', font=('Courier', 15,'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='white')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb1 = Label(labelFrame, text="Book ID : ", bg='white', fg='black')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    lb2 = Label(labelFrame, text="Issued To : ", bg='white', fg='black')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    issueBtn = Button(root, text="Issue", bg='white', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1
    
    bid = inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractBid = "SELECT status FROM " + bookTable + " WHERE bid = %s"
    try:
        cur.execute(extractBid, (bid,))
        con.commit()
        row = cur.fetchone()  # Fetch the first row
        if row:
            status = row[0]
            if status == 'Available':
                issueSql = "INSERT INTO " + issueTable + " VALUES (%s, %s)"
                updateStatus = "UPDATE " + bookTable + " SET status = 'Issued' WHERE bid = %s"
                try:
                    cur.execute(issueSql, (bid, issueto))
                    cur.execute(updateStatus, (bid,))
                    con.commit()
                    messagebox.showinfo('Success', "Book Issued Successfully")
                except pymysql.Error as e:
                    messagebox.showinfo("Error", f"Error: {e}")
            else:
                messagebox.showinfo("Message", "Book Already Issued")
        else:
            messagebox.showinfo("Error", "Book ID not present")
            
    except pymysql.Error as e:
        messagebox.showinfo("Error", f"Error: {e}")

    root.destroy()

