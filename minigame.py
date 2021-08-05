from num_guess import num_guess_main as ng
from RoPaSc import ropasc_main as rps
from oddOrEven import odd_even_main as oe
from palindrome import palindrome_main as pd

games = [ng, rps, oe, pd]


def minigame():
    playagain = True
    gamecont = ["y", "n"]
    while playagain == True:
        sgame = input("Select game - [ng, rps, oe, pd]: ")
        eval(sgame + "()")
        newgame = input("New Game (y/n)?: ")
        if newgame in gamecont and newgame == "n":
            playagain = False
        elif newgame in gamecont and newgame == "y":
            continue
        else:
            print("Wrong input! Enter 'y' or 'n'.")
        print()


minigame()