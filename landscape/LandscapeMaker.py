from __future__ import division
from Landscape import Landscape
from math import exp

################################################################################
################################################################################
class LandscapeMaker:

    def __init__(self,planete,dictOfLandscapes):
        self._dictOfLandscapes = dictOfLandscapes
        self._planete = planete

################################Match and Gets##################################
################################################################################
    def associateLandscape(self,altitude):
        for name, altitudes in self._dictOfLandscapes.items():
            if(altitudes[0] <= altitude <= altitudes[1]):
                return Landscape(altitude,self,name)

    def getIntel(self,name):
        return self._dictOfLandscapes[name]

    def addLandscape(self,currentAlt):
        self._planete.appendLandscape(self.associateLandscape(currentAlt))

################################Probability computation bricks##################
################################################################################

    def reliefLengthFactor(self,currentReliefName,toReliefName,i,iChange):
        gradientSum = sum([self._dictOfLandscapes[name][2] for name in self._dictOfLandscapes.keys()])
        gradientNormalization = self._dictOfLandscapes[currentReliefName][2]/gradientSum
        if(currentReliefName == toReliefName):
            return 1
        else:
            return (i-iChange)*gradientNormalization

    def closestReliefFactor(self,currentReliefName,toReliefName,currentAltitude):
        lowAltitude,highAltitude = self._dictOfLandscapes[toReliefName][0] , self._dictOfLandscapes[toReliefName][1]
        distanceList = [abs(lowAltitude - currentAltitude), abs(highAltitude - currentAltitude)]
        isClosest = -1
        if(distanceList[0] < distanceList[1]):
            isClosest = 1
        currentReliefLowAltitude,currentReliefHighAltitude = self._dictOfLandscapes[currentReliefName][0] , self._dictOfLandscapes[currentReliefName][1]
        return exp(-min(distanceList)/abs(currentReliefHighAltitude - currentReliefLowAltitude)),isClosest

    def calculateFitness(self,currentReliefName, toReliefName, currentAltitude, i, iChange):
        reliefLengthFactor = self.reliefLengthFactor(currentReliefName,toReliefName,i,iChange)
        closestReliefFactor = self.closestReliefFactor(currentReliefName,toReliefName,currentAltitude)
        return reliefLengthFactor*closestReliefFactor[0],closestReliefFactor[1]

##############################Probabitility Computation#########################
################################################################################

    def calculateTransitionProbability(self,currentReliefName,currentAltitude,i,iChange):
        fitnessDict = dict()
        for toReliefName in self._dictOfLandscapes.keys():
            fitnessDict[toReliefName] = self.calculateFitness(currentReliefName,toReliefName,currentAltitude,i,iChange)
        #Flatten the dict to simplify probabilistic selectionList
        #List LSelection is a list of three list, the first is the (relief,id) second is probabilityList and third is the isClosest
        sumFitness = sum([fitnessDict[name][0] for name in fitnessDict.keys()])
        ReliefIndexList = []
        probabilityList = []
        isClosestList = []
        j = 0
        for toReliefName in fitnessDict.keys():
            ReliefIndexList.append(toReliefName)
            probabilityList.append(fitnessDict[toReliefName][0]/sumFitness)
            isClosestList.append(fitnessDict[toReliefName][1])
            j+=1
        return [ReliefIndexList,probabilityList,isClosestList]
