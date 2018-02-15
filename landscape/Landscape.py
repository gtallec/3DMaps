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
        selectionList = self._landscapeMaker.calculateTransitionProbability(self._name,self._currentAlt,i,iChange)
        landScapeSelector = [i for i in range(len(selectionList[0]))]
        selectedRelief = np.random.choice(landScapeSelector,1,True,selectionList[1])
        return selectionList[0][selectedRelief[0]],selectionList[2][selectedRelief[0]]

    def calculateNewAltitude(self,selectedRelief,isClosest):
        #Calculate next altitude
        gradient = self._intel[2]
        lowAltitude = self._intel[0]
        highAltitude = self._intel[1]
        currentAltitude = self._currentAlt
        step = 0
        if(self._name == selectedRelief):
            newCurrentAltitude = currentAltitude + rd.uniform(-gradient,gradient)
            while (highAltitude <= newCurrentAltitude) or (newCurrentAltitude <= lowAltitude):
                newCurrentAltitude = currentAltitude + rd.uniform(-gradient,gradient)
            currentAltitude = newCurrentAltitude
        else:
            lowAltitudeSelected,highAltitudeSelected,gradientSelected = self._landscapeMaker.getIntel(selectedRelief)
            while(highAltitudeSelected <= currentAltitude) or (currentAltitude <= lowAltitudeSelected):
                currentAltitude += isClosest * gradient
        return currentAltitude

    def addNewAltitude(self,currentAltitude):
        #Send it to the landscapeMaker for him to associate new Landscape
        self._landscapeMaker.addLandscape(currentAltitude)

####################Full fonction to calculate new altitude#####################
################################################################################
    def nextAltitude(self,i,iChange):
        selectedRelief, isClosest = self.probabilityChange(i,iChange)
        currentAltitude = self.calculateNewAltitude(selectedRelief, isClosest)
        self.addNewAltitude(currentAltitude)

###################################Gets ans Sets################################
################################################################################
    def getName(self):
        return self._name
