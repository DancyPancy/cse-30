# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            while True:
                try:
                    cshift = int(input('Input a shift for the Caesar Cypher:\n'))
                    break
                except ValueError:
                    print('\nYou must input an integer!')
            self.codec = CaesarCypher(delimiter=self.delimiter, shift=cshift)
        elif codec == 'huffman':
            self.codec = HuffmanCodes(delimiter = self.delimiter)
        binary = self.codec.encode(message + self.delimiter)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary

            # modify the image array and save new image
            encoded_img = self.mod_img(image)
            cv2.imwrite(fileout, encoded_img)
                   
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        # print(image) # for debugging      
        flag = True

        # convert into text
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            while True:
                try:
                    cshift = int(input('Input a shift for the Caesar Cypher:\n'))
                    break
                except ValueError:
                    print('\nYou must input an integer!')
            self.codec = CaesarCypher(delimiter=self.delimiter, shift=cshift)
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            # extract bits from the image array
            binary_data = self.extract_binary(image)
            # update the data attributes:
            self.text = self.codec.decode(binary_data)
            self.binary = binary_data[:len(self.text)*8]
        
    def mod_img(self, im_arr):
        new_im_arr = im_arr.copy()
        bit_id = 0
        # iterates through the pixels of an array and modifies the values with the encoded message
        for i, pix in np.ndenumerate(im_arr):
            if bit_id >= len(self.binary):
                break
            new_im_arr[i[0]][i[1]][i[2]] += int(self.binary[bit_id]) - (pix % 2)
            bit_id += 1

        return new_im_arr

    def extract_binary(self, im_arr):
        binary = ''
        # returns the last digit of the binary number of all the pixel color values in the image array
        for pix in np.nditer(im_arr):
            binary += str(pix % 2)

        return binary




    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()

