import random
import time
def show_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()
def board_is_full(board):
    return all(spot in ["X", "O"] for spot in board)
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True 
    
    return False
def game():
    board = ["1","2","3","4","5","6","7","8","9"]
    current_play = "X"
    computer_play = "O"

    while True:
        show_board(board)
        
    # player's turn
        move = input("Choose a number for X's spot: ")
        time.sleep(0.5)
        if move in board:
            board[int(move) - 1] = current_play
        # check if player won
            if check_winner(board, current_play):
                show_board(board)
                print("Player X wins!")
                break
        else:
            print("It's taken. Please choose another one")
            continue 
        # check if board is full
        if board_is_full(board):
            show_board(board)
            print("Game over! Board is full.")
            break
        # computer's turn   SMART COMPUTER MOVE: Win → Block → Random
       
        time.sleep(0.6)
        moved = False
        #computer is trying to win        
        for spot in board:
            if spot not in ["X", "O"]:
                temp_board = board.copy()
                temp_board[int(spot) - 1] = computer_play
                if check_winner(temp_board, computer_play):
                    board[int(spot) - 1] = computer_play
                    moved = True
                    break
        # if it can't win he tries to block X
        if not moved:
            for spot in board:
                if spot not in ["X", "O"]:
                    temp_board = board.copy()
                    temp_board[int(spot) - 1] = current_play
                    if check_winner(temp_board, current_play):
                        board[int(spot) - 1] = computer_play
                        moved = True
                        break
        # can't block or win , it will choose a random spot
        if not moved:
            available_spots = [spot for spot in board if spot not in ["X", "O"]]
            computer_choice = random.choice(available_spots)
            board[int(computer_choice) - 1] = computer_play
        
        show_board(board)
        print("\n"*5)
        if check_winner(board, computer_play):
            show_board(board)
            print("Computer wins!")
            break

        

        if board_is_full(board):
            show_board(board)
            print("Game is over! Board is full.")
            break

def friends():
    board = ["1","2","3","4","5","6","7","8","9"]
    player1 = "X"
    player2 = "O"

    while True:
        show_board(board)
        time.sleep(0.5)
        move1 = input("Choose a number for X's spot: ")
        time.sleep(0.5)
        if move1 in board:
            board[int(move1) - 1] = player1
            show_board(board)
    
            if check_winner(board, player1):
                show_board(board)
                print(" Player X wins!")
                break
        else:
            print("It's taken. Please choose another one")
            continue 

        if board_is_full(board):
            show_board(board)
            print("Game over! Board is full.")
            break
        time.sleep(0.5)
        move2 = input("Choose a number for O's spot: ")
        time.sleep(0.5)
        if move2 in board:
            board[int(move2) - 1] = player2
    
            if check_winner(board, player2):
                show_board(board)
                print("Player O wins!")
                break
        else:
            print("It's taken. Please choose another one")
            continue 
       
        if check_winner(board, player2):
            show_board(board)
            print("Player O wins!")
            break

        

        if board_is_full(board):
            show_board(board)
            print("Game is over! Board is full.")
            break



def screen():
    while True:
        time.sleep(0.5)
        print(r""")
        
████████╗██╗ ██████╗      ████████╗ █████╗  ██████╗       ████████╗ ██████╗ ███████╗
╚══██╔══╝██║██╔═══        ╚══██╔══╝██╔══██╗██╔═══         ╚══██╔══╝██╔═══██╗██╔════╝
   ██║   ██║██║       █████╗ ██║   ███████║██║      █████╗   ██║   ██║   ██║█████╗  
   ██║   ██║██║       ╚════╝ ██║   ██╔══██║██║      ╚════╝   ██║   ██║   ██║██╔══╝    
   ██║   ██║╚██████          ██║   ██║  ██║╚██████           ██║   ╚██████╔╝███████╗
   ╚═╝   ╚═╝ ╚═════╝         ╚═╝   ╚═╝  ╚═╝ ╚═════╝          ╚═╝    ╚═════╝ ╚══════╝""")
        time.sleep(1)
        choose = input(r"""
                       
                                Welcome to Tic Tac Toe! 
            Do you prefer play against a friend or the computer? (friend = f, computer = c)
                                    Your answer: """).lower()
                            



         
           
        if choose == "c":
            time.sleep(1)
            print("\n" *5)
            game()
        elif choose == "f":
            time.sleep(1)
            print("\n" *5)
            friends()
        else:
            print("Invalid. Try again")
            continue

        again = input("Do you want to play again? (y/n)").lower()
        if again != "y":
            print("See you next time!")
            break

    

                   
screen()