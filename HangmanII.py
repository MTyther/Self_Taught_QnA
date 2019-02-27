import random

def hangman(word):
    wrong = 0
    stages = ["",
              "________       ",
              "|              ",
              "|       |      ",
              "|       0      ",
              "|      /|\     ",
              "|      / \     ",
              "|              "
              ]
    secretword = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")


    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter:"
        char = input(msg)
        if char in secretword:
            charindx = secretword.index(char)
            board[charindx] = char
            secretword[charindx] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

wordlist = ['apple','banana','cherry','donut','egg','food']
randomword = random.choice(wordlist)
hangman(randomword) 
