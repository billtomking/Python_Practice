#随机下子
import copy
import random
from time import time
from pprint import pprint
import csv
TheBoard = {'1':' ','2':' ','3':' ',
            '4':' ','5':' ','6':' ',
            '7':' ','8':' ','9':' '}

jie = ''

def printboard(board):
    print('-' * 20)
    print(j + 1)
    print(jie)
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-' * 20)


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
    elif board['2'] == board['5'] and board['5'] == board['8']:
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


def You(board):
    you = []
    if board['1'] == board['2'] and board['2'] == turn and board['3'] == ' ':
        return 3
    elif board['1'] == board['3'] and board['3'] == turn and board['2'] == ' ':
        return 2
    elif board['2'] == board['3'] and board['3'] == turn and board['1'] == ' ':
        return 1
    elif board['4'] == board['5'] and board['5'] == turn and board['6'] == ' ':
        return 6
    elif board['4'] == board['6'] and board['6'] == turn and board['5'] == ' ':
        return 5
    elif board['5'] == board['6'] and board['6'] == turn and board['4'] == ' ':
        return 4
    elif board['7'] == board['8'] and board['8'] == turn and board['9'] == ' ':
        return 9
    elif board['7'] == board['9'] and board['9'] == turn and board['8'] == ' ':
        return 8
    elif board['8'] == board['9'] and board['9'] == turn and board['7'] == ' ':
        return 7
    elif board['1'] == board['4'] and board['4'] == turn and board['7'] == ' ':
        return 7
    elif board['1'] == board['7'] and board['7'] == turn and board['4'] == ' ':
        return 4
    elif board['4'] == board['7'] and board['7'] == turn and board['1'] == ' ':
        return 1
    elif board['2'] == board['5'] and board['5'] == turn and board['8'] == ' ':
        return 8
    elif board['2'] == board['8'] and board['8'] == turn and board['5'] == ' ':
        return 5
    elif board['5'] == board['8'] and board['8'] == turn and board['2'] == ' ':
        return 2      
    elif board['3'] == board['6'] and board['6'] == turn and board['9'] == ' ':
        return 9
    elif board['3'] == board['9'] and board['9'] == turn and board['6'] == ' ':
        return 6
    elif board['6'] == board['9'] and board['9'] == turn and board['3'] == ' ':
        return 3        
    elif board['1'] == board['5'] and board['5'] == turn and board['9'] == ' ':
        return 9
    elif board['1'] == board['9'] and board['9'] == turn and board['5'] == ' ':
        return 5
    elif board['5'] == board['9'] and board['9'] == turn and board['1'] == ' ':
        return 1   
    elif board['3'] == board['5'] and board['5'] == turn and board['7'] == ' ':
        return 7
    elif board['3'] == board['7'] and board['7'] == turn and board['5'] == ' ':
        return 5
    elif board['5'] == board['7'] and board['7'] == turn and board['3'] == ' ':
        return 3#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    if board['1'] == board['2'] and board['2'] != turn and board['2'] != ' ' and board['3'] == ' ':
        return 3
    elif board['1'] == board['3'] and board['3'] != turn and board['3'] != ' ' and board['2'] == ' ':
        return 2
    elif board['2'] == board['3'] and board['3'] != turn and board['3'] != ' ' and board['1'] == ' ':
        return 1
    elif board['4'] == board['5'] and board['5'] != turn and board['5'] != ' ' and board['6'] == ' ':
        return 6
    elif board['4'] == board['6'] and board['6'] != turn and board['6'] != ' ' and board['5'] == ' ':
        return 5
    elif board['5'] == board['6'] and board['6'] != turn and board['6'] != ' ' and board['4'] == ' ':
        return 4
    elif board['7'] == board['8'] and board['8'] != turn and board['8'] != ' ' and board['9'] == ' ':
        return 9
    elif board['7'] == board['9'] and board['9'] != turn and board['9'] != ' ' and board['8'] == ' ':
        return 8
    elif board['8'] == board['9'] and board['9'] != turn and board['9'] != ' ' and board['7'] == ' ':
        return 7  
    elif board['1'] == board['4'] and board['4'] != turn and board['4'] != ' ' and board['7'] == ' ':
        return 7
    elif board['1'] == board['7'] and board['7'] != turn and board['7'] != ' ' and board['4'] == ' ':
        return 4
    elif board['4'] == board['7'] and board['7'] != turn and board['7'] != ' ' and board['1'] == ' ':
        return 1    
    elif board['2'] == board['5'] and board['5'] != turn and board['5'] != ' ' and board['8'] == ' ':
        return 8
    elif board['2'] == board['8'] and board['8'] != turn and board['8'] != ' ' and board['5'] == ' ':
        return 5
    elif board['5'] == board['8'] and board['8'] != turn and board['8'] != ' ' and board['2'] == ' ':
        return 2        
    elif board['3'] == board['6'] and board['6'] != turn and board['6'] != ' ' and board['9'] == ' ':
        return 9
    elif board['3'] == board['9'] and board['9'] != turn and board['9'] != ' ' and board['6'] == ' ':
        return 6
    elif board['6'] == board['9'] and board['9'] != turn and board['9'] != ' ' and board['3'] == ' ':
        return 3        
    elif board['1'] == board['5'] and board['5'] != turn and board['5'] != ' ' and board['9'] == ' ':
        return 9
    elif board['1'] == board['9'] and board['9'] != turn and board['9'] != ' ' and board['5'] == ' ':
        return 5
    elif board['5'] == board['9'] and board['9'] != turn and board['9'] != ' ' and board['1'] == ' ':
        return 1      
    elif board['3'] == board['5'] and board['5'] != turn and board['5'] != ' ' and board['7'] == ' ':
        return 7
    elif board['3'] == board['7'] and board['7'] != turn and board['7'] != ' ' and board['5'] == ' ':
        return 5
    elif board['5'] == board['7'] and board['7'] != turn and board['7'] != ' ' and board['3'] == ' ':
        return 3
    else:
        for i in range(1,10):
            if board[str(i)] == ' ':
                you.append(str(i))
        random.shuffle(you)
        return you[0]


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
board = TheBoard
while j < int(ju):    
    FangFa=[]
    board = copy.copy(TheBoard)
    turn = 'X'
    n = 0
    jie = ''
    
    while n < 9:
        think = str(You(board))
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
                    jie = 'X赢了'
                    printboard(board)
            else :
                o +=1
                if FangFa not in oWin:
                    oWin.append(FangFa)
                    jie = 'O赢了'
                    printboard(board)
            n = 9
        elif n==8:
            j += 1
            p +=1
            n = 9
            jie = '平局'
            printboard(board)
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
with open('xW非随机('+ str(ju) +').csv','wt',newline='') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(xWin)

with open('oW非随机('+ str(ju) +').csv','wt',newline='') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(oWin)

print(len(xWin)+len(oWin))
print(time()-time1)

n = input()