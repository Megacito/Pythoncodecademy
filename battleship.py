from random import randint #imports random and randint modules

board = [] #creates board list

for x in range(5): #iterates through list across 5
    board.append(["O"] * 5) #appends O string across 5 and down 5

def print_board(board): # removing the ""
    for row in board:
        print " ".join(row)
print "Let's play Battleship!"
print print_board(board)

def random_row(board): #returns random row coordinate
    return randint(0, len(board) - 1)

def random_col(board): #returns random col coordinate
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

for turn in range(4):
    
    guess_row = int(raw_input("Guess Row:")) 
    guess_col = int(raw_input("Guess Col:")) 

    if turn == 3:
        print "Game Over"
        print "You have no more turns"
        print "Chantal smells"
        print "kissy"
        break
    elif guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    elif(guess_row < 0 or guess_row > 4) or (guess_col < 0        or guess_col > 4):
        print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
    
   
        print "Turn", turn + 1 # Print (turn + 1) here!
    print_board(board)
