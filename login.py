from tkinter import *



def create_window():
    root = Tk()
    Label(root, text="new window").grid(row=0, column=0)
    login.destroy()



login = Tk()
b = Button(login, text="Create new window", command=create_window).grid(row=0, column=0)


login.mainloop()