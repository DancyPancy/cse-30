def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[ 0]

def setRootVal(root,newVal):
    root[ 0] = newVal

def getLeftChild(root):
    return root[ 1]

def getRightChild(root):
    return root[ 2]

if __name__ == '__main__':
    data = [1,2,3,4,5,6,7]
    root = BinaryTree(data[ 0])
    insertLeft(root,data[ 1])
    insertRight(root,data[ 2])

    l = getLeftChild(root)
    insertLeft(l,data[ 3])
    insertRight(l,data[ 4])

    r = getRightChild(root)
    insertLeft(r,data[ 5])
    insertRight(r,data[ 6])

    print(getLeftChild(root))
    print(getRightChild(root))
    print(root)