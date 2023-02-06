''' DO NOT FORGET TO ADD COMMENTS '''

import numpy as np
from random import choice
from graph import Graph

class Fifteen:
    
    def __init__(self, size = 4):
        g = Graph()
        for key in range(1, size**2+1):
            g.addVertex(key)

            # iterates through all the other generated tiles and adds an edge if applicable
            for tile in [i for i in list(g.getVertices()) if i != key]:

                # checks if the two tiles are horizontal neighbors and adds edge
                # mod operation checks if a new row has started and does not add the edge if true
                if (abs(key - tile) == 1) and (tile % size != 0):
                    g.addEdge(key, tile)
                
                # checks if the two tiles are vertical neighbors and adds edge
                elif abs(key - tile) == size:
                    g.addEdge(key, tile)

        # sets the last tile to the empty tile
        g.getVertex(size**2).setValue(' ')

        self.tiles = g
        self.size = size
        self.emptytile = size**2
        self.solved = [i for i in range(1, size**2)] + [' ']

    def update(self, move):
        move_id = self.tiles.vertOfVal(move)
        if self.is_valid_move(move_id):
            # swap the values of move tile and empty tile
            self.transpose(move_id, self.emptytile)
            self.emptytile = move_id
        else:
            print(f'update: {move} is not a valid move') 
        
    def transpose(self, i, j):
        self.tiles.swapVal(i, j)

    def randmove(self):
        return choice(self.tiles.getVertex(self.emptytile).getConnections())

    def shuffle(self, steps=100):
        for i in range(steps):
            self.update(self.randmove())
        
    def is_valid_move(self, move_id):
        # checks if the move tile and empty tile are neighbors 
        if move_id in self.tiles.getVertex(self.emptytile).getConnections():
            return True
        else:
            return False

    def is_solved(self):
        # iterates over all tiles
        for idx in range(self.size**2):
            # checks if the value of the tile is the same as the value of that position in solved
            if self.tiles.getVertex(idx+1).getValue() != self.solved[idx]:
                return False
        return True

    def draw(self):
        output = ''
        for row in range(self.size):
            for j in range(self.size):
                output += '+---'
            output += '+\n'
            for col in range(1, self.size+1):
                output += f'|{(" " + str(self.tiles.getVertex(row*self.size + col).getValue()))[-2:]} '
            output += '|\n'
        
        # bottom line
        for j in range(self.size):
            output += '+---'
        output += '+'

        print(output)

    def __str__(self):
        output = ''
        for tile in range(1, self.size**2+1):
            # adds value of tile to output string (if value is one digit adds a space beforehand)
            output += (' ' + str(self.tiles.getVertex(tile).getValue()))[-2:] + ' '

            # adds a new line if tile is the last in its row
            if tile % self.size == 0:
                output += '\n'
        
        return output

    def get_values(self):
        output = []
        for i in range(1, self.size**2+1):
            output.append(self.tiles.getVertex(i).getValue())
        return output
    
    def __len__(self):
        return self.size**2

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    '''You should be able to play the game if you uncomment the code below'''

    game = Fifteen(4)
    # game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        # if game.is_solved():
        #     break
    print('Game over!')

    
    
        
