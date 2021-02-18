"""
This module contains the playing board of the game.
We approach building the board by spliting into different tiles.
with  the y axis marked with letters and x axis marked with numbers. Kind of like a chess board but reversed.

The board is seperated into different rooms and doors with walls.

"""
#from intertools import chain

#from movement import *

board=[["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10"],
       ["b1","b2","b3","b4","b5","b6","b7","b8","b9","b10"],
       ["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"],
       ["d1","d2","d3","d4","d5","d6","d7","d8","d9","d10"], 
       ["e1","e2","e3","e4","e5","e6","e7","e8","e9","e10"],
       ["f1","f2","f3","f4","f5","f6","f7","f8","f9","f10"],
       ["g1","g2","g3","g4","g5","g6","g7","g8","g9","g10"],
       ["h1","h2","h3","h4","h5","h6","h7","h8","h9","h10"],
       ["i1","i2","i3","i4","i5","i6","i7","i8","i9","i10"],
       ["j1","j2","j3","j4","j5","j6","j7","j8","j9","j10"] ]

#board_flat_list = list(chain.from_iterable(board)) 


doors=["b1","b6","b4","b8","f2","d9","f9","h2"]
storage=["a1","b1"]
study=["a4","a5","a6","b4","b5","b6"]
lib=["a8","a9","a10","b8","b9","b10"]
kitchen=["e1","e2","f1","f2"]
teleport=["e5","f6"]
bathroom=["c9","c10","d9","d10"]
galery=["e9","e10","f9","f10","g9","g10"]
bed1=["h9","h10","i9","i10","j9","j10"]
bed2=["h1","h2","i1","i2","j1","j2"]
foyer=["i4","i5","i6","i7","j4","j5","j6","j7"]
#hallways= list(board_flat_list - storage - study - lib- kitchen - teleport - bathroom - galery - bed1 -bed2 -foyer)
#print(hallways)

"""
x=9
y=3

pos=board[x][y]

def movement():

    moveto = input("Which way do you want to move:- ") 
    
    if moveto=="mr" and y<10 or y>0:
        pos=board[x][y+1]
        print("Player is standing in ", pos,".")

    else:
        print("\n Invalid movement....re-enter.")



#print(board[1][1])

"""




