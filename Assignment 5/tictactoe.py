import random
import time
row_number=[]
col_number=[]
game = [['_' , '_' , '_'],
        ['_' , '_' , '_'],
        ['_' , '_' , '_']]
start_time = time.time()
game_mode = input("select game mode:")

def player1(row , col):
    if 0 <= row <= 2 and 0 <= col <= 2 :
        game[row][col] = 'X'
        
    else:
        print("index out of range , try again!")
        
    
def player2(row , col):
    if 0 <= row <= 2 and 0 <= col <= 2 :
        game[row][col] = 'O'
    else:
        print("index out of range , try again!")

def player2_pc():
    random_row = random.randint(0,2)
    random_col = random.randint(0,2)
    if random_row not in row_number and random_col not in col_number :
        game[random_row][random_col] = 'O'
 
    elif random_row in row_number and random_col in col_number :
        print("the selected row/col is already taken!")

        

def show_game_board():
    for i in range (3):
        for j in range(3):
            print(game[i][j] , end = ' ')
    print()

def check():

    if game[0][0] == 'X' and game[0][1] == 'X' and game[0][2] == 'X':
        print("congrats! player1 wins^-^")
        exit()
    elif game[1][0] == 'X' and game[1][1] == 'X' and game[1][2] == 'X':
        print("congrats! player1 wins^-^")
        exit()
    elif game[2][0] == 'X' and game[2][1] == 'X' and game[2][2] == 'X':
        print("congrats! player1 wins^-^")
        exit()
    elif game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        print("congrats! player1 wins^-^")
        exit()
    elif game[0][2] == 'X' and game[0][1] == 'X' and game[2][0] == 'X':
        print("congrats! player1 wins^-^")
        exit()


    if game[0][0] == 'O' and game[0][1] == 'O' and game[0][2] == 'O':
        print("congrats! player2 wins^-^")
        exit()
    elif game[1][0] == 'O' and game[1][1] == 'O' and game[1][2] == 'O':
        print("congrats! player2 wins^-^")
        exit()
    elif game[2][0] == 'O' and game[2][1] == 'O' and game[2][2] == 'O':
        print("congrats! player2 wins^-^")
        exit()
    elif game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        print("congrats! player2 wins^-^")
        exit()
    elif game[0][2] == 'O' and game[0][1] == 'O' and game[2][0] == 'O':
        print("congrats! player2 wins^-^")
        exit()
if game_mode == "1 player":
    while True:
        x_row = int(input("satr ra vared konid:"))
        x_col = int(input("sotun ra vared konid:"))
        player1(x_row , x_col)
        
    
    

        o_row = int(input("satr ra vared konid:"))
        o_col = int(input("sotun ra vared konid:"))
        player2(o_row , o_col)
        
    
    

        show_game_board()
        check()
        print(start_time)
if game_mode == "multi player":
    while True:
        x_row = int(input("satr ra vared konid:"))
        x_col = int(input("sotun ra vared konid:"))
        player1(x_row , x_col)
    
    
        player2_pc()
    
    

        show_game_board()
        check()
        print(start_time)



