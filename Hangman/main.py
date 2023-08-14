from hangman import *

if __name__ == "__main__":
    words = loadWords()
    newGame = Hangman()  

    newGame.run() 
