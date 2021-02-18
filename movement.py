from board import *

x=0
y=0
pos=board[x][y]
def movement():

    global x
    global y
    global pos
    
    moveto = (input("Which way do you want to move:- ")) 
    
    if moveto == "mr" :
        if y>=0 and y<9:    
            y=y+1
            pos=board[x][y]
            print("Player is standing in ", pos,".")
            #print(y)
        else:
            print("invalid move.")    

    
    elif moveto == "ml" :
        if  y<=9 and y>0:    
            y=y-1
            pos=board[x][y]
            print("Player is standing in ", pos,".")
            #print(y)
        else:
            print("invalid move.") 

    if moveto == "md" :
        if x>=0 and x<9:    
            x=x+1
            pos=board[x][y]
            print("Player is standing in ", pos,".")
            #print(x)
        else:
            print("invalid move.")    

    
    elif moveto == "mu" :
        if  x<=9 and x>0:    
            x=x-1
            pos=board[x][y]
            print("Player is standing in ", pos,".")
            #print(x)
        else:
            print("invalid move.") 
    
 #   else:
#          print("invalid move")    

    
for i in range(1,500):
   #print("grid:-",x,y)
   movement()










    


     


