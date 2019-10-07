from Library import getWord as gw
import string


guessed = False
showWord = ""
exitGame = "a"


"""Hangman game function. Tracks guessed letters and turns passed and compares to correct word"""
def hangmanGame(difficulty_level):
    global exitGame
    wrongsLeft = 10          #number of wrong guesses until game ends
    lettersGuessed = ""     #list of guessed letters
    secretWord = gw(difficulty_level)   #word to be guessed. Function in Library.py
    while not guessed and wrongsLeft > 0:
        guess = takeTurn(secretWord, lettersGuessed, wrongsLeft)    #Gets player guess


        if guess not in secretWord and guess not in lettersGuessed:
            wrongsLeft -= 1
        if guess not in lettersGuessed:
            lettersGuessed += guess
        if guessed:
            break


    if guessed:
        print("You guessed the word: ", secretWord)
        while not exitGame == "":
            exitGame = input("Press enter to exit")

    else:
        printAppropriateHangman(0)
        print("Game over, no guesses left")
        print("The word was " + secretWord)
        while not exitGame == "":
            exitGame = input("Press enter to exit")



def takeTurn(secretWord, lettersGuessed, wrongsLeft):
    global showWord
    global guessed
    showWord = ""

    for i in range(0, len(secretWord)):

        if secretWord[i] in lettersGuessed:
            showWord += secretWord[i]
            showWord += " "
        elif secretWord[i] not in " !@#$%^&*()_+=-":
            showWord += "_ "
        else:
            showWord += ("  ")
    if "_" not in showWord:
        guessed = True
        return ""
    print("\n")
    printAppropriateHangman(wrongsLeft)
    print(showWord)
    print("wrong guesses left: ", wrongsLeft)
    print("Letters guessed: ", lettersGuessed)
    playerGuess = ""
    while playerGuess == "":
        playerGuess = str(input("Guess a letter: "))
        if not playerGuess.isalpha() and not playerGuess.islower() or len(playerGuess) > 1:
            print("Please put in only one lowercase letter")
            playerGuess = ""
    return playerGuess




def printAppropriateHangman(guessesLeft):
    if guessesLeft == 0:
        print(" _________")
        print("|        ♦  ")
        print("|       ( )")
        print("|       -|-")
        print("|      / | \ " )
        print("|     |  |  |")
        print("|     0  ^  0")
        print("|       / \  ")
        print("|      /   \ ")
        print("|     |     |")
        print("|     |     |")
        print("|    ~~     ~~")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")

    elif guessesLeft == 1:
        print(" _________")
        print("|        ♦  ")
        print("|       ( )")
        print("|       -|-")
        print("|      / | \ " )
        print("|     |  |  |")
        print("|     0  ^  0")
        print("|       / \  ")
        print("|      /   \ ")
        print("|     |     |")
        print("|     |     |")
        print("|            ")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")

    elif guessesLeft == 2:
        print(" _________")
        print("|        ♦  ")
        print("|       ( )")
        print("|       -|-")
        print("|      / | \ " )
        print("|     |  |  |")
        print("|     0  ^  0")
        print("|       / \  ")
        print("|      /   \ ")
        print("|     |     |")
        print("|")
        print("|")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")

    elif guessesLeft == 3:
        print(" _________")
        print("|        ♦  ")
        print("|       ( )")
        print("|       -|-")
        print("|      / | \ " )
        print("|     |  |  |")
        print("|     0  ^  0")
        print("|       / \  ")
        print("|      /   \ ")
        print("|")
        print("|")
        print("|")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")

    elif guessesLeft == 4:
        print(" _________")
        print("|        ♦  ")
        print("|       ( )")
        print("|       -|-")
        print("|      / | \ " )
        print("|     |  |  |")
        print("|     0  ^  0")
        print("|       / \  ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")

    elif guessesLeft == 5:
        print(" _________")
        print("|        ♦  ")
        print("|       ( )")
        print("|       -|-")
        print("|      / | \ " )
        print("|     |  |  |")
        print("|     0  ^  0")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")

    elif guessesLeft == 6:
        print(" _________")
        print("|        ♦  ")
        print("|       ( )")
        print("|       -|-")
        print("|      / | \ " )
        print("|     |  |  |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")

    elif guessesLeft == 7:
        print(" _________")
        print("|        ♦  ")
        print("|       ( )")
        print("|       -|-")
        print("|      / | \ " )
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")

    elif guessesLeft == 8:
        print(" _________")
        print("|        ♦  ")
        print("|       ( )")
        print("|       -|-")
        print("|" )
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")

    elif guessesLeft == 9:
        print(" _________")
        print("|        ♦  ")
        print("|       ( )")
        print("|")
        print("|" )
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")

    else:
        print(" _________")
        print("|        ♦  ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|             ")
        print("----------------")
        print("----------------")
        print("----------------")
if __name__ == '__main__':
    diff = input("Choose a level of difficulty (1-5) ")
    hangmanGame(diff)




