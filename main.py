class Graph:
    def __init__(self,n):
        self.n = n 
        self.adj = [[]*n for i in range(n)]

    def createedge(self,x,y): #x and y are cosidered to be nodes 
        self.adj[x-1].append(y-1) #creating an edge for an undirected graph 


        self.adj[y-1].append(x-1)

    def bfs(self,source):
        visited = [False]*self.n
        res = []

        queue = []
        queue.append(source)
        visited[source] = True

        while len(queue)>0:
            s=queue.pop()
            res.append(s)

            for node in self.adj[s]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True
        return res





graph = Graph(4)
graph.createedge(1,2)
graph.createedge(1,3)
graph.createedge(2,4)

print(graph.bfs(0))
print(graph)






       

