from tkinter import *
from tkinter import messagebox,filedialog
from email.message import EmailMessage
import smtplib
import os
import imghdr
import pandas
check=False
def browse():
    global emails
    path=filedialog.askopenfilename(initialdir="c:/",title="select the excel file")
    if path=="":
        messagebox.showerror("Error","please select excel file")
    else:
        data=pandas.read_excel(path)
        if "Email" in data.columns:
            emails=list(data['Email'])
            final_email=[]
            for i in emails:
                if pandas.isnull(i)==False:
                    final_email.append(i)
            emails=final_email
            print(emails)
            if len(emails)==0:
                messagebox.showerror("Error","there is no any excel file",parent=root)
            else:
                txt_to.config(state=NORMAL)
                txt_to.insert(0,os.path.basename(path))
                txt_to.config(state="readonly")
                total_.config(text="Total: " + str(len(emails)))
                sent_.config(text="Sent:")
                left_.config(text="Left:")
                failed_.config(text="Failed:")




def browse_btn():
    if choice.get()=='bulk':
        btn_browse.config(state=NORMAL)
        txt_to.config(state="readonly")
    if choice.get()=="single":
        btn_browse.config(state=DISABLED)
        txt_to.config(state=NORMAL)



def  attachment():
    global  filename,filetype,filepath,check
    check=True
    filepath=filedialog.askopenfilename(initialdir="c:/",title="select file")
    filetype=filepath.split(".")
    filetype=filetype[1]
    filename=os.path.basename(filepath)
    message.insert(END,f"\n{filename}\n")



def sendingemail(toadd,sub,body):
    f=open("login.txt","r")
    for i in f:
        logined=i.split(",")
    message_=EmailMessage()
    message_["subject"]=sub
    message_["to"]=toadd
    message_["from"]=logined[0]
    message_.set_content(body)
    if check:
        if filetype=="jpg" or filetype=="png" or filetype=="jpeg":
            f=open(filepath,"rb")
            file_data=f.read()
            subtype=imghdr.what(filepath)
            message_.add_attachment(file_data,maintype="image",subtype=subtype,filename=filename)
        else:
            f = open(filepath, "rb")
            file_data = f.read()
            message_.add_attachment(file_data,maintype="application",subtype='octet-stream',filename=filename)


    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(logined[0],logined[1])
    s.send_message(message_)
    x=s.ehlo()
    if x[0]==250:
        return "sent"
    else:
        return 'failed'






def send_email():
    if txt_to.get()=="" or subjectEntry.get()=="" or message.get(1.0,END)=="\n":
        messagebox.showerror("Error","All fields are required",parent=root)
    else:
        if choice.get()=="single":
            result=sendingemail(txt_to.get(),subjectEntry.get(),message.get(1.0,END))
            if result=="sent":
                messagebox.showinfo("success","email sent successfully")
            if result=="failed":
                messagebox.showerror("Error","email not sent")

        if choice.get()=="bulk":
            sent=0
            failed=0
            for x in emails:
                result=sendingemail(x,subjectEntry.get(),message.get(1.0,END))
                if result=="sent":
                    sent+=1
                if result=='failed':
                    failed+=1
                total_.config(text='total:'+str(len(emails)))
                sent_.config(text="sent:"+str(sent))
                left_.config(text="left:"+str(len(emails)-(sent + failed)))
                failed_.config(text='failed:'+str(failed))

                total_.update()
                sent_.update()
                left_.update()
                failed_.update()
            messagebox.showinfo("success","emails are sent successfully")



def login():
    def clear1():
        userentry.delete(0,END)
        passentry_.delete(0,END)

    def save1():
        if userentry.get()=="" or passentry_.get()=="":
            messagebox.showerror("Error","All fields are required ",parent=root1)
        else:
            f=open("login.txt","w")
            f.write(userentry.get()+","+passentry_.get())
            f.close()
            messagebox.showinfo("Information","username and password saved",parent=root1)


    root1=Toplevel()
    root1.resizable(0,0)
    root1.title("login")
    root1.geometry("700x400+300+200")
    root1.config(bg="white")
    setting_=Label(root1, font=("arial", 40, "bold"), text="LOGIN", bg="#222A35")
    setting_.place(x=0, y=0,relwidth=1)
    des = Label(root1, text="Enter the email address and password from which to send all emails ",
                bg="yellow",fg="#222A35",font=("times new roman", 15, "bold"))
    des.place(x=0, y=77, relwidth=1)
    username_= Label(root1, font=("arial", 22), text="Email Address", bg="white", fg="black")
    username_.place(x=15, y=170)
    password_= Label(root1, font=("arial", 22), text="Password", bg="white", fg="black")
    password_.place(x=15, y=220)
    # entery box........
    userentry= Entry(root1, font=("arial", 10, "bold"), fg="black", bg="lightyellow")
    userentry.place(x=250, y=170, width=380, height=30)
    passentry_ = Entry(root1, font=("arial", 10, "bold"), fg="black", bg="lightyellow", show="*")
    passentry_.place(x=250, y=220, width=380, height=30)
    # button ......................
    btn_save1 = Button(root1, text="SAVE", font=('arial', 12, "bold"), bg="green",fg="black",
                       activebackground="green", cursor="hand2",command=save1)
    btn_save1.place(x=430, y=280)
    btn_clear1= Button(root1, text="CLEAR",  font=('arial', 12, "bold"), bg="red", fg="black",
                        activebackground="red", cursor="hand2",command=clear1)
    btn_clear1.place(x=350, y=280)

    root1.mainloop()

