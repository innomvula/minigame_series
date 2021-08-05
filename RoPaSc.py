from random import randint

def ropasc():
    rps = ['rock', 'paper', 'scissors']
    bestOf = int(input("best of: "))
    winscore = (bestOf//2) + 1
    user1score = 0
    cp1score = 0
    havewinscore = False
    while havewinscore == False:
        j = randint(0,2)
        cp1 = rps[j]
    #    print(cp1)
        user1 = input("rock/paper/scissors: " )
        if user1 not in rps:
            print("error: incorrect input")
            print("score: " + str(user1score) + '-' + str(cp1score))
        else:
            pass
        if user1 == cp1:
            print("score: " + str(user1score) + '-' + str(cp1score))
        else:
            if user1 == 'rock' and cp1 == 'paper':
                cp1score += 1
                print("score: " + str(user1score) + '-' + str(cp1score))
            elif user1 == 'rock' and cp1 == 'scissors':
                user1score += 1
                print("score: " + str(user1score) + '-' + str(cp1score))
            elif user1 == 'paper' and cp1 == 'rock':
                user1score += 1
                print("score: " + str(user1score) + '-' + str(cp1score))
            elif user1 == 'paper' and cp1 == 'scissors':
                cp1score += 1
                print("score: " + str(user1score) + '-' + str(cp1score))
            elif user1 == 'scissors' and cp1 == 'rock':
                cp1score += 1
                print("score: " + str(user1score) + '-' + str(cp1score))
            elif user1 == 'scissors' and cp1 == 'paper':
                user1score +=1
                print("score: " + str(user1score) + '-' + str(cp1score))
        if user1score == winscore or cp1score == winscore:
            havewinscore = True
    if user1score > cp1score:
        print("User1 is the winner!!")
    else:
        print("CP1 is the winner!!")

def ropasc_main():
    playagain = True
    gamecont = ["y", "n"]
    while playagain == True:
        ropasc()
        while playagain == True:
            newgame = input("Play again (y/n)?: ")
            if newgame in gamecont and newgame == "n":
                playagain = False
            elif newgame in gamecont and newgame == "y":
                break
            else:
                print("Wrong input! Enter 'y' or 'n'.")
        print()
#main()