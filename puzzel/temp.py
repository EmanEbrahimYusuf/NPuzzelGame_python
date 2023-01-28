import numpy as np
def get0Index(puzzle):
    for (y, row) in enumerate(puzzle):
        for x, value in enumerate(row):
            if (value == 0):
                return (y, x)
def get0Index2( puzzle):
    y,x=np.where(np.array(puzzle)==0)
    return y[0],x[0]
    
x=[[ 1 ,  2 ,  7 , 3 ],
   [ 5 ,  6 ,  4 , 8 ],
   [ 9 , 10 , 11 , 0 ],
   [ 13, 14 , 15 , 12]]

def step(x):
    li=[[0,1,2],[3,4,5],[6,7,8]]
    li2 = [ y for x in li for y in x]
    return ''.join(map(str,li2))

board = np.array(x).flatten()
s= sum(abs((val-1)%4 - i%4) + abs((val-1)//4 - i//4)
        for i, val in enumerate(board) if val)
print(s)
x=[[ 1 ,  2 ,  7 , 3 ],
   [ 5 ,  6 ,  4 , 8 ],
   [ 9 , 10 , 11 , 0 ],
   [ 13, 14 , 15 , 12]]

def manhattanDistance():
        distance = 0
        for i in range(0, 4):
            for j in range(0, 4):
                if(x[i][j] != 0):
                    l, y = divmod(x[i][j]-1,4)
                    distance += abs(l-i)+abs(y-j)
        return distance

print(manhattanDistance())