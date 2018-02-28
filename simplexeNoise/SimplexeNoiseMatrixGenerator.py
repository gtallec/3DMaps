from SimplexeNoiseGenerator import SimplexeNoiseGenerator
import numpy as np

class SimplexeNoiseMatrixGenerator:

    def __init__(self,height,width,horizontalResolution,verticalResolution,amplitude):
        self._amplitude = amplitude
        self._width = width
        self._height = height
        self._horizontalResolution = horizontalResolution
        self._verticalResolution = verticalResolution

    def generate(self):
        simplexeNoiseGenerator = SimplexeNoiseGenerator(2)
        simplexNoise = np.empty((self._height,self._width),dtype = float)
        xList = np.linspace(start = 0, stop = self._height * self._verticalResolution, num = self._height)
        yList = np.linspace(start = 0, stop = self._width * self._horizontalResolution, num = self._width)
        for i in range(self._height):
            for j in range(self._width):
                simplexNoise[i][j] = simplexeNoiseGenerator.generate(np.array([xList[i],yList[j]]))
        return self._amplitude*simplexNoise
