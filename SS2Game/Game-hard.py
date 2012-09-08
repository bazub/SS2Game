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
    ok=0
    for d in range(0,4):
        newx=x+dx[d]
        newy=y+dy[d]
        if(M[newx][newy]==0):
            M[newx][newy]=M[x][y]
            M[x][y]=0
            ok=1
            break
    if(M==done):
        root.quit()
    
    def play():
        x=1
        y=1
        for i in range(0,25):
            command = (lambda p1, p2: lambda: SScomm(p1, p2)) (x, y)
            butSS[i]=Button(root, image=tmp[M[x][y]], text=str(M[x][y]), command=command)
            butSS[i].image=tmp
            '''
            Place the buttons in the Grid
            '''
            butSS[i].grid(row=x-1,column=y-1,sticky=N+S+E+W)
            y=y+1
            if(y==6):
                y=1
                x=x+1
    if(ok==1):
        play()



'''
Shuffle the numbers
'''
easy=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
b=[]
for i in range(0,25):
    a=random.randint(0,24-i)
    b=b+[easy[a]]
    del easy[a]
'''
Create the 5x5 matrix and store the shuffled numbers inside it
'''
k=0
M =[[100]*7]
M.append([100])
M.append([100])
M.append([100])
M.append([100])
M.append([100])
M.append([100]*7)
done=[[100,100,100,100,100,100,100],[100,1,2,3,4,5,100],[100,6,7,8,9,10,100],[100,11,12,13,14,15,100],[100,16,17,18,19,20,100],[100,21,22,23,24,0,100],[100,100,100,100,100,100,100]]  
for i in range(0,5):
    for j in range(0,5):
        M[i+1].append(b[k])
        k=k+1
    M[i+1].append(100)
print(done)
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
for x in range(5):
    Grid.columnconfigure(root,x,weight=1)
for y in range(5):
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
for i in range(0,25):
    tmp.append(0)
    tmp[i] = PhotoImage(file='F://hard//'+str(i)+'.gif')
for i in range(0,25):
    butSS.append(0)
    command = (lambda p1, p2: lambda: SScomm(p1, p2)) (x, y)
    butSS[i]=Button(root, image=tmp[M[x][y]], text=str(M[x][y]), command=command)
    butSS[i].image=tmp
    '''
    Place the buttons in the Grid
    '''
    butSS[i].grid(row=x-1,column=y-1,sticky=N+S+E+W)
    y=y+1
    if(y==6):
        y=1
        x=x+1

'''
Keep main window open
'''
root.mainloop()


