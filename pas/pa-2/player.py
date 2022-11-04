from random import choice
from sqlite3 import converters

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X

      def get_sign(self):
            # return an instance sign
            return self.sign

      def get_name(self):
            # return an instance name
            return self.name

      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            while True: 
                  cell = input(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:').upper()
                  if cell in valid_choices:
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              break
                  print('\nYou did not choose correctly.')
                        
                  

class AI(Player):
      
      def __init__(self, name, sign, board):
            super().__init__(name, sign)

      def choose(self, board):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            while True: 
                  cell = choice(valid_choices)
                  if cell in valid_choices:
                        if board.isempty(cell):
                              print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
                              print(cell)
                              board.set(cell, self.sign)
                              break

class MiniMax(AI):

      def __init__(self, name, sign, board):
            super().__init__(name, sign, board)

      def choose(self, board):
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            cell = MiniMax.minimax(self, board, True, True)
            print(cell)
            board.set(cell, self.sign)

      def __determine_sign(self, is_self):
            if is_self:
                  return self.sign
            else:
                  if self.sign == 'O':
                        return 'X'
                  else:
                        return 'O'

      def minimax(self, board, self_player, start):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']

        # check the base conditions
            if board.isdone():
                  # self is a winner
                  if board.get_winner() == self.sign:
                        return 1
                  # is a tie
                  elif board.get_winner() == '':
                        return 0
            # self is a loser (opponent is a winner)
                  else:
                        return -1
                
        # make a move (choose a cell) recursively
        # use the pseudocode given to you above to implement the missing code
            else:
                  min_score = float('inf')
                  max_score = float('-inf')

                  # iterate through all the cells
                  for i in range(board.get_size()**2):
                        cell = valid_choices[i]

                        # if cell is empty fill cell and calculate score
                        if board.isempty(cell):
                              board.set(cell, self.__determine_sign(self_player))

                              # recursive call
                              score = MiniMax.minimax(self, board, not self_player, False)
                              # print(self_player, 'score:', score)     # use for debugging

                              # replaces max score if new move is most optimal (best for self)
                              if self_player and max_score < score: 
                                    max_score = score
                                    move = cell

                              # replaces min score if new move is the least optimal for self (best for other)
                              elif not self_player and min_score > score:
                                    min_score = score
                                    move = cell

                              # reset board
                              board.set(cell, ' ')

                  # if top level returns optimal move
                  if start:
                        return move
                  
                  # if level is self's move, return maximum possible score (best case for self)
                  elif self_player:
                        return max_score

                  # if level is of other's move, return minimum possible score (best case for other)
                  else:
                        return min_score


class SmartAI(AI):

      def __init__(self, name, sign, board):
            super().__init__(name, sign, board)

      def __not_sign(self):
            if self.sign == 'X':
                  return 'O'
            else:
                  return 'X'

      def iterate_board(func):
            def wrap(self, board):
                  valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
                  move_found = False

                  # iterates over the board
                  for i in range(board.get_size()**2):
                        if not move_found:
                              cell = valid_choices[i]
                              if board.isempty(cell):
                                    move_found = func(self, cell, board)
                  return move_found
            return wrap

      @iterate_board
      def __check_wins(self, cell, board):
            # checks if move wins and keeps move if true
            board.set(cell, self.sign)
            if board.isdone():
                  return True

            # checks if move blocks win and block if true
            board.set(cell, self.__not_sign())
            if board.isdone():
                  board.set(cell, self.sign)
                  return True

            # no wins or blocked wins found
            board.set(cell, ' ')
            return False

      def __count_forks(self, sign, board):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            count = 0

            for i in range(board.get_size()**2):
                  cell = valid_choices[i]
                  if board.isempty(cell):
                        board.set(cell, sign)
                        if board.isdone():
                              count += 1
                        board.set(cell, ' ')
            return count

      @iterate_board
      def __check_forks(self, cell, board):

            # checks if move creats a fork and keeps move if true
            board.set(cell, self.sign)
            if self.__count_forks(self.sign, board) > 1:
                  return True

            # checks if move blocks a fork and keeps block if true
            board.set(cell, self.__not_sign())      
            if self.__count_forks(self.__not_sign, board) > 1:
                  board.set(cell, self.sign)
                  return True
            
            # no forks were found
            board.set(cell, ' ')
            return False



      def choose(self, board):
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            corners = [0, 2, 6, 8]

            move_found = self.__check_wins(board)
            
            if not move_found:
                  move_found = self.__check_forks(board)

            # if no optimal moves are found chooses center when avaliable
            if (not move_found) and board.isempty('B2'):
                  board.set('B2', self.sign)
                  
            # last case scenarios
            elif not move_found: 
                  # places sign in the opposite corner of an opponents sign
                  corners = {
                        'A1':'C3',
                        'C1':'A3',
                        'A3':'C1',
                        'C3':'A1'
                  }
                  for i in corners.keys():
                        if board.board[valid_choices.index(i)] == self.__not_sign() and board.isempty(corners[i]):
                              board.set(corners[i], self.sign)
                              move_found = True
                              break

                  # places in corners
                  if not move_found:
                        for i in corners.keys():
                              if board.isempty(corners[i]):
                                    board.set(corners[i], self.sign)
                                    move_found = True
                                    break

                  # places in sides
                  if not move_found:
                        sides = [1, 3, 5, 7]
                        for i in sides:
                              if board.isempty(valid_choices[i]):
                                    board.set(valid_choices[i], self.sign)
                                    move_found = True
                                    break

                        

                        

      