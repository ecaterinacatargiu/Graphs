class DoubleDictGraph:
    """A directed graph, represented as two disctionaries/maps,
    one from each vertex to the set of outbound neighbours,
    the other from each vertex to the set of inbound neighbours"""

    def __init__(self, n):
        """Creates a graph with n vertices (numbered from 0 to n-1)
        and no edges"""
        self._dictOut = {}
        self._dictIn = {}
        for i in range(n):
            self._dictOut[i] = []
            self._dictIn[i] = []

    def parseX(self):
        """Returns an iterable containing all the vertices"""
        return self._dictOut.keys()

    def parseNout(self, x):
        """Returns an iterable containing the outbound neighbours of x"""
        return self._dictOut[x]

    def isEdge(self, x, y):
        """Returns True if there is an edge from x to y, False otherwise"""
        return y in self._dictOut[x]

    def addEdge(self, x, y):
        """Adds an edge from x to y.
        Precondition: there is no edge from x to y"""

        self._dictOut[x].append(y)
        self._dictIn[y].append(x)

    def timeActivity(self):
        """
        returns the earliest and the latest starting time for each activity and the critical activities
        """
        earlyStart = dict()
        earlyFinish = dict()

        sorted = self.DAG()
        duration = {0: 5, 1: 3, 2: 1, 3: 0}

        for node in sorted:
            earlyStart[node] = 0
            for i in self.parseNout(node):
                earlyStart[node] = max(earlyStart[node], earlyStart[i] + duration[i])
            earlyFinish[node] = earlyStart[node] + duration[node]

        totalTime = 0
        for x in self.parseX():
            if earlyFinish[x] > totalTime:
                totalTime = earlyFinish[x]

        lateStart = dict()
        lateFinish = dict()

        for node in reversed(sorted):
            lateFinish[node] = totalTime
            for y in self.parseNout(node):
                lateFinish[node] = min(lateFinish[node], lateStart[y])
            lateStart[node] = lateFinish[node] - duration[node]

        critical = []
        for x in self.parseX():
            if lateStart[x] == earlyStart[x] and lateFinish[x] == earlyFinish[x]:
                critical.append(x)

        return {"earliest start ": earlyStart, "earliest finish ": earlyFinish, "total time": totalTime,
                "latest start": lateStart, "late finish": lateFinish, "critical": critical}



    def vad(self):
       for elemes in self._dictOut:
           print(elemes,self._dictOut[elemes])


def populateTheGraph(DoubleDictGraph):
    f=open("4.txt", "r")
    line = f.readline().strip()
    attrs = line.split(" ")
    n = int(attrs[0])
    m = int(attrs[1])
    graf = DoubleDictGraph(n)
    line = f.readline().strip()
    while m != 0:
        attrs = line.split(" ")
        v1 = int(attrs[0])
        v2 = int(attrs[1])
        graf.addEdge(v1,v2)
        line = f.readline().strip()
        m = m - 1
    f.close()
    return graf


graph=populateTheGraph(DoubleDictGraph)


def topoSortDFS(graph, x, sorted, fullyProcessed, inProcess):
    inProcess.add(x)
    for y in graph.parseNout(x):
        if y in inProcess:
            return False
        elif y not in fullyProcessed:
            ok = topoSortDFS(graph, y, sorted, fullyProcessed, inProcess)
            if ok == False:
                return False
    inProcess.remove(x)
    sorted.append(x)
    fullyProcessed.add(x)
    return True

def Tarjan(graph, start):
    sorted = []
    fullyProcessed = set()
    inProcess = set()
    for x in graph.parseNout(start):
        if x not in fullyProcessed:
            ok = topoSortDFS(graph, x, sorted, fullyProcessed, inProcess)
            if ok == False:
                sorted = []
                return sorted
    sorted.append(start)
    sorted.reverse()
    return sorted



l=Tarjan(graph,0)

if l == []:
    print("The graph is not a DAG!\n")
else:
    print("The graph is a DAG!")
    print(l)

graph.timeActivity()