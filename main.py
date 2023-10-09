#Tic Tac Toe code by Shashwat Srivastava
row1 = []
row2 = []
row3 = []

#Creates Tic Tac Toe Board
def creating_grid():
    global row1
    global row2
    global row3
    row1 = [' ',' ',' ']
    row2 = [' ',' ',' ']
    row3 = [' ',' ',' ']

#Player X's turn definition, takes the row and position input and inserts X at given position
#Checks to make sure position is not already taken aswell
def playerX_pick_row(character):
    global row1
    global row2
    global row3
    position = input("At what position would you like to place your X?(1/2/3)")
    position = int(position)
    if (character == "r1"):
        if (row1[position-1] == "O"):
            print("This spot is already taken, please pick a blank spot")
            return False
        else:
            row1[position-1] = "X"
            return True
    elif (character == "r2"):
        if (row2[position-1] == "O"):
            print("This spot is already taken, please pick a blank spot")
            return False
        else:
            row2[position-1] = "X"
            return True
    elif (character == "r3"):
        if (row3[position-1] == "O"):
            print("This spot is already taken, please pick a blank spot")
            return False
        else:
            row3[position-1] = "X"
            return True

#Player O's turn definition, takes the row and position input and inserts O at given position
#Checks to make sure position is not already taken aswell
def playerO_pick_row(character):
    global row1
    global row2
    global row3
    position = input("At what position would you like to place your O?(1/2/3)")
    position = int(position)
    if (character == "r1"):
        if (row1[position-1] == "X"):
            print("This spot is already taken, please pick a blank spot")
            return False
        else:
            row1[position-1] = "O"
            return True
    elif (character == "r2"):
        if (row2[position-1] == "X"):
            print("This spot is already taken, please pick a blank spot")
            return False
        else:
            row2[position-1] = "O"
            return True
    elif (character == "r3"):
        if (row3[position-1] == "X"):
            print("This spot is already taken, please pick a blank spot")
            return False
        else:
            row3[position-1] = "O"
            return True

#Checks for all possible win cases for player X and returns whether the game is done or not in a boolean value
def win_checkX():
    global row1
    global row2
    global row3
    if (row1[0] == "X" and row1[1] == "X" and row1[2] == "X"):
        print("Game Over!")
        return True
    elif (row2[0] == "X" and row2[1] == "X" and row2[2] == "X"):
        print("Game Over")
        return True
    elif (row3[0] == "X" and row3[1] == "X" and row3[2] == "X"):
        print("Game Over")
        return True
    elif (row1[0] == "X" and row2[0] == "X" and row3[0] == "X"):
        print("Game Over")
        return True
    elif (row1[1] == "X" and row2[1] == "X" and row3[1] == "X"):
        print("Game Over")
        return True
    elif (row1[2] == "X" and row2[2] == "X" and row3[2] == "X"):
        print("Game Over")
        return True
    elif (row1[0] == "X" and row2[1] == "X" and row3[2] == "X"):
        print("Game Over")
        return True
    elif (row1[2] == "X" and row2[1] == "X" and row3[0] == "X"):
        print("Game Over")
        return True
    else :
        return False

#Checks for all possible win cases for player O and returns whether the game is done or not in a boolean value   
def win_checkO():
    global row1
    global row2
    global row3
    if (row1[0] == "O" and row1[1] == "O" and row1[2] == "O"):
        print("Game Over!")
        return True
    elif (row2[0] == "O" and row2[1] == "O" and row2[2] == "O"):
        print("Game Over")
        return True
    elif (row3[0] == "O" and row3[1] == "O" and row3[2] == "O"):
        print("Game Over")
        return True
    elif (row1[0] == "O" and row2[0] == "O" and row3[0] == "O"):
        print("Game Over")
        return True
    elif (row1[1] == "O" and row2[1] == "O" and row3[1] == "O"):
        print("Game Over")
        return True
    elif (row1[2] == "O" and row2[2] == "O" and row3[2] == "O"):
        print("Game Over")
        return True
    elif (row1[0] == "O" and row2[1] == "O" and row3[2] == "O"):
        print("Game Over")
        return True
    elif (row1[2] == "O" and row2[1] == "O" and row3[0] == "O"):
        print("Game Over")
        return True
    else :
        return False

#Game Intro
creating_grid()
print("Welcome to Tic Tac Toe, here is the board. The top row is r1, and so on.\nThe positions read from left to right starting at 1 and ending at 3")
print(row1)
print(row2)
print(row3)

#Loop that runs game
while True:
    while True: #Loop that waits for Player X turn
        playerX_turn = input("What row do you want to input your X?(r1/r2/r3)")
        if (playerX_pick_row(playerX_turn) == True):
            break
    #Prints gameboard every turn with updated values
    print(row1)
    print(row2)
    print(row3)
    if (win_checkX() == True): #If player X wins the game, stops game
        break

    while True: #Loop that waits for Player O turn
        playerO_turn = input("What row do you want to input your O?(r1/r2/r3)")
        if (playerO_pick_row(playerO_turn) == True):
            break

    if (win_checkO() == True): #If player O wins game, stops game
        break
    #Prints gameboard every turn with updated values
    print(row1)
    print(row2)
    print(row3)
    
print("Thanks for playing!!")
