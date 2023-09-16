import numpy
import pprint
def print_board(board):
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')



def check_win():
    global win
    win = False
    board1 = {'1': ' ', '2': ' ', '3': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '7': ' ', '8': ' ', '9': ' '}
    values = list(board1.values())

    #horizontal

    # THIS IS WRONG beacuse I can't compare to single character to get good result
    # for i in numpy.arange(0, len(values), 3):
    #     if values[i:i+2] == 'X':
    #         print('X wins!')
    #     if values[i:i+2] == 'O':
    #         print('O wins!')
    #I have to use list comprehension
    for i in numpy.arange(0, len(values), 3):
        if all(x == 'X' for x in values[i:i+3]):
            print('X wins!')
            win=True
        if all(o == 'O' for o in values[i:i+3]):
            print('O wins!')
            win=True

    #vertical

    for i in numpy.arange(0, 3):
        if all(x == 'X' for x in values[i::3]): #start:stop:step i::3 is start from i end empty step 3
            print('X wins!')
            x=True
        if all(o == 'O' for o in values[i::3]):
            print('O wins!')
            x=True


    # diagonally
    diagonal1=[0, 4, 8]
    diagonal2=[2, 4, 6]

    if all(values[x] == 'X' for x in diagonal1): #if I dont write =='X' it will check if field is empty only
        print('X wins!')
        x = True
    if all(values[o] == 'O' for o in diagonal1):
        print('O wins!')
        x = True
    if all(values[x] == 'X' for x in diagonal2):
        print('X wins!')
        x = True
    if all(values[o] == 'O' for o in diagonal2):
        print('O wins!')
        x = True