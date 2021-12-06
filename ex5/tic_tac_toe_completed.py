theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
theBoard_simple = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
move = ""


def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def check_score(theBoard, theBoard_simple, turn):
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
        print_board(theBoard_simple)
        print("")
        print_board(theBoard)
        print("")
        print(turn + " wins.")
        return True
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
        print_board(theBoard_simple)
        print("")
        print_board(theBoard)
        print("")
        print(turn + " wins.")
        return True
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
        print_board(theBoard_simple)
        print("")
        print_board(theBoard)
        print("")
        print(turn + " wins.")
        return True
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
        print_board(theBoard_simple)
        print("")
        print_board(theBoard)
        print("")
        print(turn + " wins.")
        return True
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
        print_board(theBoard_simple)
        print("")
        print_board(theBoard)
        print("")
        print(turn + " wins.")
        return True
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
        print_board(theBoard_simple)
        print("")
        print_board(theBoard)
        print("")
        print(turn + " wins.")
        return True
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
        print_board(theBoard_simple)
        print("")
        print_board(theBoard)
        print("")
        print(turn + " wins.")
        return True
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
        print_board(theBoard_simple)
        print("")
        print_board(theBoard)
        print("")
        print(turn + " wins.")
        return True


turn = 'X'
print("Starting Tic Tac Toe")
print("")
for i in range(9):
    print_board(theBoard_simple)
    print("")
    print_board(theBoard)
    while True:
        move = input(f'Input a number 1 to 9 to place {turn} in one of the nine squares: ')
        if move in theBoard.keys():
            if theBoard[move] == ' ':
                theBoard[move] = turn
                break
    print("")
    if i >= 4:
        result = check_score(theBoard, theBoard_simple, turn)
        if result:
            break
    if i == 8:
        print_board(theBoard_simple)
        print("")
        print_board(theBoard)
        print("")
        print("Both tie.")
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
