from tkinter import *
def getvar(r,y):
    global player
    if player=='X' and s[r][y]==0 and stop_game==False:
        b[r][y].config()
root=Tk()
root.title("tic toe game")
root.geometry("460x470+440+120")
root.resizable(False,False)
b=[[0,0,0],[0,0,0],[0,0,0]]
s=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j]=Button(font=("arial",60),width=3,bg="powder blue", command=lambda r=i,y=j: getvar(r,y))
        b[i][j].grid(row=i,column=j)
player='X'
stop_game=False
mainloop()
