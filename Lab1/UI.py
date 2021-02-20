from Whatever.Repository import Repository

class UI:

    def __init__(self, repo):
        self.__repository = repo

    @staticmethod
    def printMenu():
        print("")
        print("1. Print graph")
        print("2. Load file")
        print("3. Get the number of vertices")
        print("4. Parse the set of vertices")
        print("5. Find if there is an edge")
        print("6. Get in degree of vertex")
        print("7. Get out degree of vertex")
        print("8. Parse the set of outbound edges of vertex")
        print("9. Parse the set of inbound edges of vertex")
        print("10. Get the cost of an edge ")
        print("11. Change the cost")
        print("12. Add edge")
        print("13. Remove edge")
        print("14. Add vertex")
        print("15. Remove vertex")
        print("16. Copy graph")
        print("17. Print copy graph")
        print("18. BFS start to end")
        print("19. Exit")
        print("")

    def printGraph(self):
        print(self.__repository.getGraph())

    def loadFromFileUI(self):
        filename = input("Enter file name: ")
        self.__repository.loadFromFile(filename)
        print("File loaded!")

    def getVerticesUI(self):
        print("The number of vertices is:" + str(self.__repository.getVerticesRepo()))

    def parseVerticesUI(self):
        print(self.__repository.parseVerticesRepo())

    def findEdgeUI(self):
        origin = int(input("Origin of the edge: "))
        target = int(input("Target of the edge: "))
        print(self.__repository.findEdgeRepo(origin, target))

    def getInDegreeUI(self):
        vertex = int(input("Number of vertex: "))
        print("The in degree is " + str(self.__repository.degreeVertexRepo(vertex)[0]))

    def getOutDegreeUI(self):
        vertex = int(input("Number of vertex: "))
        print("The out degree is " + str(self.__repository.degreeVertexRepo(vertex)[1]))

    def parseOutboundUI(self):
        vertex = int(input("Number of vertex: "))
        print(self.__repository.parseOutboundRepo(vertex))

    def parseInboundUI(self):
        vertex = int(input("Number of vertex: "))
        print(self.__repository.parseInboundRepo(vertex))

    def getCostUI(self):
        origin = int(input("Origin of the edge: "))
        target = int(input("Target of the edge: "))
        edge = (origin, target)
        if self.__repository.getCostRepo(edge) == None:
            print("The edge does not exist")
        else:
            print("Cost: " + str(self.__repository.getCostRepo(edge)))

    def changeCostUI(self):
        origin = int(input("Origin of the edge: "))
        target = int(input("Target of the edge: "))
        cost = int(input("New cost:"))
        edge = (origin, target)

        valid = self.__repository.setCostRepo(edge, cost)

        if valid == False:
            print("The edge does not exist")
        else:
            print("Cost changed!")

    def addEdgeUI(self):
        origin = int(input("Origin of the edge: "))
        target = int(input("Target of the edge: "))
        cost = int(input("New cost:"))

        valid = self.__repository.addEdgeRepo(origin, target, cost)

        if valid == False:
            print("The origin/target does not exist")

    def removeEdgeUI(self):
        origin = int(input("Origin of the edge: "))
        target = int(input("Target of the edge: "))
        edge = (origin, target)

        valid = str(self.__repository.removeEdgeRepo(edge))

        if valid == False:
            print("The edge does not exist")

    def addVertexUI(self):
        vertex = int(input("Number of vertex: "))

        valid = self.__repository.addVertexRepo(vertex)

        if valid == False:
            print("The vertex already exists")

    def removeVertexUI(self):
        vertex = int(input("Number of vertex: "))

        valid = self.__repository.removeVertexRepo(vertex)

        if valid == False:
            print("The vertex does not exist")


    def randomGraphUI(self):

        edge = int(input("Number of edges: "))
        self.__repository.randomGraphRepo(edge, cost=5)


    def BFSUI(self):
        start=int(input("Start vertex: "))
        end=int(input("End vertex: "))
        result = self.__repository.BFS(start, end)
        if result == None:
            print("No path")
        else:
            print("The lenght of the path is: "+str(len(result)-1))
            print(result)

    def copyGraphUI(self):
        self.__repository.getCopyGraph()
        print("Graph copied")

    def printCopyGraphUI(self):
        graph = self.__repository.getCopyGraph()
        print(graph)


    def Start(self):
        while True:
            try:
                self.printMenu()
                command = int(input("Enter an option: "))
                if command == 1:
                    self.printGraph()
                elif command == 2:
                    self.loadFromFileUI()
                elif command == 3:
                    self.getVerticesUI()
                elif command == 4:
                    self.parseVerticesUI()
                elif command == 5:
                    self.findEdgeUI()
                elif command == 6:
                    self.getInDegreeUI()
                elif command == 7:
                    self.getOutDegreeUI()
                elif command == 8:
                    self.parseOutboundUI()
                elif command == 9:
                    self.parseInboundUI()
                elif command == 10:
                    self.getCostUI()
                elif command == 11:
                    self.changeCostUI()
                elif command == 12:
                    self.addEdgeUI()
                elif command == 13:
                    self.removeEdgeUI()
                elif command == 14:
                    self.addVertexUI()
                elif command == 15:
                    self.removeVertexUI()
                elif command == 16:
                    self.copyGraphUI()
                elif command == 17:
                    self.printCopyGraphUI()
                elif command == 18:
                    self.BFSUI()
                elif command ==19:
                    break
                else:
                    print("Invalid option")

            except Exception as ex:
                print(ex)
