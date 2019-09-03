from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:
    # Constructor
    def __init__(self, vertices):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.stack = []
        self.V = vertices

        # function to add an edge to graph

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_util(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topological_util(i, visited)

        self.stack.insert(0, v)

    def topological(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                self.topological_util(i, visited)

        print(self.stack)


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Following is a Topological Sort of the given graph")
g.topological()
