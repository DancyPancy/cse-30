# Code by: Jack Wong
# Date: Thu Nov 17 2022
# About: Stack class implements the Stack ADT

class Stack:
    
    def __init__(self):
        self.elements = [] 

    def isEmpty(self):
        return self.elements == []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if self.elements == []:
            return None
        else:
            return self.elements.pop()
    
    def peek(self):
        if self.elements == []:
            return None
        else:
            return self.elements[len(self.elements) - 1]

    def size(self):
        return len(self.elements)

# a driver program for class Stack

if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
