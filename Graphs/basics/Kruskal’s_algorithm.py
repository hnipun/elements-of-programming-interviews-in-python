from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

        # A utility function to find set of an element i
        # (uses path compression technique)

    def find(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])

        # A function that does union of two sets of x and y

        # (uses union by rank)

    def union(self, parent,x, y):
        x_set = self.find(parent,x)
        y_set = self.find(parent,y)

        parent[x_set] = y_set

    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):

        self.graph = sorted(self.graph, key=lambda item: item[2])

        result = []
        parent = [-1] * (self.V)

        i, e = 0,0

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e+1
                result.append([u,v,w])
                self.union(parent,x,y)

                # print the contents of result[] to display the built MST
        print ("Following are the edges in the constructed MST")
        for u, v, weight in result:
                # print str(u) + " -- " + str(v) + " == " + str(weight)
            print("%d -- %d == %d" % (u, v, weight))


# Driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()