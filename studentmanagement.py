from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
def add_details():
    if rollvar.get()=="" or namevar.get()=="":
        messagebox.showerror("Error","enroll and name must be required",parent=root)
    else:
        con=pymysql.connect(host='localhost',port=3307,user='root',password='',database='studentmanagement')
        cur=con.cursor()
        cur.execute("insert into student values (%s ,%s, %s, %s, %s, %s, %s)",(rollvar.get(),namevar.get(),
                        emailvar.get(),gendervar.get(),contactvar.get(),dobvar.get(),txt_add.get(1.0,END)))
        con.commit()
        con.close()
        fetch_data()
        clearall()
        messagebox.showinfo("Success","your record has been successfully saved")

def fetch_data():
    con = pymysql.connect(host='localhost', port=3307, user='root', password='', database='studentmanagement')
    cur = con.cursor()
    cur.execute("select * from student")
    rows=cur.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert("",END,values=row)
        con.commit()
    con.close()


def clearall():
    txt_roll.delete(0,END)
    txt_name.delete(0,END)
    txt_email.delete(0,END)
    combo_gender.set("")
    txt_contact.delete(0,END)
    txt_dob.delete(0,END)
    txt_add.delete(1.0,END)

def cursor_get(ev):
    cursor_row=student_table.focus()
    contents=student_table.item(cursor_row)
    row=contents['values']
    rollvar.set(row[0])
    namevar.set(row[1])
    emailvar.set(row[2])
    gendervar.set(row[3])
    contactvar.set(row[4])
    dobvar.set(row[5])
    txt_add.delete(1.0,END)
    txt_add.insert(END,row[6])

def update_data():
    con = pymysql.connect(host='localhost', port=3307, user='root', password='', database='studentmanagement')
    cur = con.cursor()
    cur.execute("update student set Name=%s,Email=%s,%Gender=%s,Contact=%s,DOB=%S,Address=%s where Enroll=%s",(
            namevar.get(),emailvar.get(),gendervar.get(),
            contactvar.get(),dobvar.get(),txt_add.get(1.0,END),rollvar.get())
            )

    con.commit()
    con.close()
    fetch_data()
    clearall()
    messagebox.showinfo("Success", "your record has been successfully updated")
def delete_data():
    con = pymysql.connect(host='localhost', port=3307, user='root', password='', database='studentmanagement')
    cur = con.cursor()
    cur.execute("delete from student where Enroll=%s",rollvar.get())
    con.commit()
    con.close()
    fetch_data()
    clearall()

def search_data():
    con = pymysql.connect(host='localhost', port=3307, user='root', password='', database='studentmanagement')
    cur = con.cursor()
    cur.execute("select * from student where"+ str(searchbyvar.get())+"LIKE '%"+str(searchtxtvar.get())+"%'")
    rows=cur.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert("",END,values=row)
        con.commit()
    con.close()

root=Tk()
root.title("school management system")
root.geometry("1378x700+0+0")
root.config(bg="white")
title=Label(root,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bd=9,relief=GROOVE,bg="green",fg="yellow")
title.pack(side=TOP,fill=X)
#frame.............................................
manageframe=Frame(root,bg="red",bd=4,relief=RIDGE)
manageframe.place(x=20,y=90,width=450,height=585)
#All variables..................................................................................
rollvar = StringVar()
namevar = StringVar()
emailvar = StringVar()
gendervar = StringVar()
contactvar = StringVar()
searchbyvar = StringVar()
searchtxtvar = StringVar()
dobvar=StringVar()

