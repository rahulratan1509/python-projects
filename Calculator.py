from tkinter import *

root = Tk()
root.title("Calculator")

root.geometry("500x700")
root.configure(bg="black")
root.wm_iconbitmap("icon-2.ico")

def click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        if screen_value.get().isdigit():
            value = int(screen_value.get())
        else:
            try:
                value = eval(screen_value.get()) # eval function is used to calculate the expression from string
            except:
                screen_value.set("Error")
                screen.update()
        screen_value.set(value)
        screen.update()
        
    elif text == "C":
        screen_value.set("")
        screen.update()
        pass
    else:
        screen_value.set(screen_value.get() + text)
        screen.update()
    

screen_value = StringVar()
screen_value.set("")

screen = Entry(root,textvar=screen_value,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

frame_1 = Frame(root,bg="black")

button= Button(frame_1,text="9",padx=25,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT ,padx=18,pady=4)
button= Button(frame_1,text="8",padx=25,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=4)
button = Button(frame_1,text="7",padx=25,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=4)

frame_1.pack()
frame_1 = Frame(root,bg="black")

button= Button(frame_1,text="6",padx=25,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT ,padx=18,pady=4)
button= Button(frame_1,text="5",padx=25,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=4)
button = Button(frame_1,text="4",padx=25,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=4)

frame_1.pack()

frame_1 = Frame(root,bg="black")

button= Button(frame_1,text="3",padx=25,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT ,padx=18,pady=4)
button= Button(frame_1,text="2",padx=25,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=4)
button = Button(frame_1,text="1",padx=25,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=4)

frame_1.pack()
frame_1 = Frame(root,bg="black")

button= Button(frame_1,text="0",padx=25,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT ,padx=18,pady=4)
button= Button(frame_1,text="+",padx=25,font="lucida 35 bold",bg="yellow")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=4)
button = Button(frame_1,text="-",padx=25,font="lucida 35 bold",bg="yellow")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=18,pady=4)

frame_1.pack()
frame_1 = Frame(root,bg="black")

button= Button(frame_1,text="C",padx=25,font="lucida 35 bold",bg="red")
button.bind("<Button-1>",click)
button.pack(side=LEFT ,padx=19,pady=4)
button= Button(frame_1,text="/",padx=25,font="lucida 35 bold",bg="yellow")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=19,pady= 4)
button = Button(frame_1,text="*",padx=25,font="lucida 35 bold",bg="yellow")
button.bind("<Button-1>",click)
button.pack(side=LEFT,padx=19,pady=4)

frame_1.pack()
frame_1 = Frame(root,bg="black")

button= Button(frame_1,text="=",padx=180,font="lucida 35 bold")
button.bind("<Button-1>",click)
button.pack(side=LEFT ,padx=20,pady=10)


frame_1.pack()


    
root.mainloop()