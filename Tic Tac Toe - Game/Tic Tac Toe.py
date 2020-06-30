import random

## Display Board Function ##

def display_board(board):
    print('\n' * 50)

    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9] + ' ')
    print('---' + '|' + '---' + '|' + '---')
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6] + ' ')
    print('---' + '|' + '---' + '|' + '---')
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3] + ' ')

## Taking Input From Player To Select The Marker X or O ##

def player_input():
    marker=''

    while not (marker=='X' or marker=='O'):
        marker=input('Player 1 Select marker O or X').upper()
    if (marker=='X'):
        return ('X','O')
    else:
        return ('O','X')

## Place marker

def place_marker(board, marker, position):
    board[position] = marker

## Add Function to check if someone win

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

##Generating a random number to decide which player will go first

def choose_first ():
    if random.randint(0,1)==0:
        return "Player 1"
    else :
        return "Player 2"


##Checking if any empty position is left on the board

def space_check (board,position):
    return board[position]==' '