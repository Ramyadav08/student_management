from tkinter import *
def callback(r,y):
    global player
    if player == "X" and status == 0 and stop_game == False:
        b[r][y].configure(text="X", fg="blue", bg="black")
        status[r][y] = "X"
        player = "O"
    if player == "O" and status == 0 and stop_game == False:
        b[r][y].configure(text="O",fg="orange",bg="#222A35")
        status[r][y] = "O"
        player = "X"
    check_winner()
def check_winner():
    global stop_game
    for i in range(3):
        if status[i][0]==status[i][1]==status[i][j]!=0:
            b[i][0].configure(bg="gray")
            b[i][1].configure(bg="gray")
            b[i][2].configure(bg="gray")
            stop_game=True
            if status[0][i] == status[1][i] == status[2][i] != 0:
                b[0][i].configure(bg="gray")
                b[1][i].configure(bg="gray")
                b[2][i].configure(bg="gray")
                stop_game = True
            if status[0][0] == status[1][1] == status[2][2] != 0:
                b[0][0].configure(bg="gray")
                b[1][1].configure(bg="gray")
                b[2][2].configure(bg="gray")
                stop_game = True
            if status[0][2] == status[1][1] == status[2][0] != 0:
                b[0][2].configure(bg="gray")
                b[1][1].configure(bg="gray")
                b[2][0].configure(bg="gray")
                stop_game = True




root = Tk()
root.title("TIC TOE GAME")
root.geometry("450x450+300+160")
root.resizable(False,False)

b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
status= [[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j]=Button(root,font=("arial",60),width=3,bg="powder blue", command=lambda r=i,y=j:callback(r,y))
        b[i][j].grid(row=i,column=j)
player="X"
stop_game=False

mainloop()