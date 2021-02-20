from Whatever.Graph import Graph

class Repository:

    def __init__(self):
        self.__graph = None

    def loadFromFile(self, fileName):
        file = open(fileName, "r")
        text = file.read()
        text = text.split('\n')
        line = text[0]
        line = line.split(" ")
        del text[0]
        try:
            n = int(line[0])
            m = int(line[1])
        except:
            raise ValueError("Invalid file input!")
        self.__graph = Graph(n)
        for i in range(m):
            line = text[i].split(" ")
            if len(line) != 3:
                raise ValueError("Invalid file input")
            origin = int(line[0])
            target = int(line[1])
            cost = int(line[2])
            if origin >= n or target >= n:
                raise ValueError("Invalid file input!")

            self.__graph.addEdge(origin, target, cost)


    def findEdgeRepo(self, origin, target):
        return self.__graph.findEdge((origin, target))

    def getVerticesRepo(self):
        return self.__graph.getVertices()

    def degreeVertexRepo(self, vertex):
        return self.__graph.degreeVertex(vertex)


    def parseVerticesRepo(self):
        return self.__graph.parseVertices()

    def parseInboundRepo(self, vertex):
        return self.__graph.parseInbound(vertex)

    def parseOutboundRepo(self, vertex):
        return self.__graph.parseOutbound(vertex)

    def getCostRepo(self, edge):
        return self.__graph.getCost(edge)

    def setCostRepo(self, edge, newCost):
        return self.__graph.setCost(edge, newCost)

    def addVertexRepo(self, vertex):
        return self.__graph.addVertex(vertex)

    def removeVertexRepo(self, vertex):
        return self.__graph.removeVertex(vertex)

    def addEdgeRepo(self, origin, target, cost):
        return self.__graph.addEdge(origin, target, cost)

    def removeEdgeRepo(self, edge):
        return self.__graph.removeEdge(edge)

    def copyGraph(self):
        return self.__graph.copyGraph()

    def getGraph(self):
        return self.__graph

    def randomGraphRepo(self,edge, cost=5):
        return self.__graph.randomGraph(edge, cost=5)

    def getCopyGraph(self):
        self.__copyGraph = self.__graph.copy()

    def BFS(self, start, end):
        #return self.__graph.bfs(start, end)
        dest= self.__graph.bfs(start, end)
        if dest == None:
            return None
        path = []
        crawl = end
        while dest[crawl] !=-1:
            path.append(crawl)
            crawl = dest[crawl]
        path.append(start)
        path.reverse()
        return path













