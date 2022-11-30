# Code by: Jack Wong
# Date: Tue Nov 29 2022
# About: Hash table with chaining collision solution

class Hashtable:
    
    def __init__(self):
        self.table = [[] for i in range(5)]

    def __hash(self, key):
        hkey = len(key)
        for i in key:
            hkey += ord(i)
        return hkey % 5

    def __search(self, key):
        index = self.table[self.__hash(key)]
        pos = 0
        for i in index:
            if i[0] == key:
                return (pos, i)
            pos += 1
        return None

    def get(self, key):
        return self.__search(key)[1][1]


    def get_size(self):
        size = 0
        for i in self.table:
            size += len(i)
        return size

    def add(self, key, value):
        self.table[self.__hash(key)].append((key, value))

    def remove(self, key):
        item = self.__search(key)
        index = self.table[self.__hash(key)]
        if item != None:
            index.pop(item[0])

    def is_empty(self):
        return self.get_size() == 0


if __name__ == '__main__':
    data = ['goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', 'cow', 'cat']

    # make a hash table with key-value pairs: 'goat': 0, 'pig': 1, 'chicken': 2, etc. 
    h = Hashtable()
    for i in range(len(data)):
        h.add(data[i], i)       # the key is data[i], the value is i

    # print the hash table items
    for key in data:
        print(h.get(key))
    
    # test the method get() and if items in the hash table are correct
    for i in range(len(data)): 
        assert h.get(data[i]) == i 

    # test the method get_size()
    n = h.get_size() 
    assert n == 8 

    # test the method remove() and is_empty()
    for i in data: 
        h.remove(i) 
    print(h.is_empty()) 
    assert h.is_empty()
