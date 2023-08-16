# Coordinates of the tic tac toe board will be represented using numbers 1 to 9 for now.
originalCoordinates = {
    '1' : '-',
    '2' : '-',
    '3' : '-',
    '4' : '-',
    '5' : '-',
    '6' : '-',
    '7' : '-',
    '8' : '-',
    '9' : '-',
}
# Winning Squares are all combination of 3 squares that can be crossed of for a player to win. They are represented as a list of Tuples. Each Tuple is a three element tuple.
winningSquares = [
    ('1', '2', '3'),
    ('4', '5', '6'),
    ('7', '8', '9'),
    ('1', '4', '7'),
    ('2', '5', '8'),
    ('3', '6', '9'),
    ('1', '5', '9'),
    ('3', '5', '7'),
]



class TicTacToe:
    
    def __init__(self) -> None:
        self.player1Points = 0
        self.player2Points = 0
        self.coordinates = originalCoordinates.copy()
        # isXTurn is to be used to check whether it is X's turn or not (O's).
        self.isXturn = True
        self.winningSquares = winningSquares
    
    
    def run(self):
        print("WELCOME TO TIC TAC TOE!\n")
  
        while True:
            options = input("\nEnter '1' to play a new game, '2' to play again and '3' to end the program. \nEnter your choice: ")

            if options == '1':
                self.player1Points = 0
                self.player2Points = 0
            
                
                self.play(self.player1Points, self.player2Points)
                print("Player 1 (X) score: %d" % self.player1Points)
                print("Player 2 (O) score: %d" % self.player2Points)
            
            elif options == '2':
            

                if self.player1Points == 0 and self.player2Points == 0:
                    print("\nYOU CAN'T PLAY AGAIN SINCE YOU HAVEN'T PLAYED YET. TRY '1' OR '3'.\n")
                else:
                    self.play(self.player1Points, self.player2Points)
                    print("Player 1 (X) score: %d" % self.player1Points)
                    print("Player 2 (O) score: %d" % self.player2Points)
            
            elif options == '3':
                print("\nTHANK YOU FOR PLAYING!")
                break
            else:
                print("\nINVALID COMMAND! TRY AGAIN!\n")  
            
            # Reset the value of all the squares
            self.coordinates = {
                '1' : '-',
                '2' : '-',
                '3' : '-',
                '4' : '-',
                '5' : '-',
                '6' : '-',
                '7' : '-',
                '8' : '-',
                '9' : '-',
            }
      
    
    
    # demo board means to identify whether to show an example board or not (for explaning how to play)
    def printBoard(self, demoBoard = False):
        if demoBoard:
            print('''
                 %s  | %s  | %s 
                ____|____|____
                 %s  | %s  | %s
                ____|____|____
                 %s  | %s  | %s
                    |    |
                '''% ('1','2','3','4','5','6','7','8','9'))
        else:
            coorValues = [i for i in self.coordinates.values()]

            print('''
                 %s  | %s  | %s 
                ____|____|____
                 %s  | %s  | %s
                ____|____|____
                 %s  | %s  | %s
                    |    |
                '''% (coorValues[0],
                        coorValues[1],
                        coorValues[2],
                        coorValues[3],
                        coorValues[4],
                        coorValues[5],
                        coorValues[6],
                        coorValues[7],
                        coorValues[8]
                        ))


    def checkForWin(self, playerLetter):
        # Assume it is initially false, means player hasn't been deemed winner yet.
        hasWon = False
        
        for squares in self.winningSquares:
            # if just one set of squares have the same values
            if self.areAllTheSame(squares[0], squares[1], squares[2], playerLetter):
                hasWon = True
                return hasWon
            
        return hasWon

    
    def areAllTheSame(self, sqr1, sqr2, sqr3, playerLetter): # player letter indicates either 'X' or 'O'
        
        # If any one the squares has a value of '-' instead of 'X' or 'O'
        if self.coordinates[sqr1] == '-' or self.coordinates[sqr2] == '-' or self.coordinates[sqr3] == '-':
            return False
        
        else:
            # If the value on ALL three squares is the same, means either 3 Xs or 3 Os.
            if self.coordinates[sqr1] == self.coordinates[sqr2] == self.coordinates[sqr3] == playerLetter:
                return True
            
            else:
                return False
            
    
    def play(self, player1points, player2points):
        # Reset the board squares everytime
                
        self.player1Points = player1points
        self.player2Points = player2points
    # numberOFFilledSpaces is defined to make keeping track of how many coordinates aren't filled yet easier.
        numberOfFilledSpaces = 9    
        
        print("\nThe coordinate system is labelled 1 to 9 starting from the top left position, across one row at a time and ending at the bottom right position. This is how it looks: \n")
        self.printBoard(demoBoard = True)

        
        # As long as all the coordinates haven't been filled yet.
        while numberOfFilledSpaces != 0:
            if self.isXturn:
                entry = input("Player 1 (X), Enter a number: ")
                
                # Check if the coordinate has been used or not 
                if self.coordinates[entry] == '-': 
                    self.coordinates[entry] = 'X'
                    self.isXturn = False
                    
                    numberOfFilledSpaces -= 1
                    self.printBoard()
                      
                    # check if player 1 won the game or not                   
                    if self.checkForWin('X'):
                        print('\nCONGRATULATIONS! PLAYER 1 IS THE WINNER!\n')

                        # Since there is a winner, we reset the values of the squares and update the scores.
                        self.player1Points += 1
                        # self.coordinates = originalCoordinates
                        self.isXturn = True

                        break
                                        
                else:
                    print("\nYOU CAN'T. That position has already been occupied. Choose another one.\n")
                    
                
            else:
                entry = input("Player 2 (O), Enter a number: ")
                
                # Check if the coordinate has been used or not 
                if self.coordinates[entry] == '-': 
                    self.coordinates[entry] = 'O'
                    self.isXturn = True
                    
                    numberOfFilledSpaces -= 1
                    self.printBoard()
                    
                    # check if player 2 won the game or not
                    if self.checkForWin('O'):
                        print('\nCONGRATULATIONS! PLAYER 2 IS THE WINNER!\n')

                        # Since there is a winner, we reset the values of the squares and update the scores.
                        self.player2Points += 1
                        # self.coordinates = originalCoordinates
                        self.isXturn = True

                        break                    
                    
                else:
                    print("\nYOU CAN'T. That position has already been occupied. Choose another one.\n")
         
        # Should all squares be used        
        else:
            print("\nAll squares have been used, play again?\n")
            # Check if there happens to be a winner (in case), else it is a tie.
            pass


