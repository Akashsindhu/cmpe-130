from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
  
    def __init__(self,vertices): 
        self.V = vertices #No. of vertices
        self.graph = [] # default dictionary
                                # to store graph

    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def findP(self, parent, i):
        if parent[i] == i:
            return i
        return self.findP(parent, i)

    def union(self, parent, rank, v, w):
        vroot = self.findP(parent, v)
        wroot = self.findP(parent, w)

        if rank[vroot] < rank[wroot]:
            parent[vroot] = wroot
        elif rank[wroot] < rank[vroot]:
            parent[wroot] = vroot

        else: #if their tank are same, make one as root and increase its rank by one
            parent[wroot] = vroot
            rank[vroot] += 1

    def KruskalMST(self):
        result = []

        i = 0 #sorted edges index
        j = 0 #index for result[]

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while j < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.findP(parent, u)
            y = self.findP(parent, v)

            if x != y:
                j = j + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        return self.graph