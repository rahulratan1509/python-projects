
from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.status_bar = Label(self,textvar=self.var,relief=SUNKEN,anchor="w")
        self.status_bar.pack(side=BOTTOM,fill=X)
    def click(self):
        print("Button Clicked 1")
    def create_button(self,your_text):
        Button(text=your_text,command = self.click()).pack()
        
        
if __name__ == '__main__':
    window = GUI()
    window.status()
    window.create_button("CLICK ME")
    window.mainloop()
    