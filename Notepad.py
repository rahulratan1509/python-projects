from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

if __name__ == '__main__':
    
    root = Tk()
    root.title("Untitled - Notepad")
    
    root.wm_iconbitmap("icon-2.ico")
    root.geometry("644x500")
    
    # defining functions
    
    
    def new_file():
        global file
        root.title("Untitled - Notepad")
        file = None
        Text_area.delete(1.0,END) ## 1.0 is first character to end character has to be delete
        
        
        
        pass
    
    def open_file():
        global file
        file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.*")])
        
        if file =="":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            Text_area.delete(1.0,END)
            
            f = open(file, 'r')
            Text_area.insert(1.0,f.read())
            f.close()
            
                               
                               
                               
    
    
    def save_file():
        global file
        if file == None:
            file = asksaveasfilename(initialfile="Untitled.txt",
                                     defaultextension=".txt",
                                     filetypes=[("All files","*.*"),
                                                ("Text Documents","*.txt")])
            if file == "":
                file = None
            else:
                #save as a new file
                f = open(file,"w")
                f.write(Text_area.get(1.0,END))
                f.close()
                root.title(os.path.basename(file) + " - Notepad")
        else:
            f = open(file,"w")
            f.write(Text_area.get(1.0,END))
            f.close()
            
            
        
    
    def quit_app():
        root.destroy()
        pass
    
    def cut_func():
        Text_area.event_generate(("<<Cut>>")) ###these functions are new
        pass
    
    def copy_func():
        Text_area.event_generate(("<<Copy>>"))
        
        pass
    
    def paste_func():
        Text_area.event_generate(("<<Paste>>"))
        pass
    
    def help_func():
        pass
    
    def about_func():
        showinfo("NotePad","By rahul")
        
    
    Text_area = Text(root,font="lucida 13")
    file = None #for saving files and opening file
    Text_area.pack(fill="both",expand=True)
    
    
    #adding scroll bar
    
    Scroll_Bar =Scrollbar(Text_area)
    Scroll_Bar.pack(side="right", fill=Y)
    Scroll_Bar.config(command=Text_area.yview)
    Text_area.config(yscrollcommand=Scroll_Bar.set)
    
    
    #creating menu bar
    Menu_bar = Menu(root)
    File_Menu = Menu(Menu_bar, tearoff =0)
    
    
    File_Menu.add_command(label="New",command=new_file)
    
    File_Menu.add_command(label="Open",command=open_file)
    
    File_Menu.add_command(label="Save",command=save_file)
    
    File_Menu.add_separator()
    
    File_Menu.add_command(label="Exit",command=quit_app)
    
    
    Menu_bar.add_cascade(label="File", menu = File_Menu)
    
    
    
    Edit_Menu = Menu(Menu_bar, tearoff =0)
    
    Edit_Menu.add_command(label="Cut",command=cut_func)
    
    Edit_Menu.add_command(label="Copy",command=copy_func)
    
    Edit_Menu.add_command(label="Paste",command=paste_func)
    
    
    Menu_bar.add_cascade(label="Edit",menu=Edit_Menu)
    
    
    
    Help_Menu = Menu(Menu_bar, tearoff =0)
    
    Help_Menu.add_command(label="About US",command=about_func)
    
    Menu_bar.add_cascade(label="Help",menu=Help_Menu)
    
    
    
    root.config(menu=Menu_bar)
    
    
    
    
    root.mainloop()