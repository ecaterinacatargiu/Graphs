"""Design and implement an abstract data type directed graph and a function (either a member function or an external one, as your choice) for reading a directed graph from a text file.
The vertices will be specified as integers from 0 to n-1, where n is the number of vertices.
Edges may be specified either by the two endpoints (that is, by the source and target), or by some abstract data type Edge_id (that data type may be a pointer or reference to the edge representation, but without exposing the implementation details of the graph).
Additionally, create a map that associates to an edge an integer value (for instance, a cost).

Required operations:

1.get the number of vertices;
2.parse (iterate) the set of vertices;
3.given two vertices, find out whether there is an edge from the first one to the second one, and retrieve the Edge_id if there is an edge (the latter is not required if an edge is represented simply as a pair of vertex identifiers);
4.get the in degree and the out degree of a specified vertex;
5.parse (iterate) the set of outbound edges of a specified vertex (that is, provide an iterator). For each outbound edge, the iterator shall provide the Edge_id of the curren edge (or the target vertex, if no Edge_id is used).
6.parse the set of inbound edges of a specified vertex (as above);
7.get the endpoints of an edge specified by an Edge_id (if applicable);
8.retrieve or modify the information (the integer) attached to a specified edge.
9.The graph shall be modifiable: it shall be possible to add and remove an edge, and to add and remove a vertex. Think about what should happen with the properties of existing edges and with the identification of remaining vertices. You may use an abstract Vertex_id instead of an int in order to identify vertices; in this case, provide a way of iterating the vertices of the graph.
10.The graph shall be copyable, that is, it should be possible to make an exact copy of a graph, so that the original can be then modified independently of its copy. Think about the desirable behaviour of an Edge_property attached to the original graph, when a copy is made."""

from random import randint

