# assignment: programming assignment 1
# author: Jack Wong
# date: October 4, 2022
# file: hangman.py is a program that (put the description of the program)
# input: enter the length of the word you want to guess and the number of lives 
#        that you want to have and start inputing letter guesses for the hidden word
# output: outputs if you guess a letter correctly, incorrectly, 
#         and outputs game state on a win or a loss

from calendar import c
from importlib.machinery import WindowsRegistryFinder
from random import choice, random
import string

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    dictionary = {}
    max_size = 12
    w_list = open(filename, 'r')
    try:
        while True:
            word = w_list.readline().strip()
            w_size = len(word)
            if w_size == 0:
                break
            elif w_size > max_size:
                w_size = max_size
            try:
                dictionary[w_size].append(word)
            except KeyError:
                dictionary[w_size] = [word]
    except Exception:
        raise TypeError('file type unsupported')
    return dictionary
    
# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    keys = dictionary.keys()
    for key in keys:
        print(f'{key}: {dictionary.get(key)}')

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :   
    lives = 5
    size = 0
    try:
        size = int(input('Please choose a size of a word to be guessed [3 - 12, default any size]: '))
    except ValueError:
        pass
    finally:
        if size >= 3 and size <= 12:
            print(f'The word size is set to {size}.')
        else:
            size = 0
            print('A dictionary word of any size will be chosen.')
    try:
        usr_lives = int(input('Please choose a number of lives [1 - 10, default 5]: '))
        if usr_lives >= 1 & usr_lives <= 10:
            lives = usr_lives
    except ValueError:
        pass
    finally:
        print(f'You have {lives} lives.')
    return (size, lives)

# returns the amount of lives represented by 'O' for lives 'X' for lost lives
def print_lives(lives: int , lives_left: int):
    return 'X' * (lives - lives_left) + 'O' * (lives_left)

# returns the representation of the current state of the guessed word 
def update_word(current_word: list, hidden_word: string, char: string):
    check = char.upper()
    temp_word = hidden_word
    while check in temp_word:
        index = temp_word.rindex(check)
        current_word[index] = check
        temp_word = temp_word[:index] + temp_word[index+1:]


# returns a string containing the display of the state of the current game 
def print_game_state(letters_chosen, current_word, lives, lives_left):
    return f"Letters chosen: {', '.join(letters_chosen)}\n{' '.join(current_word)}    lives: {str(lives_left)}   {print_lives(lives, lives_left)}"


# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print a game introduction
    print('Welcome to the Hangman Game!')

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    game_over = False 

    while not game_over:
        # set up game options (the word size and number of lives)
        size, lives = get_game_options()

        # select a word from a dictionary (according to the game options)
        if size != 0:
            hidden_word = choice(dictionary[size]).upper()
        else:
            hidden_word = choice(choice(list(dictionary.values()))).upper()
    
        # INITIALIZE FOR GAME LOOP   (INNER PROGRAM LOOP)
        letters_chosen = []
        lives_left = lives
        current_word = ["__"]*len(hidden_word)
        update_word(current_word, hidden_word, '-')

        # START GAME LOOP (INNTER PROGRAM LOOP)
        end = False
        while not end:
            # format and print the game interface:
            # Letters chosen: E, S, P                list of chosen letters
            # __ P P __ E    lives: 4   XOOOO        hidden word and lives
            print(print_game_state(letters_chosen, current_word, lives, lives_left))
        
            # End game conditions end loop
            if lives_left == 0:
                print(f'You lost! The word is {hidden_word}')
                end = True
            elif '__' not in current_word:
                print(f'Congratulations!!! You won! The word is {hidden_word}')
                end = True

            # Runs the new guess loop if game is still going
            else:
                valid_input = False
                while not valid_input:
                    # ask the user to guess a letter
                    guess = input('Please chose a new letter > ').upper()
                    
                    # update the list of chosen letters
                    if len(guess) != 1 or not guess.isalpha():
                        print('You did not enter a letter!')
                    elif guess in letters_chosen:
                        print('You have already chosen this letter.')

                    # if the letter is correct update the hidden word,
                    # else update the number of lives,
                    # and print interactive messages
                    elif guess in hidden_word:
                        valid_input = True 
                        letters_chosen.append(guess)
                        update_word(current_word, hidden_word, guess)
                        print('You guessed right!')
                    else:
                        valid_input = True
                        lives_left -= 1
                        letters_chosen.append(guess)
                        print('You guessed wrong, you lost one life.')

        # END MAIN LOOP (OUTER PROGRAM LOOP)

        # ask if the user wants to continue playing, 
        # if yes start a new game, otherwise terminate the program
        if input('Would you like to play again [Y/N]? ').upper() != 'Y':
            print('Goodbye!')
            game_over = True
