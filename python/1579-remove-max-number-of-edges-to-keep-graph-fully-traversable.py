class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.n = n

    def find(self, x):
      while x != self.parent[x]:
        self.parent[x] = self.parent[self.parent[x]]
        x = self.parent[x]
      return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        if self.rank[x] > self.rank[y]:
            self.rank[x] += self.rank[y]
            self.parent[y] = x
        else:
            self.rank[y] += self.rank[x]
            self.parent[x] = y

        self.n -= 1
        return 1

    def is_connected(self):
        return self.n == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)

        edges_required = 0

        # Perform union for edges of type 3, for both Alice and Bob
        for edge_type, u, v in edges:
            if edge_type == 3:
                edges_required += (alice.union(u, v) | bob.union(u, v))

        # Perform union for Alice if type = 1 and for Bob if type = 2
        for edge_type, u, v in edges:
            if edge_type == 1:
                edges_required += alice.union(u, v)
            elif edge_type == 2:
                edges_required += bob.union(u, v)

        # Check if the Graphs for Alice and Bob have n - 1 edges or is a single component
        if alice.is_connected() and bob.is_connected():
            return len(edges) - edges_required

        return -1
