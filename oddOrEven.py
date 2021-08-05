def odd_even():
    num = int(input("what number are you thinking? "))
    if num % 2 != 0:
        print("That's an odd number! Have another?")
    else:
        print("That's an even number!!")

def odd_even_main():
    playagain = True
    gamecont = ["y", "n"]
    while playagain == True:
        odd_even()
        newgame = input("Play again (y/n)?: ")
        if newgame in gamecont and newgame == "n":
            playagain = False
        elif newgame in gamecont and newgame == "y":
            continue
        else:
            print("Wrong input! Enter 'y' or 'n'.")
        print()
#odd_even_main()
            
    
    