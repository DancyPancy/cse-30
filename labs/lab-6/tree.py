# Create your own class BinaryTree that implements the Binary Tree ADT:

# 1. A constructor BinaryTree(rootObj)
# 2. insertLeft(newNode)
# 3. insertRight(newNode)
# 4. getRightChild()
# 5. getLeftChild()
# 6. getRootVal():
# 7. setRootVal(obj)
# 8. __str__()  should return a string in the following format 
#    root [left[[][]]][right[[][]]] where root, left, right are 
#    values of the root, its left child, and its right child 
#    respectively. If the children are missing, then they are 
#    represented as [], so if the root does not have children, 
#    then it should be shown as root[][].     

class BinaryTree:

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        if self.rightChild == None:
            return ''
        else:
            return self.rightChild

    def getLeftChild(self):
        if self.leftChild == None:
            return ''
        else:
            return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj

    def __str__(self):
        return f'{self.key}[{self.getLeftChild()}][{self.getRightChild()}]'

# driver code
if __name__ == '__main__':
    r = BinaryTree('a')
    print(r)
    r.insertLeft('b')
    r.insertRight('c')
    print(r)
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    print(r)
    print(r.getRootVal())
    print(r.getLeftChild())
    print(r.getRightChild())