import random

class RockPaperScissor:
    def __init__(self):
        self.playerPoints = 0
        self.computerPoints = 0
        self.moves = ['r', 'p', 's'] # r stands for rock, p for paper and s for scissor!
    
    def run(self):
        print("WELCOME TO ROCK PAPER SCISSORS")
        print()
  
        while True:
            options = input("Enter '1' to play a new game, '2' to play again with computer and '3' to end the program. \nEnter your choice: ")

            if options == '1':
                self.playerPoints = 0
                self.computerPoints = 0
                
                self.playAgainstComputer(self.playerPoints, self.computerPoints)
            
            elif options == '2':
                if self.playerPoints == 0 and self.computerPoints == 0:
                    print("YOU CAN'T PLAY AGAIN SINCE YOU HAVEN'T PLAYED YET. TRY '1' OR '3'.\n")
                else:
                    self.playAgainstComputer(self.playerPoints, self.computerPoints)
            
            elif options == '3':
                print("\nTHANK YOU FOR PLAYING!")
                break
            else:
                print("\nINVALID COMMAND! TRY AGAIN!\n")
    
    def playAgainstComputer(self, playerPoints, computerPoints):
        
        self.computerPoints = computerPoints
        self.playerPoints = playerPoints
        
        computerAction = self.moves[random.randint(0,2)]
        
        playerInput = input("\nEnter 'r' for rock, 'p' for paper and 's' for scissor: ")
        
        if playerInput == computerAction: # Tie
            self.printComputerChoice(computerAction)
            print("\nIt's a tie!")
            self.printScores()
            
        elif playerInput == 'r':
            if computerAction == 's': # player is rock and comp. is scissor
                self.printComputerChoice(computerAction)
                print("\nYou win!")
                self.playerPoints += 1
                self.printScores()
            else:
                self.printComputerChoice(computerAction)
                print("\nYou lose!") 
                self.computerPoints += 1
                self.printScores()

        elif playerInput == 'p':
            if computerAction == 'r': # player is paper and comp. is rock
                self.printComputerChoice(computerAction)
                print("\nYou win!")
                self.playerPoints += 1
                self.printScores()
            else:
                self.printComputerChoice(computerAction)
                print("\nYou lose!")
                self.computerPoints += 1
                self.printScores()
        elif playerInput == 's':
            if computerAction == 'p': # player is scissor and comp. is paper
                self.printComputerChoice(computerAction)
                print("\nYou win!")
                self.playerPoints += 1
                self.printScores()
            else:
                self.printComputerChoice(computerAction)
                print("\nYou lose!")
                self.computerPoints += 1  
                self.printScores()
        else:
            print("\nINVALID INPUT! TRY AGAIN!")
            self.playAgainstComputer(self.playerPoints, self.computerPoints) 
     
    def printScores(self):
        print("Your score: %d" %self.playerPoints)
        print("Computer's score: %d" %self.computerPoints) 
        print()               

    def printComputerChoice(self, move):
        print("Computer has chosen '%s'." %move)
