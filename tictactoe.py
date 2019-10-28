import time
import sys
import random

# "Main" method that calls all the other internal methods, like checking for wins and drawing the boards
def start_up():
    print("Welcome to Tic Tac Toe! This is a 2 - player game.")
    # Validating the input of each of the players, checking whether or not they have entered a name
    player_1_solved, player_2_solved = False, False
    while(player_1_solved != True):
        player_1_name = input("What is your name, Player 1?")
        time.sleep(0.45)
        if(player_1_name == ""):
            print("Please enter a name!")
            time.sleep(0.1)
        else:
            print("Welcome, Player " + "'" + str(player_1_name) + "'!")
            player_1_solved = True

    while(player_2_solved != True):
        player_2_name = input("What is your name, Player 2?")
        time.sleep(0.75)
        if(player_1_name == ""):
            print("Please enter a name!")
            time.sleep(0.1)
        else:
            print("Welcome, Player " + "'" + str(player_2_name) + "'!")
            player_2_solved = True
    random_player = random.randint(1, 2)
    time.sleep(0.45)
    # RNG that sees which player gets to go first
    if(random_player == 1):
        print("By a pseudorandom decision, Player '" + str(player_2_name) + "' will be given the first move.")
        first_player = player_2_name
        second_player = player_1_name
    else:
        print("By a pseudorandom decision, Player '" + str(player_1_name) + "' will be given the first move.")
        first_player = player_1_name
        second_player = player_2_name
    commence_game(first_player, second_player)
# A series of numerous print statements that create a tic tac toe board with a 3x3 2D array and 1 element in each of the 9 boxes
def draw_board(grid):
    # Drawing a tic - tac - toe board: Prints a 3x3 grid array.
    print("      A" + "   B   " + "C")
    print("    _____________")
    print(str(1) + "   | " + str(grid[0][0]) + "\t| " + str(grid[1][0]) + "\t| " + str(grid[2][0]) + "\t|")
    print("    -------------")
    print(str(2) + "   | " + str(grid[0][1]) + "\t| " + str(grid[1][1]) + "\t| " + str(grid[2][1]) + "\t|")
    print("    -------------")
    print(str(3) + "   | " + str(grid[0][2]) + "\t| " + str(grid[1][2]) + "\t| " + str(grid[2][2]) + "\t|")
    print("    _____________")
# This is the main logic of the game: While loops, checking for win validation, checking for ties, etc.
def commence_game(p1, p2):
    ttt_array = [[" " for x in range(3)] for y in range(3)]
    time.sleep(0.45)
    first_player = p1.title()
    # These are the two different symbols for ttt. Later, there will be random functionality added to the script.
    sym_1 = "X"
    sym_2 = "O"
    first_won, second_won = False, False
    count = 0
    while(first_won != True and second_won != True):
        fill_check = False
        while(fill_check != True):
            move = input("Player '" + first_player + "', make a move.")
            coord_list = parseCoordinates(move)
            w = coord_list[0]
            h = coord_list[1]
            # This plots and adds the tic tac toe tiles into the 2D array
            if(first_player.lower() == p1.title().lower()):
                if(ttt_array[w][h] == " "):
                    ttt_array[w][h] = sym_1
                    fill_check = True
                else:
                    print("You cannot fill an already completed square.")
            elif(first_player.lower() == p2.title().lower()):
                if(ttt_array[w][h] == " "):
                    ttt_array[w][h] = sym_2
                    fill_check = True
                else:
                    print("You cannot fill an already completed square.")
        count = count + 1
        draw_board(ttt_array)
        vert = checkVert(ttt_array, sym_1, sym_2)
        horiz = checkHorizontal(ttt_array, sym_1, sym_2)
        diag = checkDiagonal(ttt_array, sym_1, sym_2)
        if(vert == "W" or horiz == "W" or diag == "W"):
            print("Player '" + first_player + "' won!")
            play_again = input("Do you want to play again? (Y OR N)")
            rightInput = False
            # Script for playing again or exiting the game
            while(rightInput != True):
                if(play_again.lower() == "y"):
                    start_up()
                    rightInput = True
                elif(play_again.lower() == "n"):
                    time.sleep(0.55)
                    print("Thanks for Playing!!")
                    rightInput = True
                    sys.exit()
                else:
                    print("Invalid Input")
        # Simple iterating, player changing script that switches the two players to see who is first
        if (count % 2 == 0):
            first_player = p1.title()
        else:
            first_player = p2.title()
        if(checkTie(ttt_array) == "T"):
            print("The game was a tie! ")
            time.sleep(0.25)
            rightInput = False
            # Script for playing again or exiting the game
            while (rightInput != True):
                play_again = input("Do you want to play again? (Y OR N)")

                if (play_again.lower() == "y"):
                    start_up()
                    rightInput = True
                elif (play_again.lower() == "n"):
                    time.sleep(0.55)
                    print("Thanks for Playing!!")
                    rightInput = True
                    sys.exit()
                else:
                    print("Invalid Input")


