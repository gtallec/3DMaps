from Node import Node
import numpy as np
import math

class Grid:

    def __init__(self,gridStep,height,width):
        self._nodeMatrix = np.empty((height,width),dtype = object)
        self._gridStep = gridStep
        for i in range(height):
            for j in range(width):
                self._nodeMatrix[i][j] = Node(i*gridStep,j*gridStep)
                self._nodeMatrix[i][j].assignRandomGradient()

################################################################################
################################################################################

    def findTopLeftCorner(self,x,y):
        return math.floor(float(x)/float(self._gridStep)),math.floor(float(y)/float(self._gridStep))

    def vectorContribution(self,iTopLeft,jTopLeft,x,y):
        topLeftContribution = self._nodeMatrix[iTopLeft][jTopLeft].contribution(x,y)
        topRightContribution = self._nodeMatrix[iTopLeft][jTopLeft + 1].contribution(x,y)
        botLeftContribution = self._nodeMatrix[iTopLeft + 1][jTopLeft].contribution(x,y)
        botRightContribution = self._nodeMatrix[iTopLeft + 1][jTopLeft + 1].contribution(x,y)
        return topLeftContribution,topRightContribution,botLeftContribution,botRightContribution

    def interpolate(self,i,j,x,y):
        step = self._gridStep
        #Normalize x and y
        xNorm = float(x-(i)*step)/float(step)

        yNorm = float(y-(j)*step)/float(step)
        #Use Interpolation function
        return self.interpolateFunction(xNorm),self.interpolateFunction(yNorm)

    def interpolateFunction(self,x):
        #N = 10
        #L = [ scipy.special.binom(N + n, n)*scipy.special.binom(2*N + 1, N-n)*np.power(-x,n) for n in range(N+1) ]
        return x



################################################################################
################################################################################

    def generate(self,x,y):
        i,j = self.findTopLeftCorner(x,y)
        i,j = int(i),int(j)
        topLeftContribution,topRightContribution,botLeftContribution,botRightContribution = self.vectorContribution(i,j,x,y)
        xInterpolation, yInterpolation = self.interpolate(i,j,x,y)
        leftContribution = topLeftContribution + xInterpolation*(botLeftContribution - topLeftContribution)
        rightContribution = topRightContribution + xInterpolation*(botRightContribution - topRightContribution)
        totalContribution = leftContribution + yInterpolation*(rightContribution - leftContribution)
        return totalContribution
