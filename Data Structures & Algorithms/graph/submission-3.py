class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph or dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:

        visit = set()
        def dfs(node, target, visit):
            if node == target:
                return True

            if node in visit:
                return False
            visit.add(node)
            for n in self.graph[node]:
                if dfs(n, target, visit) == True:
                    return True
            visit.remove(node)
            return False
        
        return dfs(src,dst,visit)
            
