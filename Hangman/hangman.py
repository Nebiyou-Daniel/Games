import random

def loadWords():
    '''
    This function will take a list of words from the "hangmanWords.txt" and
    return those words in the form of a list.
    The word's length range from 7 upto 13.
    '''
    WORDFILE = "hangmanWords.txt"
    words = open(WORDFILE, "r")
    lines = words.readline()
    
    wordList = lines.split()
    
    return wordList

def chooseWord():
    '''
    This function will take one word randomly from the given set of words.
    '''
    words = loadWords()
    return random.choice(words)


class Hangman():
    def __init__(self):
        '''
        When the Class if defined, it will take in a word the computer will
        have chosen for us.

        '''
        self.secretWord = chooseWord()
        self.numberOfTries = len(self.secretWord) + 3
        
        self.guessedLetters = []
        self.correctlyGuessedLetters = []
        self.availableLetters = 'abcdefghijklmnopqrstuvwxyz' # all small letters initially
        
    def getNumberOfTriesLeft(self):
        return self.numberOfTries
    
    def getGuessedLetters(self):
        return self.guessedLetters
    
    def getAvailableLetters(self):
        return self.availableLetters
    
    def isLetterGuessed(self, userGuess):
        if userGuess in self.guessedLetters:
            print("The letter '%s' has already been guessed, try another one." % userGuess)
        else:
            if userGuess in self.secretWord:
                self.correctlyGuessedLetters.append(userGuess)
                self.guessedLetters.append(userGuess)
                self.availableLetters = self.availableLetters.replace(userGuess, "_")
                self.setNumberOfTries(self.numberOfTries - 1)
                print("Good guess! It is found in the word!")
            else:
                self.guessedLetters.append(userGuess)
                self.availableLetters = self.availableLetters.replace(userGuess, "_")
                self.setNumberOfTries(self.numberOfTries - 1)
                print("Incorrect! the letter '%s' isn't found in the word." % userGuess)
    
    def isWordGuessed(self):
        for letter in self.secretWord:
            if letter not in self.correctlyGuessedLetters:
                return False
        return True
    
    def showGuessedWord(self):
        guessedWord = ""
        
        for letter in self.secretWord:
            if letter in self.correctlyGuessedLetters:
                guessedWord += letter + " "
            else:
                guessedWord += "_ "
                
        print(guessedWord)
    
    def run(self):
        
        self.showFirstMessages()
        
        while self.numberOfTries != 0:
            print()
            print("You have %d tries left." % self.numberOfTries)
            print("Here are the letters you are yet to use: %s" % self.availableLetters)
            print()
            print("Here is the secret word:", end=" ")
            self.showGuessedWord()

            print()

            if self.isWordGuessed():  
                print()
                print("CONGRATULATIONS! You did it! The word is '%s'." % self.secretWord)
                print()
                break
            
            userGuess = input("Please enter a letter: ")
            print()
            
            
            self.isLetterGuessed(userGuess)

        else:
            if self.isWordGuessed():
                print("CONGRATULATIONS! You did it! The word is '%s'." % self.secretWord)
                print()
            else:
                print("Sorry, but you ran out of guesses, the correct word is '%s'." % self.secretWord)
                print()
    
    def showFirstMessages(self):
        print()
        print("Try and guess my %d letter long word!" % len(self.secretWord))
        print()
        print("You have %d number of tries left!" % self.numberOfTries)

    
    def setNumberOfTries(self, number):
        self.numberOfTries = number    
    
    
    def isPlayerGuessCorrect(playerWord, chosenWord):
        # NOT USED FOR NOW
        '''
        Checks if the word the player fills in matches the word that the 
        computer chose for that round of the game.
        '''
        if playerWord == chosenWord:
            return True
        return False



