import copy
import operator

class Vertex:

    def __init__(self, number):
        """Creates a list of inbound vertexes and one of outbound vertexes as well as ieterators for each one"""
        self.number = number
        self.edges = []
        #self.iterator = Iterator()
        self.colors = []
        self.isColored = 0

    def __str__(self):
        return str(self.number)

    def getNumber(self):
        return self.number

    def removeEdge(self, v):
        if v in self.edges:
            self.edges.remove(v)

    def addEdge(self, v):
        if v not in self.edges:
            self.edges.append(v)

    def removeColor(self, c):
        self.colors.remove(c)

    def addColor(self, c):
        self.color.append(c)


class Iterator:
    """Generic iterator which holds the current position and the maximim position"""
    def __init__(self):
        self.n = 0
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        if self.i<self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration


class UndirectedGraph:

    def __init__(self):
        self.__nrVertices = 0
        self.__nrEdges = 0
        self.__listVertices = []
        self.__listEdges = []

    def readFromFile(self, filename):
        with open(filename, "r") as f:
            lines=f.readlines()
            line = lines[0]
            line=line.split()
            self.__nrVertices = int(line[0])
            self.__nrEdges = int(line[1])
            lines.pop(0)

            for i in range(self.__nrVertices):
                v = Vertex(i)
                self.__listVertices.append(v)
                for j in range(self.__nrVertices):
                    v.addColor(j)
                v.removeColor(0)
                v.addColor(self.__nrVertices)

            for line in lines:
                line=line.split()
                v1=int(line[0])
                v2=int(line[1])
                self.__listVertices[v1].edges.append(self.__listVertices[v2])
                self.__listVertices[v2].edges.append(self.__listVertices[v1])
                tpl =(v1,v2)
                self.__listEdges.append(tpl)

            for i in self.__listVertices:
                i.iterator.n = len(i.edges)
        f.close()


    def removeEdge(self, v1, v2):
        if (v1,v2) in self.__listEdges:
            self.__listEdges.remove((v1,v2))

    def removeVertex(self,v):
        t=Vertex(-1)
        ok = False
        for i in self.__listVertices:
            if i.getNumber()==v:
                t=i
                ok = True
                break

        if ok==False:
            return False

        for i in self.__listVertices:
            self.removeEdge(v, i.getNumber())
            self.removeEdge(i.getNumber(), v)

        for i in self.__listVertices:
            i.removeEdge(t)

        self.__listVertices.remove(t)
        self.__nrVertices-=1

        return t


    def addEdge(self, v1, v2):
        self.__listEdges.append((v1,v2))

    def addVertex(self,v):

        for i in v.edges:
            self.addEdge(i.getNumber(),v.getNumber())

        for i in self.__listVertices:
            if i in v.edges:
                i.addEdge(v)

        self.__nrVertices+=1
        self.__listVertices.append(v)

    def getVertexx(self,v):
        return self.__listVertices[v]

    def printVerrtives(self):
        for i in self.__listVertices:
            print(i.number, "edges:")
            for j in i.edges:
                print(j.number)
            print(i.colors)
            print("\n")

    def printEdges(self):
        print(self.__listEdges)

    def getNrVertices(self):
        return self.__nrVertices

    def getNrEdges(self):
        return self.__nrEdges

    def verifyEdge(self, v1, v2):
        return (v1,v2) in self.__listEdges

    def getDegree(self,v):
        return len(self.__listVertices[v].edges)

    def getVertices(self):
        return self.__listVertices

    def getEdges(self):
        return self.__listEdges


G = UndirectedGraph()
G.readFromFile("example.txt")


def GCP(g, k, ub):

    if g.getNrVertices()==0:
        return k
    vertices = g.getVertices()
    for i in vertices:
        ok=1
        for j in i.colors:
            if j<ub:
                ok=0
        if ok==1:
            return ub

        v = vertices[0]
        colors=[]
        for i in v.colors:
            if i<ub:
                colors.append(i)
        for c in colors:
            for j in v.edges:
                if c in j.colors:
                    j.colors.remove(c)
            v=g.removeVertex(v.getNumber())
            ub=min(ub,GCP(G, max(k,c), ub))

            g.addVertex(v)
            for j in v.edges:
                if c not in j.colors:
                    j.colors.append(c)
        return ub


p = GCP(G, 0, G.getNrVertices()+1)
print(p)










