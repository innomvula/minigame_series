def is_palindrome(strng):
    rev_str = ""
    ngidx = -1
    for i in range(len(strng)):
        rev_str += strng[ngidx]
        ngidx -=1
        
    if rev_str == strng:
        return True
    else:
        return False

def pdrome():
    word = input("Give me a word and I will tell you if it is a palindrome or not: ")
    lword = word.lower()
    if lword.isalpha():
        if is_palindrome(lword) ==  True:
            print(f"{is_palindrome(lword)}, ".upper() + word + " is a palindrome!")
        else:
            print(f"{is_palindrome(lword)}, ".upper() + word + " is not a palindrome!")
    else:
        print("Input error! Type in a word.")
        
def palindrome_main():
    playagain = True
    gamecont = ["y", "n"]
    while playagain == True:
        pdrome()
        newgame = input("Play again (y/n)?: ")
        if newgame in gamecont and newgame == "n":
            playagain = False
        elif newgame in gamecont and newgame == "y":
            continue
        else:
            print("Wrong input! Enter 'y' or 'n'.")
        print()
#palindrome_main()