# Checks to see if all the squares are filled in. Occurs after the win scenario testing, so there is not a risk of a over-counting or a misrepresenting a full win as a tie
def checkTie(arr):
    count = 0
    for i in range(3):
        for j in range(3):
            if(arr[i][j] == " "):
                count = count + 1
            else:
                pass
    if(count == 0):
        return "T"
    else:
        return "NT"
# Check of the three vertical win scenarios
def checkVert(array, sym_1, sym_2):
    if((array[0][0] == sym_1 and array[1][0] == sym_1 and array[2][0] == sym_1) or (array[0][1] == sym_1 and array[1][1] == sym_1 and array[2][1] == sym_1) or (array[2][0] == sym_1 and array[2][1] == sym_1 and array[2][2] == sym_1)):
        return "W"
    if ((array[0][0] == sym_2 and array[1][0] == sym_2 and array[2][0] == sym_2) or (array[0][1] == sym_2 and array[1][1] == sym_2 and array[2][1] == sym_2) or (array[2][0] == sym_2 and array[2][1] == sym_2 and array[2][2] == sym_2)):
        return "W"
    else:
        return "NW"
# Check of the three horizontal win scenarios
def checkHorizontal(array, sym_1, sym_2):
    if((array[0][0] == sym_1 and array[0][1] == sym_1 and array[0][2] == sym_1) or (array[1][0] == sym_1 and array[1][1] == sym_1 and array[1][2] == sym_1) or (array[2][0] == sym_1 and array[2][1] == sym_1 and array[2][2] == sym_1)):
        return "W"
    if ((array[0][0] == sym_2 and array[0][1] == sym_2 and array[0][2] == sym_2) or (array[1][0] == sym_2 and array[1][1] == sym_2 and array[1][2] == sym_2) or (array[2][0] == sym_2 and array[2][1] == sym_2 and array[2][2] == sym_2)):
        return "W"
    else:
        return "NW"
# Check of the two diagonal win scenarios
def checkDiagonal(array, sym_1, sym_2):
    if((array[0][0] == sym_1) and (array[1][1] == sym_1) and (array[2][2] == sym_1)):
        return "W"
    elif((array[2][0] == sym_1) and (array[1][1] == sym_1) and (array[0][2] == sym_1) ):
        return "W"
    if((array[0][0] == sym_2) and (array[1][1] == sym_2) and (array[2][2] == sym_2)):
        return "W"
    elif((array[2][0] == sym_2) and (array[1][1] == sym_2) and (array[0][2] == sym_2)):
        return "W"
    else:
        return "NW"
# Changing the user input coordinates "1, A" into 0,0, so that it can be incorporated into the two dimensional array
def parseCoordinates(coord):
    w = 0
    h = 0
    if(len(coord) == 2):
        coordinate_list = []
        for c in coord:
            coordinate_list.append(c)
        if("a" in coordinate_list):
            w = 0
        elif("b" in coordinate_list):
            w = 1
        elif("c" in coordinate_list):
            w = 2
        if("1" in coordinate_list):
            h = 0
        elif("2" in coordinate_list):
            h = 1
        elif("3" in coordinate_list):
            h = 2
    else:
        print("Error: Must enter two coordinates, in the form 'A1', '1A', etc. (Case Insensitive")
    parsed_list = [w, h]
    return parsed_list
start_up()