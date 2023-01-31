from tkinter import *
import calendar
root=Tk()
root.title("CALENDAR")
root.geometry("260x260+450+250")
root.resizable(0,0)

def show():
    a=int(spin1.get())
    b=int(spin2.get())
    cal=calendar.month(b,a)
    txt.delete(0.0,END)
    txt.insert(INSERT,cal)
lbl1=Label(root,text="MONTH",font=("arial,12,bold")).place(x=15,y=0)
lbl2=Label(root,text="YEAR",font=("arial,12,bold")).place(x=150,y=0)
spin1=Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
spin1.place(x=85,y=2)
spin2=Spinbox(root,from_=1999,to=2100,width=4)
spin2.place(x=200,y=2)
btn=Button(root,text="Show",font=("arial,12,bold"),command=show).place(x=100,y=30)
txt=Text(root,width=25,height=10).place(x=20,y=60)

root.mainloop()