#input system......................................................................................
m_title=Label(manageframe,text="Student Details",font=("times new roman",40,"bold"),bg="yellow",fg="black",relief=GROOVE)
m_title.grid(row=0,columnspan=2,pady=20,padx=30)
roll=Label(manageframe,text="ENROLL",font=("times new roman",20,"bold"),bg="red",fg="white")
roll.grid(row=1,column=0,padx=20,pady=10,sticky="w")
txt_roll=Entry(manageframe,textvariable=rollvar,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_roll.grid(row=1,column=1,padx=20,pady=10,sticky="w")

name=Label(manageframe,text="Name",font=("times new roman",20,"bold"),bg="red",fg="white")
name.grid(row=2,column=0,padx=20,pady=10,sticky="w")
txt_name=Entry(manageframe,textvariable=namevar,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_name.grid(row=2,column=1,padx=20,pady=10,sticky="w")

email=Label(manageframe,text="Email",font=("times new roman",20,"bold"),bg="red",fg="white")
email.grid(row=3,column=0,padx=20,pady=10,sticky="w")
txt_email=Entry(manageframe,textvariable=emailvar,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_email.grid(row=3,column=1,padx=20,pady=10,sticky="w")

gender=Label(manageframe,text="Gender",font=("times new roman",20,"bold"),bg="red",fg="white")
gender.grid(row=4,column=0,padx=20,pady=10,sticky="w")
combo_gender=ttk.Combobox(manageframe,textvariable=gendervar,font=("atimes new roman",13,"bold"),state="readonly")
combo_gender["values"]=("Male","Female","Others")
combo_gender.grid(row=4,column=1,padx=20,pady=10)

contact=Label(manageframe,text="Contact",font=("times new roman",20,"bold"),bg="red",fg="white")
contact.grid(row=5,column=0,padx=20,pady=10,sticky="w")
txt_contact=Entry(manageframe,textvariable=contactvar,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_contact.grid(row=5,column=1,padx=20,pady=10,sticky="w")

dob=Label(manageframe,text="DOB",font=("times new roman",20,"bold"),bg="red",fg="white")
dob.grid(row=6,column=0,padx=20,pady=10,sticky="w")
txt_dob=Entry(manageframe,textvariable=dobvar,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
txt_dob.grid(row=6,column=1,padx=20,pady=10,sticky="w")

add=Label(manageframe,text="Address",font=("times new roman",20,"bold"),bg="red",fg="white")
add.grid(row=7,column=0,padx=20,pady=10,sticky="w")
txt_add=Text(manageframe,font=("times new roman",10,"bold"),bd=5,relief=GROOVE,width=30,height=3)
txt_add.grid(row=7,column=1,padx=20,pady=10,sticky="w")
#btn frame.........................................................................
btnframe=Frame(manageframe,bd=3,relief=RIDGE,bg="black")
btnframe.place(x=14,y=525,width=428)

add=Button(btnframe,text="ADD",width=10,command=add_details).grid(row=0,column=0,pady=10,padx=10)
update=Button(btnframe,text="UPDATE",width=10,command=update_data).grid(row=0,column=1,pady=10,padx=10)
delete=Button(btnframe,text="DELETE",width=10,command=delete_data).grid(row=0,column=2,pady=10,padx=10)
clear=Button(btnframe,text="CLEAR",width=10,command=clearall).grid(row=0,column=3,pady=10,padx=10)
#details frames.......................................................................
detailsframe=Frame(root,bg="red",bd=4,relief=RIDGE)
detailsframe.place(x=500,y=90,width=880,height=585)

search=Label(detailsframe,text="Search by",font=("times new roman",20,"bold"),bg="red",fg="white",relief=GROOVE,bd=0)
search.grid(row=0,column=0,pady=10,padx=30)
combo_search=ttk.Combobox(detailsframe,textvariable=searchbyvar,font=("atimes new roman",13,"bold"),width=10,state="readonly")
combo_search["values"]=("Enroll","Name","Contact")
combo_search.grid(row=0,column=1,padx=20,pady=10)
txt_search=Entry(detailsframe,textvariable=searchtxtvar,font=("times new roman",10,"bold"),bd=5,width=20,relief=GROOVE)
txt_search.grid(row=0,column=2,padx=20,pady=10,sticky="w")
search_btn=Button(detailsframe,text="Search",width=10,pady=5 ,command=search_data).grid(row=0,column=3,pady=10,padx=10)
show_btn=Button(detailsframe,text="Show All",width=10,pady=5,command=fetch_data).grid(row=0,column=4,pady=10,padx=10)
#................................table frames..........................................
tableframe=Frame(detailsframe,bg="#222A35",bd=4,relief=RIDGE)
tableframe.place(x=10,y=60,width=760,height=490)

scroll_x=Scrollbar(tableframe,orient=HORIZONTAL)
scroll_y=Scrollbar(tableframe,orient=VERTICAL)

student_table=ttk.Treeview(tableframe,column=("Enroll","Name","Email","Gender","Contact","DOB","Address"),
                           xscrollcommand=scroll_y,yscrollcommand=scroll_x)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

student_table.heading("Enroll",text="Enroll")
student_table.heading("Name",text="Name")
student_table.heading("Email",text="Email")
student_table.heading("Gender",text="Gender")
student_table.heading("Contact",text="Contact")
student_table.heading("DOB",text="DOB")
student_table.heading("Address",text="Address")
student_table["show"]="headings"
student_table.column("Enroll",width=100)
student_table.column("Name",width=100)
student_table.column("Email",width=100)
student_table.column("Gender",width=100)
student_table.column("Contact",width=100)
student_table.column("DOB",width=100)
student_table.column("Address",width=150)
student_table.pack(fill=BOTH,expand=1)
student_table.bind("<ButtonRelease-1>",cursor_get)
fetch_data()

root.mainloop()