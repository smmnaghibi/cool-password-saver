from tkinter import *

# def create_window():
#     root = Tk()
#     Label(root, text="new window").grid(row=0, column=0)
#     login.destroy()
#
# login = Tk()
# Button(login, text="Create new window", command=create_window).grid(row=0, column=0)
def sign_in():
    ...

def sign_up():
    ...

sign_in_up_window = Tk()
sign_in_up_window.title("Login")
Label(sign_in_up_window).grid(row=0, column=0)
Label(sign_in_up_window).grid(row=0, column=1)
Button(sign_in_up_window, text="       Sing up       ",command=sign_up).grid(row=1, column=0)
Button(sign_in_up_window, text="       Sing in       ",command=sign_in).grid(row=1, column=1)
Label(sign_in_up_window).grid(row=2, column=0)
Label(sign_in_up_window).grid(row=2, column=1)















sign_in_up_window.mainloop()