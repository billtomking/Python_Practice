import copy
import random
from time import time
from pprint import pprint
import csv
TheBoard = {'1':' ','2':' ','3':' ',
            '4':' ','5':' ','6':' ',
            '7':' ','8':' ','9':' '}


def Yan(board):
    if board['1'] == board['2'] and board['2'] == board['3']:
        if board['1'] != ' ':
            return 1
        else:
            return
    elif board['4'] == board['5'] and board['5'] == board['6']:
        if board['4'] != ' ':
            return 1
        else:
            return
    elif board['7'] == board['8'] and board['8'] == board['9']:
        if board['7'] != ' ':
            return 1
        else:
            return
    elif board['1'] == board['4'] and board['4'] == board['7']:
        if board['1'] != ' ':
            return 1
        else:
            return
    elif board['3'] == board['6'] and board['6'] == board['9']:
        if board['3'] != ' ':
            return 1
        else:
            return
    elif board['1'] == board['5'] and board['5'] == board['9']:
        if board['1'] != ' ':
            return 1
        else:
            return
    elif board['3'] == board['5'] and board['5'] == board['7']:
        if board['3'] != ' ':
            return 1
        else:
            return
    else:
        return


n=0
x=0
o=0
j=0
p=1

xWin=[]
oWin=[]
time1 = time()
ju = input('测试局数')
time1 = time()
while j < int(ju):    
    FangFa=[]
    board = copy.copy(TheBoard)
    turn = 'X'
    n = 0
    #print(j)
    
    while n < 9:
        #sprintboard(board)
        think = str(random.randint(1,9))
        if board[think] != ' ':
            continue
        FangFa.append(think)
        board[think] = turn
        if Yan(board) == 1:
            j += 1
            if turn == 'X':
                x +=1
                if FangFa not in xWin:
                    xWin.append(FangFa)
            else :
                o +=1
                if FangFa not in oWin:
                    oWin.append(FangFa)
            n = 9
        elif n==8:
            j += 1
            p +=1
            n = 9
        else:
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            n += 1

print('总数' + str(ju))
print('先手（X）胜数' + str(x))
print('后手（O）胜数' + str(o))
print('平局数' + str(p))
with open('xW.csv','wt',newline='') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(xWin)

with open('oW.csv','wt',newline='') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(oWin)

print(len(xWin)+len(oWin))
print(time()-time1)

n = input()