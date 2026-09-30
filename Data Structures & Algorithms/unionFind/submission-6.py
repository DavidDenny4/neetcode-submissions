class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.comp_count = n

        for i in range(n):
            self.parent[i + 1] = n
            self.rank[i + 1] = 0

    def find(self, x: int) -> int:
        print(f"the current parent is {self.parent}")
        print(f"the value of x is {x}")
        p = self.parent[x]
        while p != self.parent[p]:
            parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        x_parent, y_parent = self.find(x), self.find(y)

        if x_parent == y_parent:
            return False
        
        if rank[x_parent] > rank[y_parent]:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += 1
        elif rank[x_parent] < rank[y_parent]:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1
        else:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += 1
        
        self.comp_count -= 1
        return True

    def getNumComponents(self) -> int:
        return self.comp_count
