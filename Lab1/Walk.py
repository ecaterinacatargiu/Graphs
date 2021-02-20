from Whatever.Graph import Graph


def lowestWalkMatrix(self, D, W):
    """
    This function will compute the all shortest path matrix
    :return:
    """
    D2 = []
    for i in range(0, self.__numberOfVertices):
        D2.append([])
        for j in range(0, self.__numberOfVertices):
            D2[i].append(D[i][j])

    for i in range(0, self.__numberOfVertices):
        for j in range(0, self.__numberOfVertices):
            D[i][j] = 1000000
            position = -1
            for k in range(0, self.__numberOfVertices):
                if (D2[i][k] + W[k][j]) < D[i][j]:
                    D[i][j] = D2[i][k] + W[k][j]
                    position = k
                else:
                    pass
            if position != -1:
                self._walkDictionary[(i, j)] = list(
                    dict.fromkeys(self.walkDictionary[(i, position)] + self._walkDictionary[(position, j)]))
    return D


def lowestWalk(self, vertexX, vertexY):
    """
    This function will compute the lowest cost walk using the all shortest path matrix
    :param vertexX:
    :param vertexY:
    :return:
    """
    D = []
    for i in range(0, self.__numberOfVertices):
        D.append([])
        for j in range(0, self.__numberOfVertices):
            D[i].append(self.__adjacencyMatrix[i][j])
    m = 1
    while m < self.__numberOfVertices:
        D = self.lowestWalkMatrix(D, self.__adjacencyMatrix)
        m = m * 2
    print(D[vertexX][vertexY])
    return self.__walkDictionary[(vertexX, vertexY)]