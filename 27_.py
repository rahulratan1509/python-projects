from tkinter import *
root = Tk()

root.geometry("655x444")
root.title("HOW to ADD Custom Icon - Title ")
root.wm_iconbitmap("icon-2.ico")

root.configure(background="grey")

width = root.winfo_screenmmwidth()
height = root.winfo_screenmmheight()

print(f" {width} x {height}")

root.mainloop()