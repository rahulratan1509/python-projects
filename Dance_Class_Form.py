from tkinter import *
import csv
root = Tk()
root.geometry("600x300")
root.title("DANCE CLASS")




Name = StringVar()
Age  = IntVar()
Gender = StringVar()
Phone = StringVar()

Name_LAbel = Label(root,text="NAME")
Age_Label = Label(root,text="Age")
Gender_Label =Label(root,text="Gender")
Phone_Label = Label(root,text="Phone Number")

Name_entry = Entry(root,textvariable=Name)
Age_entry =Entry(root,textvariable=Age)
Gender_entry = Entry(root,textvariable=Gender)
Phone_entry = Entry(root,textvariable=Phone)

Name_LAbel.grid()
Age_Label.grid()
Gender_Label.grid()
Phone_Label.grid()

Name_entry.grid(row=0,column=1,padx=5)
Age_entry.grid(row=1,column=1,padx=5)
Gender_entry.grid(row=2,column=1,padx=5)
Phone_entry.grid(row=3,column=1,padx=5)

def get_info():
    f = open('Dance_data__1.csv','a',newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow([Name_entry.get()," "+Age_entry.get()+" "," "+Gender_entry.get()+" "," "+Phone_entry.get()])
    f.close()

Button = Button(text="Submit",command=get_info)
Button.grid()



root.mainloop()