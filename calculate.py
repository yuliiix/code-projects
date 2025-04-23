import time
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def set_screen_size(columns=60, lines=20):
    if os.name == "nt":
        os.system(f'mode con: cols={columns} lines={lines}')
    else:
        print(f"\033[8;{lines};{columns}t")
def show_board1(board):
    print()
    print(f"{board[0]} + {board[1]} = {board[2]}")
    print()
def show_board2(board):
    print()
    print(f"{board[0]} - {board[1]} = {board[2]}")
    print()
def show_board3(board):
    print()
    print(f"{board[0]} * {board[1]} = {board[2]}")
    print()
def show_board4(board):
    print()
    print(f"{board[0]} / {board[1]} = {board[2]}")
    print()
def show_board5(board):
    print()
    print(f"{board[0]} ^ {board[1]} = {board[2]}")
    print()
def fix_number(n):
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n
def pause():
    time.sleep(0.5)
def plus():
    board = ["_", "_", "_"]
    show_board1(board)

    num1 = float(input("choose number 1: "))
    num1 = fix_number(num1)
    board[0] = num1
    pause()
    show_board1(board)

    num2 = float(input("choose number 2: "))
    num2 = fix_number(num2)
    pause()
    board[1] = num2

    result = num1 + num2
    result = fix_number(result)
    board[2] = result
    pause()
    show_board1(board)

def minus():
    board = ["_", "_", "_"]
    show_board2(board)

    num1 = float(input("choose number 1: "))
    num1 = fix_number(num1)
    board[0] = num1
    pause()
    show_board2(board)

    num2 = float(input("choose number 2: "))
    num2 = fix_number(num2)
    pause()
    board[1] = num2

    result = num1 - num2
    result = fix_number(result)
    board[2] = result
    pause()
    show_board2(board)

def multiply():
    board = ["_", "_", "_"]
    show_board3(board)

    num1 = float(input("choose number 1: "))
    num1 = fix_number(num1)
    board[0] = num1
    pause()
    show_board3(board)

    num2 = float(input("choose number 2: "))
    num2 = fix_number(num2)
    board[1] = num2 
    pause()
    result = num1 * num2
    result = fix_number(result)
    board[2] = result
    pause()
    show_board3(board)

def divide():
    board = ["_", "_", "_"]
    show_board4(board)

    num1 = float(input("choose number 1: "))
    num1 = fix_number(num1)
    board[0] = num1
    show_board4(board)

    num2 = float(input("choose number 2: "))
    while num2 == 0:
        print("Cannot divide by 0. Try again.")
        num2 = float(input("choose number 2: "))
    num2 = fix_number(num2)
    board[1] = num2
    pause()
    result = num1 / num2
    result = fix_number(result)
    board[2] = result
    pause() 
    show_board4(board)

def power():
    board = ["_", "_", "_"]
    show_board5(board)

    num1 = float(input("choose number 1: "))
    num1 = fix_number(num1)
    board[0] = num1 
    pause()
    show_board5(board)

    num2 = float(input("choose number 2: "))
    num2 = fix_number(num2)
    board[1] = num2
    pause()
    result = num1 ** num2
    result = fix_number(result)
    board[2] = result
    pause()
    show_board5(board)


def game():
    print(r"""
         *** Welcome to the CALCULATE Game ***
     Type two numbers and an operation (+, -, *, /, ^)
           Let's see how smart your math is!
""")
    time.sleep(3)
    clear_screen()
    while True:
        
        choice = input("Choose an operation (+, -, *, /, ^) or 'q' to quit: ")
        if choice == "q":
            print("Thanks for playing! Goodbye!")
            time.sleep(2)
            break
        elif choice == "+":
            pause()
            plus()
        elif choice == "-":
            pause()
            minus()
        elif choice == "*":
            pause()
            multiply()
        elif choice == "/":
            pause()
            divide()
        elif choice == "^":
            pause()
            power()
        else:
            print("Invalid operation. Please try again.")
        time.sleep(3)
        clear_screen()
def all():
    set_screen_size()
    game()
all()

