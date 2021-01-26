from tkinter import * 
root = Tk()
root.title("My WINDOW")
root.geometry("1110x850")
root.minsize(1120, 820)
root.maxsize(1120, 820)
root.configure(bg="blue")

# Heading
H = Label(text="GAYA  NEWS", font="Elephant 30 bold", bg="black", fg="white", borderwidth=3, padx=5, pady=5, relief=SUNKEN)
H.pack(fill=X)
# date
D = Label(text="Date:-07.06.2020", bg="black", fg="white", borderwidth=3, padx=5, pady=5, relief=SUNKEN)
D.place(x=1000, y=70)
#SEMI HEADING
H2 = Label(text="TODAYS HEADLINES",font="Elephant 20 bold",fg="red")
H2.place(x=400,y=70)

Text1 = Label(text='''Colloquially, the terms meme and Internet meme may refer to pieces of media that are designed in the format of true Internet memes, but which are not themselves
	             intended to spread or evolve, and which have recently become umbrella terms referring to any piece of quickly-consumed comedic or relatable content. What is LIFE)
	             YUP EVERYTHING IS FUCKED up fuck Society''',bg='blue',padx =5,pady =5)
Text1.place(x=20,y=210)

Text2 = Label(text='''Colloquially, the terms meme and Internet meme may refer to pieces of media that are designed in the format of true Internet memes, but which are not themselves
	             intended to spread or evolve, and which have recently become umbrella terms referring to any piece of quickly-consumed comedic or relatable content. What is LIFE)
	             YUP EVERYTHING IS FUCKED up fuck Society''',bg='blue',padx =5,pady =5)
Text2.place(x=20,y=410)

Text3 = Label(text='''Colloquially, the terms meme and Internet meme may refer to pieces of media that are designed in the format of true Internet memes, but which are not themselves
	             intended to spread or evolve, and which have recently become umbrella terms referring to any piece of quickly-consumed comedic or relatable content. What is LIFE)
	             YUP EVERYTHING IS FUCKED up fuck Society''',bg='blue',padx =5,pady =5)
Text3.place(x=20,y=610)
Text4 = Label(text='''Colloquially, the terms meme and Internet meme may refer to pieces of media that are designed in the format of true Internet memes, but which are not themselves
	             intended to spread or evolve, and which have recently become umbrella terms referring to any piece of quickly-consumed comedic or relatable content. What is LIFE)
	             YUP EVERYTHING IS FUCKED up fuck Society''',bg='blue',padx =5,pady =5)
Text4.place(x=20,y=710)

pic1 = PhotoImage(file="1.png")
p1 = Label(image=pic1)

pic2 = PhotoImage(file="2.png")
p2 = Label(image=pic2)

pic3 = PhotoImage(file="3.png")
p3 = Label(image=pic3)

p1.place(x=110,y=265)
p2.place(x=500,y=265)
p3.place(x=850,y=265)
pic4 = PhotoImage(file="3.png")
p4 = Label(image=pic4)
p4.place(x=510,y=470)





root.mainloop()
