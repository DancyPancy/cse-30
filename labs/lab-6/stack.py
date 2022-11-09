class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

if __name__ == '__main__':
    data = [1, 2, 3, 4]
    print(data)\

    s = Stack()
    for i in data:
            s.push(i)
    while not s.isEmpty():
            print(s.pop(), end=' ')