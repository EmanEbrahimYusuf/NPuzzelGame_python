import os


from sympy import root
from BFS_Solver import BFS
from puzzel_file import *
from solver import *
import time
import numpy as np

def getTestCases(foldername):
    cases=[]
    for f in os.listdir(foldername):
        file =open(foldername+'/'+f,'r')
        data=file.read()
        data=data.split("\n")
        a=[]
        for x in range(2,len(data)):
            a.append(data[x])
        array=[]
        for x in a:
            for c in x.split(" "):
                if(c != ''):
                   array.append(int(c))
        array=np.array(array)
        array= array.reshape(int(data[0]),int(data[0]))
        cases.append(array)
    return cases

loop=True
while loop:

    print('Sample Test Solvable Puzzles ?                       => 1')
    print('Sample Test Unsolvable Puzzles ?                     => 2')
    print('Complete Test Solvable puzzles Manhattan & Hamming ? => 3')
    print('Complete Test Solvable puzzles Manhattan Only ?      => 4')
    print('Complete Test V. Large test case ?                   => 5')
    print("Complete Test Unsolvable puzzles ?                   => 6")
    v=int(input("Enter The Tests Number                               => "))
    
    folder=''
    case=[]
    if v==1:
        folder='test_cases\Sample Solvable Puzzles'
    elif v==2:
        folder='test_cases\Sample Unsolvable Puzzles'
    elif v==3:
        folder='test_cases\Complete Solvable puzzles\Manhattan & Hamming'
    elif v==4:
        folder='test_cases\Complete Solvable puzzles\Manhattan Only'
    elif v==5:
        folder='test_cases\Complete V. Large test case'
    elif v==6:
        folder='test_cases\Complete Unsolvable puzzles'
    else:
        print('invaled chose... ):')
    if folder!='':

        tests=getTestCases(folder)
        print(" We Have "+str(len(tests))+" Tests")
        for x in tests:
            print(x)
            n=0
            puzzle = Puzzel(x)
            s = Solver(puzzle,len(x))
            b=BFS(puzzle,len(x))
            if(s.isSolveble(x)):
                print("solveble.... :)")
                tic = time.time()
                p = s.solve()
                toc = time.time()
                steps = 0
                for node in p:
                    
                    #print(node.action)
                    #node.puzzle.printPuzzel()
                    steps += 1
                
                print("Total number of steps in : " + str(steps))
                print("Total amount of time in search: " + str(toc - tic) + " second(s)")
                print('---------------------------------------------------------------------------')
            else:
                print("Not solveble....... :(")
                print('---------------------------------------------------------------------------')
    k=input('You Want To Mack Another Operation [y,n]')
    k='y'
    if k=='y':
        loop=True
    elif k=='n':
        loop = False
    else:
        print("invalid")