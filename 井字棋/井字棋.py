import copy
TheBoard = {'1':' ','2':' ','3':' ',
            '4':' ','5':' ','6':' ',
            '7':' ','8':' ','9':' '}

def printboard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

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
    elif board['2'] == board['5'] and board['5'] == board['8']:
        if board['3'] != ' ':
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
while True:    
    board = copy.copy(TheBoard)
    printboard(board)
    turn = 'X'
    n = 0
    while n < 9:
        think = input('选择下棋位置')
        if think not in board.keys():
            print('错误位置')
            print('合法位置有' + str(board.keys()))
            continue
        if board[think] != ' ':
            print('此位置已有棋子，请重新选择位置')
            continue
        board[think] = turn
        printboard(board)
        if Yan(board) == 1:
            print(str(turn) + '赢了')
            n = 9
        else:
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            n += 1
