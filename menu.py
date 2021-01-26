# tutorial 17
from tkinter import *
root = Tk()
root.geometry("644x344")
root.title("Program")


def myfunc():
    print("you clicked on file")
#without drop Down
my_menu = Menu(root)
my_menu.add_command(label="File",command=myfunc)
my_menu.add_command(label="Edit",command=myfunc)
my_menu.add_command(label="Find",command=myfunc)
my_menu.add_command(label="Exit",command=quit)

root.config(menu=my_menu)

root.mainloop()
