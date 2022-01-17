board = [" " for i in range(9)]
help_board = [i for i in range(9)]

def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def print_help_board():
    row1 = "|{}|{}|{}|".format(help_board[0] + 1, help_board[1] + 1, help_board[2] + 1)
    row2 = "|{}|{}|{}|".format(help_board[3] + 1, help_board[4] + 1, help_board[5] + 1)
    row3 = "|{}|{}|{}|".format(help_board[6] + 1, help_board[7] + 1, help_board[8] + 1)
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def print_boards():
    print_help_board()
    print_board()
    
def player_move(icon):

    while True:
    
        if icon == "X":
            number = 1
        elif icon == "O":
            number = 2

        print("Your turn player {}".format(number))
        choice = int(input("Enter your move (1-9):").strip())
        if board[choice - 1] == " ":
            board[choice - 1] = icon
            break
        else:
            print()
            print("That space is taken")
        
def win(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
    
def draw():

    if not win("X") and not win("O") and (" " not in board):
        return True
    else:
        return False
 
while True:
    print_boards()
    player_move("X")
    print_boards()
    if win("X"):
        print("X wins!")
        break
    if draw():
        print("Draw!")
        break
    player_move("O")
    if win("O"):
        print_boards()
        print("O wins!")
        break
    if draw():
        print("Draw!")
        break