class Graph:

    def __init__(self, nrVertices):
        self.__nrVertices = nrVertices
        self.__in = {}
        self.__out = {}
        self.__cost = {}

        for i in range(nrVertices):
            self.__out[i] = []
            self.__in[i] = []

    def __str__(self):
        m = "The number of vertices is: "+ str(self.__nrVertices)+"\n"
        m+="The edges of the graph are: "+"\n"
        for i in self.__cost.keys():
            m+=str(i)+"->"+str(self.__cost[i])+"\n"
        return m

    def getVertices(self):
        """This function returns the number of vertices"""
        return self.__nrVertices

    def parseVertices(self):
        """This function parses the vertices and returns an iterator containing all the existing vertices"""
        return self.__out.keys()

    def findEdge(self, edge):
        """This function finds(returns) a given edge, if it exists and none otherwise"""
        if edge in self.__cost.keys():
            return True
        return False

    def degreeVertex(self, vertex):
        """Returns the in and out degree of a given vertex if the vertex exists, and none otherwise"""
        if vertex in self.__in.keys():
            return [len(self.__in[vertex]), len(self.__out[vertex])]
        return None

    def parseInbound(self, vertex):
        """Returns an iterator with the inbound vertices of a given vertex"""
        if vertex in self.__out.keys():
            return self.__in[vertex]

    def parseOutbound(self, vertex):
        """Returns an iterator of the outbound vertices of a given vertex"""
        if vertex in self.__in.keys():
            return self.__out[vertex]

    def getCost(self, edge):
        """Returns the cost of a given edge"""
        if edge in self.__cost.keys():
            return self.__cost[edge]
        return None

    def setCost(self, edge, newCost):
        """Modifies the cost of a given edge and returns true if the cost is modified and 0 otherwise"""
        if edge in self.__cost.keys():
            self.__cost[edge] = newCost
            return True
        return False

    def addEdge(self, origin, target, cost):
        """This function adds an edge in to the graph.
        Input: origin of the edge, tharge of the edge and cost of the edge
        Output: true if the edge is added and false otherwise"""

        if origin not in self.__in.keys():
            return False
        if target not in self.__out.keys():
            return False
        if(origin,target) not in self.__cost.keys():
            self.__out[origin].append(target)
            self.__in[target].append(origin)
            self.__cost[(origin,target)] = cost
            return True
        return False

    def removeEdge(self, edge):
        """Removes an edge from the graph.
        Input: the edge that will be deleted
        Output: true if the edge is deleted and false otherwise"""
        origin = edge[0]
        target = edge[1]
        if edge not in self.__cost.keys():
            return False
        self.__out[origin].remove(target)
        self.__in[target].remove(origin)
        del self.__cost[edge]
        return True

    def addVertex(self, vertex):
        """Adds a new vertex to the graph.
        Input: the vertex that will be added
        Output: true if the vertex is added and false otherwise"""
        if vertex in self.__in.keys():
            return False
        self.__nrVertices+=1
        self.__in[vertex] = []
        self.__out[vertex] = []
        return True

    def removeVertex(self, vertex):
        """Removes a given vertex from the graph
        Input: vertex
        Output: true if the vertex is deleted alse otherwise"""

        v = self.getVertices()
        if vertex > self.getVertices() - 1:
            return False
        if vertex == self.getVertices() - 1:
            del self.__in[self.getVertices()- 1]
            del self.__out[self.getVertices() - 1]
            for key in list(self.__cost.keys()):
                if vertex in key:
                    del self.__cost[key]
            for value in self.__in.values():
                if len(value) > 0:
                    i = 0
                    while i < len(value):
                        if value[i] == vertex:
                            value.pop(i)
                            i -= 1
                        i += 1
            for value in self.__out.values():
                if len(value) > 0:
                    i = 0
                    while i < len(value):
                        if value[i] == vertex:
                            value.pop(i)
                            i -= 1
                        i += 1
            v -= 1
        else:
            edgesIn = self.__in[self.getVertices() - 1]
            edgesOut = self.__out[self.getVertices() - 1]
            del self.__out[self.getVertices() - 1]
            del self.__in[self.getVertices() - 1]
            del self.__in[vertex]
            del self.__out[vertex]
            self.__in[vertex] = edgesIn
            self.__out[vertex] = edgesOut
            for key in self.__in.keys():
                if vertex in self.__in[key]:
                    self.__in[key].remove(vertex)
                if self.getVertices() - 1 in self.__in[key]:
                    self.__in[key].remove(self.getVertices() - 1)
                    self.__in[key].append(vertex)
            for key in self.__out.keys():
                if vertex in self.__out[key]:
                    self.__out[key].remove(vertex)
                if self.getVertices() - 1 in self.__out[key]:
                    self.__out[key].remove(self.getVertices() - 1)
                    self.__out[key].append(vertex)
            for key in range(0, self.getVertices() - 1):
                if (key, vertex) in self.__cost.keys():
                    del self.__cost[(key, vertex)]
                if (vertex, key) in self.__cost.keys():
                    del self.__cost[(vertex, key)]
                if (key, self.getVertices() - 1) in self.__cost.keys():
                    cost = self.__cost[(key, self.getVertices() - 1)]
                    del self.__cost[(key, self.getVertices() - 1)]
                    self.__cost[(key, vertex)] = cost
                if (self.getVertices() - 1, key) in self.__cost.keys():
                    cost = self.__cost[(self.getVertices() - 1, key)]
                    del self.__cost[(self.getVertices() - 1, key)]
                    self.__cost[(vertex, key)] = cost
            v -= 1


    def copyGraph(self):
        """Creates a copy of the graph"""
        g = Graph(self.__nrVertices)
        for edge in self.__cost.keys():
            g.addEdge(edge[0],edge[1], self.__cost[edge])
        return g


    def randomGraph(self, edges, cost=5):
        if edges > self.getVertices() ** 2:
            raise ValueError
        gen = 0
        while gen < edges:
            x = self.addEdge(randint(0, self.getVertices() - 1), randint(0, self.getVertices() - 1), randint(-cost, cost))
            if x == True:
                gen += 1


    def bfs(self,start,end):
        visited = [False] * self.__nrVertices
        path = [-1] * self.__nrVertices
        dist = [0] * self.__nrVertices
        queue = []
        queue.append(start)
        visited[start]=True
        dist[start]=0
        while len(queue)!=0:
            v = queue.pop(0)
            for i in self.__out[v]:
                if visited[i]==False:
                    queue.append(i)
                    dist[i]=dist[v]+1
                    path[i]= v
                    visited[i]=True
                if i==end:
                    return path
        return None