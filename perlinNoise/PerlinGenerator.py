import math
import numpy as np
from RandomGenerator import RandomGenerator


class PerlinGenerator:

    def __init__(self, persistance, startOctave, endOctave, rawSeed = 1, height = 2000, width = 2000):
        #
        self._startOctave = startOctave
        self._endOctave = endOctave
        #
        self._persistance = persistance
        #
        self._rawSeed = rawSeed
        #
        self._height = height
        self._width = width
        #
        self._gridList = []
        self.generateGrids()
        #

    def generateGrids(self):
        for octave in range(1):
            amplitude = math.pow(self._persistance,octave)
            octaveGrid = np.empty((self._height,self._width), dtype = float)
            randomGenerator = RandomGenerator(octave,self._rawSeed)
            for i in range(self._height):
                for j in range(self._width):
                    octaveGrid[i][j] = randomGenerator.rawNoise(i,j)
            self._gridList.append(octaveGrid)

    def getNoise(self,u,v):
        noise = 0
        #
        for octave in range(self._endOctave - self._startOctave):
            frequence = math.pow(2,octave + self._startOctave) + 1
            amplitude = math.pow(self._persistance,octave)
            #
            x = u*frequence
            y = v*frequence
            print('x', x, ' y', y)
            #
            randomGenerator = RandomGenerator(octave,self._rawSeed)
            noise += randomGenerator.interpolatedNoise(x,y,self._gridList[0])*amplitude
        #
        return noise
