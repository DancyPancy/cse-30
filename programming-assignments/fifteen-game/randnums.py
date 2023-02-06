from random import choice

chars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, ' ']


if __name__ == '__main__':
    output = ''
    for i in range(1000): 
        output += str(choice(chars))
    
    print(output)