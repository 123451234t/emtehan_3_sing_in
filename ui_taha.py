from tkinter import *
from tkinter import messagebox
import database
root = Tk()
root.geometry("500x400")
root.config(bg="aqua")

# =======================func
database.craet()
    
def in_():
    if ent_email.get()=='' or ent_password.get()=='':
        messagebox.showerror('Entry error','password or email empty!')
        
    else:
        database.signup(ent_fname.get(),ent_lname.get(),ent_email.get(),ent_password.get())
        messagebox.showinfo('login','Login was euccessful')
    

def up():
    d=database.signin(ent_fname.get(),ent_lname.get(),ent_email.get(),ent_password.get())
    if d:
        messagebox.showinfo('login  info','welcom')
        
    else:
        messagebox.showerror('login error','you have not sing up')
    





# ============================wedget
lbl_fname = Label(root,text="fname:",font="arial 15 bold",bg="red").place(x=40,y=20)
lbl_lname = Label(root,text="lname:",font="arial 15 bold",bg="red").place(x=40,y=70)
lbl_email = Label(root,text="* email:",font="arial 15 bold",bg="red").place(x=40,y=170)
lbl_pas = Label(root,text="* password:",font="arial 15 bold",bg="red").place(x=40,y=220)

ent_fname = Entry(root,font="arial 15 bold")
ent_fname.place(x=180,y=20)
ent_lname = Entry(root,font="arial 15 bold")
ent_lname.place(x=180,y=70)
ent_email = Entry(root,font="arial 15 bold")
ent_email.place(x=180,y=170)
ent_password = Entry(root,font="arial 15 bold",show="*")
ent_password.place(x=180,y=220)

btn_up = Button(root,text="sing up",font="arial 15 bold",bg="red",command=in_).place(x=100,y=320)
btn_in = Button(root,text="sing in",font="arial 15 bold",bg="red",command=up).place(x=300,y=320)











root.mainloop()