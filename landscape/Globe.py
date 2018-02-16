from Planete import Planete
import numpy as np
from Landscape import Landscape

class Globe:

    def __init__(self,firstAltitude,dictOfLandscapes,height,width):
        landscapeMatrix = np.empty((height,width),dtype = object)
        #Design borders
        planeteHor = Planete(firstAltitude,dictOfLandscapes,width)
        planeteHor.fillLandScapeList()

        for i in range(width):
            landscapeMatrix[0][i] = planeteHor.getLandscapeList(i)

        for j in range(width):
            planeteVert = Planete(landscapeMatrix[0][j]._currentAlt,dictOfLandscapes,height)
            planeteVert.fillLandScapeList()
            for i in range(1,height):
                landscapeMatrix[i][j] = planeteVert.getLandscapeList(i)
        self._landscapeMatrix = landscapeMatrix

    def getAltitudeMatrix(self):
        matrix = self._landscapeMatrix
        altitudeArray = [[matrix[i][j]._currentAlt for j in range(len(matrix[i]))] for i in range(len(matrix))]
        return altitudeArray
