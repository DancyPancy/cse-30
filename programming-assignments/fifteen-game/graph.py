# Code by: Jack Wong
# Date: Wed Nov 30 2022
# About: Implements a graph ADT (the graph is undirected)

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = []
        self.value = key

    def addNeighbor(self, nbr_id):
        self.connectedTo.append(nbr_id)

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str(self.connectedTo)

    def getConnections(self):
        return self.connectedTo

    def getId(self):
        return self.id

    def getValue(self):
        return self.value

    def setValue(self, val):
        self.value = val
        return self.value
 
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        if key not in self.vertList.keys():
            self.numVertices += 1
            newVert = Vertex(key)
            self.vertList[newVert.id] = newVert
            return newVert
        else:
            print('addVertex: vertex with this key already exists')
            return None

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            print(f'getVertex: vertex with key "{key}" does not exist')
            return None

    def __contains__(self, n):
        return n in self.vertList.values()

    def addEdge(self, f, t):
        if f not in self.vertList:
            print(f'addEdge: vertex with key "{f}" does not exist')
            pass
        elif t not in self.vertList:
            print(f'addEdge: vertex with key "{t}" does not exist')
            pass
        else:
            self.vertList[f].addNeighbor(t)
            self.vertList[t].addNeighbor(f)
        
    def swapVal(self, f, t):
        if f not in self.vertList:
            print(f'swapVal: vertex with key "{f}" does not exist')
            pass
        elif t not in self.vertList:
            print(f'swapVal: vertex with key "{t}" does not exist')
            pass
        elif t in self.vertList[f].getConnections():
            temp = self.vertList[f].getValue()
            self.vertList[f].setValue(self.vertList[t].getValue())
            self.vertList[t].setValue(temp)
        else:
            print(f'swapVal: vertices "{f}" and "{t}" do not share an edge')

    def getVertices(self):
        return self.vertList.keys()

    def vertOfVal(self, val):
        for vert_id in self.getVertices():
            if self.vertList[vert_id].getValue() == val:
                return vert_id
        print(f'vertOfVal: vertex with value "{val}" does not exist')
        return None

    def __iter__(self):
        return iter(self.vertList.values())
    
    def breadth_first_search(self, s):
        pass
    
    def depth_first_search(self):
        pass
    
    def DFS(self, vid, path):
        pass

if __name__ == '__main__':

    g = Graph()
    for i in range(6):
        g.addVertex(i)
        
    g.addEdge(0,1)
    g.addEdge(0,5)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,0)
    g.addEdge(5,4)
    g.addEdge(5,2)

    for v in g:
        print(v)

    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False
        
    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]
    
    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]


