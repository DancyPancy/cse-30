''' DO NOT FORGET TO ADD COMMENTS '''

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
          

def clickButton(labels, pos, game):
    if game.is_valid_move(pos):

        temp = labels[pos].get()
        labels[pos].set(' ')
        gui.nametowidget(pos).configure(bg='grey')
        labels[game.emptytile].set(temp)
        gui.nametowidget(game.emptytile).configure(bg='#C8A2C8')

        game.update(int(labels[game.emptytile].get()))
        
    if game.is_solved():
        for tile in labels.keys():
            gui.nametowidget(tile).configure(bg='#90EE90')
    else:
        for tile in labels.keys():
            if tile == game.emptytile:
                backg = 'grey'
            else:
                backg = '#C8A2C8'
            gui.nametowidget(tile).configure(bg=backg)


def addButton(gui, labels, pos, game):
    if pos == game.emptytile:
        backg = 'grey'
    else:
        backg = '#C8A2C8'

    return Button(gui, textvariable=labels[pos], name=str(pos),
                        bg=backg, fg='white', font=font, height=3, width=5,
                        command = lambda : clickButton(labels, pos, game))

def makeButtons(gui, game):
    labels = {}
    buttons = []

    for i in range(len(game)):
        pos = i+1
        labels[pos] = StringVar(value=str(game.tiles.getVertex(pos).getValue()))
        button = addButton(gui, labels, pos, game)
        buttons.append(button)

    return buttons, labels

def arrangeButtons(size, buttons):
    for i in range(size):
        for j in range(size):
            buttons[i*size + j].grid(row=i, column=j, columnspan=1) 


def shuffle(gui, game, labels, count, num):

    if count < num:
        move_id = game.randmove()
        clickButton(labels, move_id, game)
        gui.after(10, lambda : shuffle(gui, game, labels, count+1, num))
    
if __name__ == '__main__':    

    # make tiles
    size = 4


    game = Fifteen(size)

    # make a window
    gui = Tk()
    gui.title("Slide Puzzle")

    # make font
    font = font.Font(family='Helveca', size='15', weight='bold')

    # make buttons
    buttons, labels = makeButtons(gui, game)
    arrangeButtons(size, buttons)

    shuffle_button = Button(gui, text='Shuffle', name='shuffle',
                        bg='grey', fg='white', font=font, height=1, width=5//2*size,
                        command = lambda : shuffle(gui, game, labels, 0, 15*size**2)
                        ).grid(row=size+1, columnspan=size)

    # update the window
    gui.mainloop()
