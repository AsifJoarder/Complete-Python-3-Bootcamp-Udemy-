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