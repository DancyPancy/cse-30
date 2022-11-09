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

def is_palindrome(s):
    q = Queue()
    for char in s:  # this line should be present in your code only once!!!
        q.enqueue(char)

    # I assumed that I was not able to do any checking while the queue was being filled,
    # unlike the implementation for balanced parantheses on the colab, hence the inefficient solution
    while q.size() > 1:

        # rotate the items in queue until the last and first items are at the front of the queue
        for i in range(q.size()-1):
            q.enqueue(q.dequeue())

        # check if the last and first items are equivalent if not return False
        last = q.dequeue()
        first = q.dequeue()
        if first != last:
            return False
    
    return True

if __name__ == '__main__':
    print(is_palindrome("hello"))
    print(is_palindrome("madam"))