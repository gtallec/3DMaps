import numpy as np
import math
import random as rd

class SimplexeNoiseGenerator:

    def __init__(self, dimension):
        self._dimension = dimension
        self._gradientList = self.generateGradientList()
        self._permutationTable = self.generatePermutationTable()


    def generate(self, X):
    #The point here is to find in which simplexe the vector X lies, to do so :
        #1: We change base so that we can easily determine in which hypercube
        #the vector lies
        changedBaseX = self.skew(X)
        #2: Determine the origin of the hypercube in which the point lies
        hypercubeOrigin = np.floor(changedBaseX)
        #3: Unskew the origin coordinates so that we get the origin of the
        # simplex the vector lies in
        simplexOrigin = self.unSkew(hypercubeOrigin)
        #4: Calculate the internal Coordinates inside the simplexe
        internalCoordinates = X - simplexOrigin
        listOfSimplifiedVertices = self.findListOfSimplexVertices(internalCoordinates)
        #6: The aim is now to find the N other vertices
        listOfSimplexVertices = []
        for vertex in listOfSimplifiedVertices:
            simplexVertex = simplexOrigin + self.unSkew(vertex)
            listOfSimplexVertices.append(simplexVertex)
    #Now we have to determine which gradient we apply to each vertex of the simplex
        listOfGradient = self.generateListOfGradient(hypercubeOrigin, listOfSimplifiedVertices)
        print(self.computeTotalContribution(listOfGradient,listOfSimplexVertices,X))
        return self.computeTotalContribution(listOfGradient,listOfSimplexVertices,X)

    def skew(self,X):
        n = self._dimension
        F = (np.sqrt(n+1) - 1)/n
        changeBaseMatrix = F * np.ones(shape = (n,n)) + np.eye(n,n)
        return np.dot(changeBaseMatrix,X)

    def unSkew(self,X):
        n = self._dimension
        G = -(1 - (1/np.sqrt(n+1)))/n
        changeBaseMatrix = G * np.ones(shape = (n,n)) + np.eye(n,n)
        return np.dot(changeBaseMatrix,X)

    def findListOfSimplexVertices(self,internalCoordinates):
        #
        print('internalCoordinates', internalCoordinates)
        copyInternalCoordinates = np.copy(internalCoordinates)
        listOfSimplexVertices = []
        baseVertex = np.zeros((1,self._dimension))[0]
        listOfSimplexVertices.append(baseVertex)
        #
        verticesChecker = 0
        while (verticesChecker < len(copyInternalCoordinates)):
            baseVertex = np.copy(baseVertex)
            argmax = np.argmax(copyInternalCoordinates)
            copyInternalCoordinates[argmax] = -8000
            baseVertex[argmax] = 1
            listOfSimplexVertices.append(baseVertex)
            verticesChecker += 1
        return listOfSimplexVertices


    def generateGradientList(self):
        gradientList = []
        listOfPermutations = self.getPermutations(self._dimension - 1)

        for permutation in listOfPermutations:
            for i in range(len(permutation) + 1):
                gradientList.append(np.array(permutation[:i] + [0] + permutation[i:], dtype = float)/float(self._dimension - 1))
        return gradientList


    def getPermutations(self,dimension):
        if (dimension == 1):
            return [[-1],[1]]
        else:
            newPermutations = []
            previousPermutations = self.getPermutations(dimension - 1)
            for permutation in previousPermutations:
                newPermutations.append([-1] + permutation)
                newPermutations.append([1] + permutation)
            return newPermutations

    def generateIndices(self,hypercubeOrigin, simplifiedVertexCoordinates):
        finalIndex = 0
        for i in range(1,self._dimension + 1):
            finalIndex = self._permutationTable[finalIndex + int(hypercubeOrigin[-i]) + int(simplifiedVertexCoordinates[-i])]
        return finalIndex

    def generateListOfGradient(self,hypercubeOrigin, simplifiedVertexCoordinatesList):
        n = len(self._gradientList)
        return [self._gradientList[self.generateIndices(hypercubeOrigin,simplifiedVertexCoordinates)%n] for simplifiedVertexCoordinates in simplifiedVertexCoordinatesList]

    def generatePermutationTable(self):
        permutationTable = [i for i in range(1,256)]
        rd.shuffle(permutationTable)
        newPermutationTable = []
        for i in range(1,512):
            newPermutationTable.append(permutationTable[i%255])
        return newPermutationTable

    def computeTotalContribution(self,listOfGradient,listOfSimplexVertices,initialCoordinates):
        totalContribution = 0
        for i in range(len(listOfGradient)):
            contribution = self.computeContribution(listOfGradient[i],listOfSimplexVertices[i],initialCoordinates)
            totalContribution += contribution
        return totalContribution

    def computeContribution(self,gradient,vertex,initialCoordinates):
        vertexNorm = math.pow(np.linalg.norm(vertex-initialCoordinates),2)
        distanceToVertex = initialCoordinates - vertex
        distanceContribution = 0.6 - vertexNorm
        if(distanceContribution < 0):
            return 0
        else:
            return math.pow(distanceContribution,4) * np.dot(distanceToVertex,gradient)
