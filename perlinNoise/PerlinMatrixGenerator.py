import numpy as np
import math
from PerlinGenerator import PerlinGenerator

class PerlinMatrixGenerator:

    def __init__(self,height,width,verticalResolution = 1,horizontalResolution = 1):
        self._height = height
        self._width = width
        self._verticalResolution = verticalResolution
        self._horizontalResolution = horizontalResolution

    def generate(self,persistance = 0.5,startOctave = 0,endOctave = 5,rawSeed = 1):
        perlinGenerator = PerlinGenerator(persistance, startOctave, endOctave, rawSeed,\
        height = int(math.ceil(self._verticalResolution * (self._height - 1) * math.pow(2,endOctave))),\
        width = int(math.ceil(self._horizontalResolution * (self._width - 1) * math.pow(2,endOctave))))
        xLine = np.linspace(start = 0,stop = self._verticalResolution * (self._height - 1), num = self._height)
        yLine = np.linspace(start = 0,stop = self._horizontalResolution * (self._width - 1), num = self._width)
        matrix = np.empty((self._height,self._width), dtype = float)
        for i in range(self._height):
            for j in range(self._width):
                matrix[i][j] = perlinGenerator.getNoise(xLine[i],yLine[j])
        return matrix
