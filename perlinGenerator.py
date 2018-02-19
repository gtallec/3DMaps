from Grid import Grid
import numpy as np
import scipy
import matplotlib.pyplot as plt

class PerlinGenerator:

    def __init__(self,verticalRes,horizontalRes,height,width,amplitude):
        perlinHeight = height/verticalRes + 1
        perlinWidth = width/horizontalRes + 1

        self._perlinGrid = Grid(1,perlinHeight,perlinWidth)
        self._perlinMatrix = np.zeros((height,width))

        X = [i * (float(1)/float(verticalRes)) for i in range(height)]
        Y = [j * (float(1)/float(horizontalRes)) for j in range(width)]

        for i in range(height):
            for j in range(width):
                self._perlinMatrix[i][j] = self._perlinGrid.generate(X[i],Y[j])
        self._perlinMatrix = self._perlinMatrix * amplitude

    def display(self,i):
        plt.plot([j for j in range(len(self._perlinMatrix[i]))],self._perlinMatrix[i])
        plt.show()
