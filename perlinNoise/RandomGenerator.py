import random
import math
import numpy as np

class RandomGenerator:

    def __init__(self,octave,rawSeed):
        self._octave = octave
        self._rawSeed = rawSeed

    def rawNoise(self,x,y):
        random.seed = self._octave * 1000000 + (x*1000000000) + math.pow(y*100000000000,self._rawSeed)
        return 2*(random.random()) - 1

    def interpolationFunction(self,a,b,n):
        radians = n*math.pi
        n = (1 - math.cos(radians)) * 0.5;
        return a + n*(b-a)

    def interpolatedNoise(self,x,y,octaveGrid):
    #
        #
        floorX = int(x)
        xInsideSquare = x-floorX
        print('floorX',floorX,'xInsideSquare',xInsideSquare)
        #
        floorY = int(y)
        yInsideSquare = y - floorY
        print('floorY',floorY,'yInsideSquare',yInsideSquare)
    #
        #
        leftUpCornerNoise = octaveGrid[floorX][floorY]
        #
        leftDownCornerNoise = octaveGrid[floorX + 1][floorY]
        #
        rightUpCornerNoise = octaveGrid[floorX][floorY + 1]
        #
        rightDownCornerNoise = octaveGrid[floorX + 1][floorY + 1]
    #
        leftInterpolation = self.interpolationFunction(leftUpCornerNoise,leftDownCornerNoise,xInsideSquare)
        rightInterpolation = self.interpolationFunction(rightUpCornerNoise,leftUpCornerNoise,xInsideSquare)
    #
        totalInterpolation = self.interpolationFunction(leftInterpolation,rightInterpolation,yInsideSquare)
    #
        return totalInterpolation
