from tkinter import Label, Entry, Button, Tk
from tkinter.ttk import Treeview
from sqlite3 import connect
from random import choice
import os.path

def sign_in():

    def check():
        try:
            file = open("log.txt","r")
            reader = file.read().split(",")
            if uname.get() == reader[0] and password.get() == reader[1]:
                sign_in_window.destroy()
                main()

            else:
                Tk().bell()

        except:
            print("log.txt was deleted or You didn't sign up")
    sign_in_window = Tk()
    sign_in_window.title("Sign in")
    Label(sign_in_window, text="username : ").grid(row=0, column=0)
    uname = Entry(sign_in_window)
    uname.grid(row=0, column=1)
    Label(sign_in_window, text="password : ").grid(row=1, column=0)
    password = Entry(sign_in_window,show="*")
    password.grid(row=1, column=1)
    Button(sign_in_window, text="              sign in              ", command=check).grid(row=2,column=1)
    sign_in_up_window.destroy()

def sign_up():

    def check():
        if not os.path.exists("log.txt"):
            file = open("log.txt","w")
            file.write(uname.get()+","+password.get())
            sign_up_window.destroy()
            main()
        else:
            sign_up_window.destroy()
            sign_window()

    sign_up_window = Tk()
    sign_up_window.title("Sign up")
    Label(sign_up_window, text="username : ").grid(row=0, column=0)
    uname = Entry(sign_up_window)
    uname.grid(row=0, column=1)
    Label(sign_up_window, text="password : ").grid(row=1, column=0)
    password = Entry(sign_up_window,show="*")
    password.grid(row=1, column=1)
    Button(sign_up_window, text="             sign up             ", command=check).grid(row=2, column=1)
    sign_in_up_window.destroy()

def main():
    def save():
        conn = connect('my_db.db')
        c = conn.cursor()
        c.execute("INSERT INTO PassList VALUES ('{}','{}')".format(website_entry.get(), password_entry.get()))
        conn.commit()
        website_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        conn.close()
        show()

    def search():
        for i in tv.get_children():
            tv.delete(i)
        conn = connect("my_db.db")
        c = conn.cursor()
        c.execute("SELECT * FROM PassList WHERE website = '{}'".format(show_entry.get()))
        for row in c.fetchall():
            tv.insert("", "end", values=row)
        show_entry.delete(0, 'end')

    def update():
        conn = connect("my_db.db")
        c = conn.cursor()
        c.execute("UPDATE PassList SET password = '{}' WHERE website = '{}'".format(update_password_entry.get(),
                                                                                    update_website_entry.get()))
        conn.commit()
        update_website_entry.delete(0, 'end')
        update_password_entry.delete(0, 'end')
        conn.close()
        show()

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

    def generate():
        pass_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '@', '#', '-', '_']
        ran_pass = ''
        for i in range(13):
            ran_pass += choice(pass_lst)

        random_pass.delete(0, 'end')
        random_pass.insert(0, ran_pass)

    root = Tk()
    root.geometry("403x492")
    root.title("Password Saver")
    Label(root, text="Cool Password Saver", font=('', 18)).grid(row=0, column=0)

    cols = ["Website", "Password"]
    tv = Treeview(root, columns=cols, show="headings")
    for col in cols:
        tv.heading(col, text=col)
    tv.grid(row=2, column=0, columnspan=2)

    Label(root, text="Website : ").grid(row=3, column=0)
    website_entry = Entry(root)
    website_entry.grid(row=3, column=1)

    Label(root, text="Password : ").grid(row=4, column=0)
    password_entry = Entry(root, show="*")
    password_entry.grid(row=4, column=1)

    Button(root, text="               Save               ", command=save).grid(row=5, column=1)

    Label(root, text="Website : ").grid(row=6, column=0)
    show_entry = Entry(root)
    show_entry.grid(row=6, column=1)

    Button(root, text="              Show              ", command=search).grid(row=7, column=1)

    Label(root, text="Website  : ").grid(row=8, column=0)
    update_website_entry = Entry(root)
    update_website_entry.grid(row=8, column=1)

    Label(root, text="Password  : ").grid(row=9, column=0)
    update_password_entry = Entry(root, show="*")
    update_password_entry.grid(row=9, column=1)

    Button(root, text="             Update             ", command=update).grid(row=10, column=1)

    Label(root, text="Random Password : ").grid(row=11, column=0)
    random_pass = Entry(root)
    random_pass.grid(row=11, column=1)

    Button(root, text='            Generate            ', command=generate).grid(row=12, column=1)

    show()
    root.mainloop()

def sign_window():
    global sign_in_up_window
    sign_in_up_window = Tk()
    sign_in_up_window.title("Login")
    Label(sign_in_up_window).grid(row=0, column=0)
    Label(sign_in_up_window).grid(row=0, column=1)
    Button(sign_in_up_window, text="       Sing up       ",command=sign_up).grid(row=1, column=0)
    Button(sign_in_up_window, text="       Sing in       ",command=sign_in).grid(row=1, column=1)
    Label(sign_in_up_window).grid(row=2, column=0)
    Label(sign_in_up_window).grid(row=2, column=1)
    sign_in_up_window.mainloop()
sign_window()
