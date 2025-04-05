class Graph:
    def __init__(self,n):
        self.n=n
        self.adjacent= [[]*n for i in range(n)]
    def createedge(self,x,y):
        self.adjacent[x-1].append(y-1)
        self.adjacent[y-1].append(x-1)
    def bfs(self,source):
        visited=[False]*self.n
        result=[]
        q=[]
        q.append(source)
        visited[source]=True
        while len(q)>0:
            v=q.pop(0)
            result.append(v)
            for node in self.adjacent[v]:
                if visited[node]==False:
                    q.append(node)
                    visited[node]=True
        return result
#Bug 5 not coming



graph=Graph(6)
graph.createedge(1,5)
graph.createedge(5,3)
graph.createedge(3,4)
graph.createedge(4,1)
graph.createedge(1,2)
print(graph.adjacent)

print(graph.bfs(0))
