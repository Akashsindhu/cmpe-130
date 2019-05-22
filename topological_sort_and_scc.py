from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def SortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.SortUtil(i, visited, stack)
        stack.append(v)

    def topological_Sort(self): 
        visited = [False]*self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.SortUtil(i, visited, stack)
        return self.graph

    def fillOrder(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)
        return stack

    def getTranspose(self):
        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def DFSUtil(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def SCC(self):    # strongly connected components
        stack = []
        visited = [False]*(self.V)

        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        gr = self.getTranspose()
        visited = [False]*(self.V)

        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)

        return self.graph