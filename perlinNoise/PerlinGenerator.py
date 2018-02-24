import math
from RandomGenerator import RandomGenerator


class PerlinGenerator:

    def __init__(self, persistance, startOctave, endOctave, rawSeed = 1):
        #
        self._startOctave = startOctave
        self._endOctave = endOctave
        #
        self._persistance = persistance
        #
        self._rawSeed = rawSeed

    def getNoise(self,u,v):
        noise = 0
        #
        for octave in range(self._endOctave - self._startOctave):
            frequence = math.pow(2,octave + self._startOctave) + 1
            amplitude = math.pow(self._persistance,octave)
            #
            x = u*frequence
            y = v*frequence
            #
            randomGenerator = RandomGenerator(octave,self._rawSeed)
            noise += randomGenerator.interpolatedNoise(int(x),int(y))*amplitude
        #
        return noise
