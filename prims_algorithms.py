import sys # Library for INT_MAX 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 

    def minKey(self, key, mst):
        min = sys.maxint#initialize min value
        min_i = 0
        for v in range(self.V):
            if key[v] < min and mst[v] == False:
                min = key[v]
                min_i = v
        return min_i

    def primMST(self): 
        key = [sys.maxint] * self.V
        parent = [None]*self.V

        key[0]= 0
        mstSet = [False]*self.V
        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)

            mstSet[u] = True #shortest path tree

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        return self.graph