class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    data = ["Bill","David","Susan","Jane","Kent","Brad"]
    print(data)

    for i in data:
        q.enqueue(i)
    while not q.isEmpty():
        print(q.dequeue(), end=', ')