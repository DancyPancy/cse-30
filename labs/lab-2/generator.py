
from math import perm


def permute(items_original):
    if (len(items_original) == 1) :
        yield items_original
    else:
        for items_permuted in permute(items_original[1:]):
            for i in range(len(items_original)):
                yield items_permuted[:i] + items_original[0:1] + items_permuted[i:]

dictionary_file = 'dictionary.txt'

def anagram(word, dictionary):
    words = list(map(lambda x: x.strip(), open(dictionary, 'r').read().splitlines()))
    for perm in permute(word):
        if perm in words:
            yield perm

if __name__ == '__main__':
    for word in {gram for gram in anagram('name', dictionary_file)}:
        print(word)