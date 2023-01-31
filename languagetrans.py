from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
def change(text="type", src="english", dest="hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text=text1,src=src1,dest=dest1)
    return trans1
def data():
    s = combo1.get()
    d = combo2.get()
    msg = source_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root=Tk()
root.geometry("500x700+420+0")
root.resizable(0,0)
root.title("google translate")
root.config(bg="#222A35")
lbl=Label(root,text="TRANSLATOR",font=("arial",40,"bold"),bg="#222A35",fg="white")
lbl.place(x=60,y=30,height=50,width=400)
frame=Frame(root).pack(side=BOTTOM)
lbl1=Label(root,text="Source Text",font=("arial",20,"bold"),bg="#222A35",fg="white")
lbl1.place(x=60,y=80,height=50,width=400)
source_txt=Text(frame,font=("arial",20),wrap=WORD)
source_txt.place(x=10,y=120,height=200,width=470)
list_txt=list(LANGUAGES.values())
combo1=ttk.Combobox(frame,value=list_txt,state="readonly")
combo1.place(x=5,y=340,height=40,width=150)
combo1.set("english")
button_change=Button(frame,text="Translate",font="bold",relief=GROOVE,bg="green",fg="yellow",
                     activebackground="green",command=data)
button_change.place(x=170,y=340,height=40,width=150)
combo2=ttk.Combobox(frame,value=list_txt,state="readonly")
combo2.place(x=340,y=340,height=40,width=150)
combo2.set("hindi")
#>>>>>>>>>>>>>>>destination test>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
lbl2=Label(root,text="Destination Text",font=("arial",20,"bold"),bg="#222A35",fg="white")
lbl2.place(x=60,y=390,height=50,width=400)
dest_txt=Text(frame,font=("arial",20),wrap=WORD)
dest_txt.place(x=10,y=450,height=200,width=470)
root.mainloop()