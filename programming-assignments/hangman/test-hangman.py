# author: Larissa Munishkina
# date: Mar 27, 2022
# file: test_hangman.py tests a hangman.py
# input: file 'dictionary_short.txt'
# output: possible assertion errors

import hangman
import sys
import io

dictionary_file = '/home/dancypancy/Dev/cse-30/pa-1/dictionary-short.txt'

if __name__ == '__main__':
    
    # test import_dictionary(filename)
    dict_standard = {2:['ad'],
                     3:['bat'],
                     4:['card'],
                     5:['dress'],
                     6:['engine'],
                     7:['T-shirt'],
                     8:['gasoline'],
                     9:['gathering'],
                     10:['evaluation'],
                     11:['self-esteem'],
                     12:['unemployment']}
    dictionary = hangman.import_dictionary(dictionary_file)
    assert dictionary == dict_standard

    # test get_game_options()
    output_standard = 'The word size is set to 4.\nYou have 4 lives.\n'
    hangman.input = lambda x:'4' # redirect input
    stdout = sys.stdout
    sys.stdout = io.StringIO()   # redirect stdout
    size, lives = hangman.get_game_options()
    output = sys.stdout.getvalue() 
    sys.stdout = stdout          # restore stdout
    assert size == 4
    assert lives == 4
    assert output == output_standard