def rexit():
    result=messagebox.askyesno("Notification","Do you want to exit?")
    if result:
        root.destroy()
    else:
        pass

def clear():
    txt_to.delete(0,END)
    subjectEntry.delete(0,END)
    message.delete(1.0,END)

root=Tk()
root.geometry("1000x630+100+20")
root.title("Email sender app")
root.resizable(0, 0)
root.config(bg="white")
# tittle.................
title = Label(root, font=("arial", 40, "bold"), text="Bulk email send ", bg="#222A35")
title.place(x=0, y=0, relwidth=1)
btn_setting = Button(root, text="LOGIN", font=("arial", 22, "bold"), bg="green",cursor="hand2",
                     activebackground="green", fg="yellow", bd=0,command=login)
btn_setting.place(x=800, y=4)
#radio button...........
choice= StringVar()
single = Radiobutton(root, text="single", value="single",variable=choice,
                     font=("times new roman", 25, "bold"),bg='white', fg="black",
                     command=browse_btn).place(x=50, y=90)
bulk = Radiobutton(root, text="Bulk", value="bulk",variable=choice,
                   font=("times new roman", 25, "bold"),bg='white',fg="black",
                   command=browse_btn ).place(x=250, y=90)
choice.set("single")
#body..........................................................
To = Label(root, font=("arial", 22), text="To (Email Address)", fg="black",bg="white").place(x=15, y=170)
subject = Label(root, font=("arial", 22), text="SUBJECT", fg="black",bg="white").place(x=15, y=220)
msg = Label(root, font=("arial", 22), text="MESSAGE", fg="black",bg="white").place(x=15, y=370)
txt_to = Entry(root, font=("arial", 16), fg="black", bg="lightyellow")
txt_to.place(x=300, y=170, width=350, height=30)
subjectEntry = Entry(root, font=("arial", 15), fg="black", bg="lightyellow")
subjectEntry.place(x=300, y=220, width=400, height=30)
message = Text(root, font=("arial", 16), fg="black", bg="lightyellow")
message.place(x=300, y=270, width=600, height=200)

btn_send = Button(root, text="SEND", font=('arial', 12, "bold"), bg="green", fg="black", activebackground="green",
                  cursor="hand2",command=send_email)
btn_send.place(x=700, y=560)
btn_clear= Button(root, text="CLEAR", font=('arial', 12, "bold"), bg="red", fg="black", activebackground="red",
                   cursor="hand2",command=clear).place(x=800, y=560)
btn_exit = Button(root, text="EXIT ", font=('arial', 12, "bold"), bg="red", fg="black", activebackground="red",
                   cursor="hand2",command=rexit).place(x=900, y=560)
btn_browse = Button(root, text="BROWSE", font=('arial', 10, "bold"), bg="green",fg="black", activebackground="green",
                    cursor="hand2",state=DISABLED,command=browse)
btn_browse.place(x=700, y=170)
#mic and attachment..........................................

attachment=Button(root, text="Attachment", font=('arial', 12, "bold"), bg="gray", fg="black", activebackground="#222A35",
                   cursor="hand2",command=attachment).place(x=900, y=270)
total_=Label(root,font=("arial",15,"bold"),bg="white",fg="black")
total_.place(x=15,y=560)
sent_=Label(root,font=("arial",15,"bold"),bg="white",fg="black")
sent_.place(x=250,y=560)
left_=Label(root,font=("arial",15,"bold"),bg="white",fg="black")
left_.place(x=400,y=560)
failed_=Label(root,font=("arial",15,"bold"),bg="white",fg="black")
failed_.place(x=550,y=560)

root.mainloop()