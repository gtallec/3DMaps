import numpy as np
from PerlinGenerator import PerlinGenerator

class PerlinMatrixGenerator:

    def __init__(self,height,width):
        self._height = height
        self._width = width

    def generate(self,persistance = 0.25,startOctave = 0,endOctave = 5,rawSeed = 1):
        perlinGenerator = PerlinGenerator(persistance, startOctave, endOctave, rawSeed)
        matrix = np.empty((self._height,self._width), dtype = float)
        for i in range(self._height):
            for j in range(self._width):
                matrix[i][j] = perlinGenerator.getNoise(i,j)
        return matrix
