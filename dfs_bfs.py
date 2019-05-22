from collections import defaultdict 

class Graph:
	def __init__(self): 
		self.graph = defaultdict(list) 

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def hadPathTo(self, v, visited):
		visited[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				self.hadPathTo(i, visited) #keep tracking the vertex

	def dfs(self, v):
		#mark all vertices as not visited
		visited = [False]*(len(self.graph))

		self.hadPathTo(v, visited)
		return self.graph

	def bfs(self, v):
		queue = []
		visited = [False]*(len(self.graph))

		queue.append(v)
		visited[v] = True

		while queue:
			v = queue.pop(0)
			for i in self.graph[v]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True
		return self.graph
