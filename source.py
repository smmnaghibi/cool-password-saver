from tkinter import Label, Entry, Button, Tk
from tkinter.ttk import Treeview
from sqlite3 import connect

def save():
    ...

def search():
    for i in tv.get_children():
        tv.delete(i)
    conn = connect("my_db.db")
    c = conn.cursor()
    c.execute("SELECT * FROM PassList WHERE name = '{}'".format(show_entry.get()))
    for row in c.fetchall():
        tv.insert("", "end", values=row)

def update():
    ...

def show():
    for i in tv.get_children():
        tv.delete(i)
    conn = connect("my_db.db")
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM PassList")
    except:
        c.execute("CREATE TABLE PassList (website text, password test)")
        conn.commit()
        c.execute("SELECT * FROM PassList")

    for row in c.fetchall():
        tv.insert("", "end", values=row)

    conn.close()

root = Tk()
root.geometry("370x450")
root.title("Password Saver")
Label(root, text="Cool Password Saver", font=('',18)).grid(row=0, column=0)

cols = ["Website"]
tv = Treeview(root, columns=cols, show="headings")
for col in cols:
    tv.heading(col, text=col)
tv.grid(row=2, column=0, columnspan=1)

Label(root, text="Website : ").grid(row=3, column=0)
website_entry = Entry(root)
website_entry.grid(row=3, column=1)

Label(root, text="Password : ").grid(row=4,column=0)
password_entry = Entry(root)
password_entry.grid(row=4, column=1)

Button(root, text="               Save               " , command=save).grid(row=5, column=1)

Label(root, text="Website : ").grid(row=6, column=0)
show_entry = Entry(root)
show_entry.grid(row=6, column=1)

Button(root, text="              Show              ", command=search).grid(row=7, column=1)

Label(root, text="Website  : ").grid(row=8, column=0)
update_website_entry = Entry(root)
update_website_entry.grid(row=8, column=1)

Label(root, text="Password  : ").grid(row=9, column=0)
update_password_entry = Entry(root)
update_password_entry.grid(row=9, column=1)

Button(root, text="             Update             ", command=update).grid(row=10, column=1)


show()
root.mainloop()