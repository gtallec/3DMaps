import random as rd
import numpy as np

class Node:

    aleaGradient = [np.array([-1,0]),np.array([1,0]),np.array([0,-1]),np.array([0,1]),np.array([1,1])/np.sqrt(2),np.array([-1,-1])/np.sqrt(2),np.array([-1,1])/np.sqrt(2),np.array([1,-1])/np.sqrt(2)]
    def __init__(self,x,y):
        self._x = x
        self._y = y
        self._randomVector = None

    def assignRandomGradient(self):
        randomNumber = rd.randint(0,7)
        self._randomVector = Node.aleaGradient[randomNumber]

    def contribution(self,xPoint,yPoint):
        distanceVector = np.array([xPoint-self._x, yPoint - self._y])
        return np.dot(self._randomVector,distanceVector)
