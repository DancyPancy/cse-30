# codecs
import numpy as np

class Codec():
    
    def __init__(self, delimiter = '#'):
        self.name = 'binary'
        self.delimiter = delimiter

    # convert text or numbers into binary form    
    def encode(self, text):
        if type(text) == str:
            return ''.join([format(ord(i), "08b") for i in text])
        else:
            print('Format error')

    # convert binary data into text
    def decode(self, data):
        binary = []        
        for i in range(0, len(data), 8):
            byte = data[i: i+8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            text += chr(int(byte,2))       
        return text 

class CaesarCypher(Codec):

    def __init__(self, shift=3, delimiter = '#'):
        self.name = 'caesar'
        self.delimiter = delimiter  
        self.shift = shift    
        self.chars = 256      # total number of characters

    # convert text into binary form
    # your code should be similar to the corresponding code used for Codec
    def encode(self, text):
        if type(text) == str:
            return ''.join([format((ord(i)+self.shift) % 256, "08b") for i in text])
        else:
            print('Format error')

    
    # convert binary data into text
    # your code should be similar to the corresponding code used for Codec
    def decode(self, data):
        binary = []        
        for i in range(0, len(data), 8):
            byte = data[i: i+8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            e_num = int(byte, 2)
            if e_num < self.shift:
                text += chr(256 - (self.shift-e_num))
            else:
                text += chr(e_num-self.shift) 
        return text 

# a helper class used for class HuffmanCodes that implements a Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ''
        
class HuffmanCodes(Codec):
    
    def __init__(self,  delimiter = '#'):
        self.tree = None
        self.data = {}
        self.name = 'huffman'
        self.delimiter = delimiter

    # make a Huffman Tree    
    def make_tree(self, data):
        # make nodes
        nodes = []
        for char, freq in data.items():
            nodes.append(Node(freq, char))
            
        # assemble the nodes into a tree
        while len(nodes) > 1:
            # sort the current nodes by frequency
            nodes = sorted(nodes, key=lambda x: x.freq)

            # pick two nodes with the lowest frequencies
            left = nodes[0]
            right = nodes[1]

            # assign codes
            left.code = '0'
            right.code = '1'

            # combine the nodes into a tree
            root = Node(left.freq+right.freq, left.symbol+right.symbol,
                        left, right)

            # remove the two nodes and add their parent to the list of nodes
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(root)
        return nodes[0]

    # traverse a Huffman tree
    def get_whole_tree(self, node, val, dict):
        next_val = val + node.code
        if(node.left):
            self.get_whole_tree(node.left, next_val, dict)
        if(node.right):
            self.get_whole_tree(node.right, next_val, dict)
        if(not node.left and not node.right):
            dict[node.symbol] = next_val

    def decode_from_tree(self, node, data):
        if node.symbol == self.delimiter or len(data) == 0:
            return ''
        elif not node.left and not node.right:
            return node.symbol + self.decode_from_tree(self.tree, data)
        elif node.left and data[0] == node.left.code:
            return self.decode_from_tree(node.left, data[1:])
        elif node.right and data[0] == node.right.code:
            return self.decode_from_tree(node.right, data[1:])



    def create_dictionary(self, text):
        freq_dict = {}

        for char in text:
            try:
                freq_dict[char] += 1
            except KeyError:
                freq_dict[char] = 1
        
        return freq_dict

    # convert text into binary form
    def encode(self, text):
        data = ''
        self.tree = self.make_tree(self.create_dictionary(text))
        char_key = {}
        self.get_whole_tree(self.tree, '', char_key)

        for char in text:
            data += char_key[char]

        return data

    # convert binary data into text
    def decode(self, data):
        return self.decode_from_tree(self.tree, data)

# driver program for codec classes
if __name__ == '__main__':
    text = 'hello'
    # text = 'Casino Royale 10:30 Order martini'
    print('Original:', text)

    c = Codec()
    binary = c.encode(text + c.delimiter)
    print('Binary:',binary)
    data = c.decode(binary)
    print('Text:',data)

    cc = CaesarCypher()
    binary = cc.encode(text + cc.delimiter)
    print('Binary:',binary)
    data = cc.decode(binary)
    print('Text:',data)

    h = HuffmanCodes()
    binary = h.encode(text + h.delimiter)
    print('Binary:',binary)
    data = h.decode(binary)
    print('Text:',data)  
