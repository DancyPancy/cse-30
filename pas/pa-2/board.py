class Board:

      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = ' '
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ''

      def get_size(self): 
             # optional, return the board size (an instance size)
             return self.size

      def get_winner(self):
            # return the winner's sign O or X (an instance winner)   
            return self.winner

      def __cell_index(self, cell):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            return valid_choices.index(cell)

      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            self.board[self.__cell_index(cell)] = sign
            
      def isempty(self, cell):
            # return True if the cell is empty (not marked with X or O)
            return self.board[self.__cell_index(cell)] == ' '
            
      def isdone(self):
            done = False
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X

            #check row 1
            if (self.board[0] != ' ') and (self.board[0] == self.board[1] == self.board[2]):
                  done = True
                  self.winner = self.board[0]

            #check row 2
            elif (self.board[3] != ' ') and (self.board[3] == self.board[4] == self.board[5]):
                  done = True
                  self.winner = self.board[3]
            
            #check row 3
            elif (self.board[6] != ' ') and (self.board[6] == self.board[7] == self.board[8]):
                  done = True
                  self.winner = self.board[6]

            #check column 1
            elif (self.board[0] != ' ') and (self.board[0] == self.board[3] == self.board[6]):
                  done = True
                  self.winner = self.board[0]

            #check column 2
            elif (self.board[1] != ' ') and (self.board[1] == self.board[4] == self.board[7]):
                  done = True
                  self.winner = self.board[1]
            
            #check column 3
            elif (self.board[2] != ' ') and (self.board[2] == self.board[5] == self.board[8]):
                  done = True
                  self.winner = self.board[2]

            #check diagonal 1
            elif (self.board[0] != ' ') and (self.board[0] == self.board[4] == self.board[8]):
                  done = True
                  self.winner = self.board[0]

            #check diagonal 2
            elif (self.board[2] != ' ') and (self.board[2] == self.board[4] == self.board[6]):
                  done = True
                  self.winner = self.board[6]

            #check if board is full
            elif ' ' not in self.board:
                  done = True
                  self.winner = ''

            return done
      def show(self):
            # draw the board
            # need to complete the code
            print('\n   A   B   C') 
            print(' +---+---+---+')
            print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
            print(' +---+---+---+')
            print('2| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
            print(' +---+---+---+')

