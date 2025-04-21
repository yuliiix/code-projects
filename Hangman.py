import random
import time
word_list = [
    "python", "developer", "keyboard", "function", "variable", "loop", "object", "class", "boolean", "syntax",
    "debug", "string", "method", "random", "internet", "program", "compile", "execute", "binary", "runtime",
    "array", "list", "tuple", "dictionary", "input", "output", "code", "error", "integer", "float",
    "char", "lambda", "import", "package", "module", "statement", "condition", "exception", "file", "index",
    "insert", "append", "remove", "split", "join", "sort", "reverse", "uppercase", "lowercase", "replace",
    "escape", "comment", "line", "block", "indent", "script", "command", "editor", "terminal", "interpreter",
    "operator", "compare", "while", "for", "if", "else", "elif", "true", "false", "none", "return",
    "break", "continue", "pass", "global", "local", "scope", "argument", "parameter", "default", "recursion",
    "nested", "math", "time", "open", "read", "write", "close", "with", "try", "except", "finally",
    "raise", "assert", "init", "super", "class", "public", "private", "protected", "static", "this", "self",
    "main", "looping", "conditionals", "inheritance", "polymorphism", "encapsulation", "abstraction", "design",
    "architecture", "refactor", "optimize", "debugging", "testing", "build", "deploy", "version", "commit",
    "push", "pull", "merge", "branch", "clone", "fork", "repository", "token", "api", "json", "html", "css",
    "javascript", "typescript", "react", "angular", "vue", "node", "express", "django", "flask", "mysql", "sqlite",
    "postgres", "server", "client", "protocol", "request", "response", "session", "cookie", "authentication",
    "authorization", "login", "logout", "register", "form", "button", "input", "output", "label", "layout",
    "grid", "flex", "media", "query", "responsive", "mobile", "desktop", "screen", "keyboard", "mouse", "monitor",
    "window", "frame", "dialog", "popup", "alert", "confirm", "prompt", "error", "warning", "info", "success",
    "animation", "transition", "hover", "click", "drag", "drop", "select", "checkbox", "radio", "slider",
    "volume", "brightness", "theme", "dark", "light", "mode", "settings", "preference", "option", "menu", "navigation",
    "sidebar", "footer", "header", "title", "caption", "content", "article", "section", "footer", "banner"
]
hangman_pics = [
    """
     -----
     |   |
         |
         |
         |
        ===
    """,
    """
     -----
     |   |
     O   |
         |
         |
        ===
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
        ===
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
        ===
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
        ===
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

def beginning_screen():
    print(r"""
  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       

        Welcome to HANGMAN!
        Try to guess the word before you get HANGED 
    """)
    time.sleep(1.5)
def display_hangman(tries):
    time.sleep(1)
    print(hangman_pics[tries])
def get_letter():
    while True:
        time.sleep(1)
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("❌ Invalid input. Please enter a single letter A–Z.")
def win_screen():
    print(r"""
╔════════════════════════╗
║    YOU SAVED THE WORD! ║
╚════════════════════════╝
 Congratulations! You win!
""")
def game_over_screen(chosen_word):
    print(r"""
╔═════════════════════════════╗
║  GAME OVER! YOU'RE HANGED!  ║
╚═════════════════════════════╝
""")
    print(f"The word was: {chosen_word}")
def game():
    chosen_word = random.choice(word_list)
    hidden_word = ["_"] * len(chosen_word)
    print( ", ".join(hidden_word))
    guessed_letters = []
    tries = 0
    display_hangman(tries)
    max_tries = len(hangman_pics) - 1
    
    while tries < max_tries and "_" in hidden_word:
        guess = get_letter()
        time.sleep(1)
        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue
        print(f"your guess is :{guess}")
        guessed_letters.append(guess)
        
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    hidden_word[i] = guess
            time.sleep(1)
            print( ", ".join(hidden_word))
        else:
            time.sleep(1)
            print("wrong guess! \n")
            print( ", ".join(hidden_word))
            tries += 1
        print(hangman_pics[tries])
        print(""*70)
        time.sleep(0.3)
        
    if "_" not in hidden_word:
        win_screen()
    else:
        game_over_screen(chosen_word)
        print(hangman_pics[tries])

    

beginning_screen()
while True:
    game()
    again = input("Do you want to play again? (y/n)").lower()
    print("\n" + "="*40 + "\n")
    if again != "y":
        print("see you lext time!")
        time.sleep(3)
        break
        
