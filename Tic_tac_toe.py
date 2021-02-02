board = ["-" ,"-" ,"-" ,
         "-" ,"-" ,"-" ,
         "-" ,"-" ,"-" ,]
#global var
game_on = True 
winner = None
current_player = "X" 
#Gonna print the whole board       
def Show_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")  
    print("\n")
def game():#actual logic of the game
    Show_board()

    while game_on:
        player_handling(current_player)

        check_if_game_over()

        change_player()
    #declaring the Winner
    if winner == "X" or winner == "O":
        print(winner + " won") 
    elif winner == None:
        print("Tie")       

def player_handling(player):#player handling
    print(player + "'s turn.")
    coordinate = input("Choose a number between 1 to 9: ") 
    correct = False
    while not correct:

        while coordinate not in ["1" , "2" ,"3" , "4" ,"5" ,"6" ,"7","8","9"]:
            coordinate = input("Unkown value Entered Choose from 1 - 9: ")

        coordinate = int(coordinate) -1 

        if board[coordinate] == "-":
            correct = True
        else:
            print("You Can't Go There , Plz Try again.") 

    board[coordinate] = player
    Show_board()

def change_player():#Must use golobal to change a var 
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"     
    return   

def check_if_game_over():
    check_game_win()
    check_game_tie()

def check_game_win():
    global winner
    #returns a boolean result and calling the fuction if true

    row_wins = rows()
    colom_wins = colom()
    diagonal_wins = diagonals()
    if row_wins:
        winner = row_wins
    elif colom_wins :
        winner = colom_wins 
    elif diagonal_wins:
        winner = diagonal_wins   
    else:
        winner = None        
    return
#Main three rules to win is to get three row or colom or diagonal the same
#this below checks for that
def rows():
    global game_on
    row1 = board[0] == board[1] == board[2] != "-" #all this var will return a boolean results
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    #if the the results of the var is true below runs
    if row1 or row2 or row3 :
        game_on =False
    #this will return the player who won by the index of it
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]            
    return

def colom():
    global game_on
    colom1 = board[0] == board[3] == board[6] != "-" 
    colom2 = board[1] == board[4] == board[7] != "-"
    colom3 = board[2] == board[5] == board[8] != "-"
    
    if colom1 or colom2 or colom3 :
        game_on =False

    if colom1:
        return board[0]
    elif colom2:
        return board[1]
    elif colom3:
        return board[2] 
    return

def diagonals():
    global game_on
    diagonal1 = board[0] == board[4] == board[8] != "-" 
    diagonal2 = board[6] == board[4] == board[2] != "-"
    
    if diagonal1 or diagonal2 :
        game_on =False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6] 
    return        
def check_game_tie():
    global game_on
    if "-" not in board:
        game_on = False
    return    
game()      
