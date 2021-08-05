from random import randint
def num_guess():
    chance = 5
    num = randint(1, 100)
    print(num)
    while chance > 0:
        guess = int(input("guess: "))
        chance -= 1
        diff = abs(guess - num)
        if guess == num:
            print("guessed correctly :)")
            print("Chances left: {}".format(chance))
            break
        elif guess > num and chance != 0:
            if diff <= 20:
                print("Wrong!! But you are close. Guess lower!")
                print("Chances left: {}".format(chance))
            else:
                print("guessed incorrectly :(")
                print("Chances left: {}".format(chance)) 
        elif guess <= num and chance != 0:
            if diff < 20:
                print("Wrong!! But you are close. Guess higher!")
                print("Chances left: {}".format(chance))
            else:
                print("guessed incorrectly :(")
                print("Chances left: {}".format(chance)) 
        else:
            print("guessed incorrectly :(")
            print("Chances left: {}".format(chance))
            print(f"The number was {num}")
def num_guess_main():
    playagain = True
    gamecont = ["y", "n"]
    while playagain == True:
        num_guess()
        newgame = input("Play again (y/n)?: ")
        if newgame in gamecont and newgame == "n":
            playagain = False
        elif newgame in gamecont and newgame == "y":
            continue
        else:
            print("Wrong input! Enter 'y' or 'n'.")
        print()
#num_guess_main()