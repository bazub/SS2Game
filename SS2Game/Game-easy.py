'''
Created on Sep 8, 2012

@author: Bogdan
'''
import random
from tkinter import *
from PIL import *

def SScomm(x,y):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for d in range(0,4):
        newx=x+dx[d]
        newy=y+dy[d]
        if(M[newx][newy]==0):
            M[newx][newy]=M[x][y]
            M[x][y]=0
            break
    if(M==done):
        root.quit()
    
    def play():
        x=1
        y=1
        for i in range(0,9):
            command = (lambda p1, p2: lambda: SScomm(p1, p2)) (x, y)
            butSS[i]=Button(root, image=tmp[M[x][y]], text=str(M[x][y]), command=command)
            butSS[i].image=tmp
            '''
            Place the buttons in the Grid
            '''
            butSS[i].grid(row=x-1,column=y-1,sticky=N+S+E+W)
            y=y+1
            if(y==4):
                y=1
                x=x+1
    play()



'''
Shuffle the numbers
'''
easy=[0,1,2,3,4,5,6,7,8]
b=[]
for i in range(0,9):
    a=random.randint(0,8-i)
    b=b+[easy[a]]
    del easy[a]
'''
Create the 3x3 matrix and store the shuffled numbers inside it
'''
k=0
M =[[9]*5]
M.append([9])
M.append([9])
M.append([9])
M.append([9]*5)
done=[[9,9,9,9,9],[9,1,2,3,9],[9,4,5,6,9],[9,7,8,0,9],[9,9,9,9,9]]  
for i in range(0,3):
    for j in range(0,3):
        M[i+1].append(b[k])
        k=k+1
    M[i+1].append(9)
'''
Create the main window
'''
root=Tk()
root.geometry("420x420+400+100")
root.title("Matrix Games                          by Bazub")
root.bind("<Escape>", lambda e: e.widget.quit())
root.resizable(FALSE,FALSE)

'''
Configure the grid (buttons will auto-resize to fill the empty space)
'''
for x in range(3):
    Grid.columnconfigure(root,x,weight=1)
for y in range(3):
    Grid.rowconfigure(root,y,weight=1)
'''
Create Buttons
'''
butSS=[]
x=1
y=1
'''
Initialize images for buttons
'''
tmp=[]
for i in range(0,9):
    tmp.append(0)
    tmp[i] = PhotoImage(file='easy//'+str(i)+'.gif')
for i in range(0,9):
    butSS.append(0)
    command = (lambda p1, p2: lambda: SScomm(p1, p2)) (x, y)
    butSS[i]=Button(root, image=tmp[M[x][y]], text=str(M[x][y]), command=command)
    butSS[i].image=tmp
    '''
    Place the buttons in the Grid
    '''
    butSS[i].grid(row=x-1,column=y-1,sticky=N+S+E+W)
    y=y+1
    if(y==4):
        y=1
        x=x+1

'''
Keep main window open
'''
root.mainloop()


