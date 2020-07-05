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

##Sending 1-9 to the space_check method to check if empty space available
def full_board_check(borad):
    for i in range(1,10):
        if(space_check(board,i)):
            return False
    return True

##Check if input is in between 1-9 and also the place is empty
def player_choice(board):
    position=0
    while not position in [1,2,3,4,5,6,7,8,9] and not space_check(board,position):
        position =  int(input('Choose your next position: (1-9) '))

    return position

##Taking input from user if he/she wants to reply

def reply():
    return input(" Do you want to play again ? Type Yes or NO :").lower().startswith('y')

##Main Part - Which is controlling all functions above to thing happen

while True :
    board=[' ']*10   ##Creating a empty board array from 1-9

    player1_marker,player2_marker = player_input()      ##Selecting marker
    turn = choose_first()       ##Ranndomly select who's turn will be first
    print(turn + ' will go first')

    play=input('Are you ready to play ? Enter Yes or No')


    if play.lower()[0] == 'y':
        game_on = True
    else:
        game_on =False

    while game_on:      ##while loop contain things after starting the game
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1_marker,position)
            if win_check(board,player1_marker):
                display_board(board)
                print('Congratulations !! Player 1 Win')
                break;
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The Game Is Draw !!')
                    break;
                else:
                    turn='Player 2'

        else :


            ##  Player 2

            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations !! Player 2 Win')
                break;
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The Game Is Draw !!')
                    break;
                else:
                    turn = 'Player 1'

    if not reply():
        print('Thanks For Playing !!')
        break;