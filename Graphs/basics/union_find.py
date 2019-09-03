class DSU:
    def __init__(self, N):
        self.parent = list(range(N))

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)

        self.parent[x_set] = y_set


dsu = DSU(20)

stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]

n = len(stones)

for x, y in stones:
    dsu.union(x, y + 10)
    print(dsu.parent)

# print(dsu.parent)
#
# print( n- len({dsu.find(x) for x, y in stones}))


