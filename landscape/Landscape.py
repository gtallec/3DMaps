import numpy as np
import random as rd
################################################################################
################################################################################
class Landscape:
    def __init__(self,currentAlt,landscapeMaker,name):
        self._currentAlt = currentAlt
        self._landscapeMaker = landscapeMaker
        self._name = name
        self._intel = self._landscapeMaker.getIntel(name)

###############Define Basic bricks to calculate new altitude####################
################################################################################
    def probabilityChange(self,i,iChange):
        #Calculate the probability of changing relief
        selectionList = self._landscapeMaker.calculateTransitionProbability(self._name,i,iChange)
        selectedRelief = np.random.choice(selectionList[0],1,True,selectionList[1])
        return selectedRelief,selectionList[3]

    def calculateNewAltitude(self,selectedRelief,isClosest):
        #Calculate next altitude
        gradient = self._intel[2]
        lowAltitude = self._intel[0]
        highAltitude = self._intel[1]
        currentAltitude = self._currentAlt
        step = 0
        if(self._name == selectedRelief):
            currentAltitude += rd.uniform(-gradient,gradient)
        else:
            while(lowAltitude <= currentAltitude) and (currentAltitude <= highAltitude):
                currentAltitude += isClosest * gradient
        return currentAltitude

    def addNewAltitude(self,currentAltitude):
        #Send it to the landscapeMaker for him to associate new Landscape
        self._landscapeMaker.associateLandscape(currentAltitude)

####################Full fonction to calculate new altitude#####################
################################################################################
    def nextAltitude(self,i,iChange):
        selectedRelief, isClosest = self.probabilityChange(i,iChange)
        currentAltitude = self.calculateNewAltitude(selectedRelied, isClosest)
        self.addNewAltitude(currentAltitude)

###################################Gets ans Sets################################
################################################################################
    def getName(self):
        return self._name
