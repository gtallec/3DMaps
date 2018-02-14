
from LandscapeMaker import LandscapeMaker
################################################################################
import random as rd
################################################################################
################################################################################
class Planete:

    def __init__(self,dictOfLandscapes):
        #Instanciate a landscapeMaker which match altitudes with Landscapes
        landscapeMaker = LandscapeMaker(self,dictOfLandscapes)
        #Initialize the planet List
        self._landscapeList = []
        #Initialize with random altitudes
        minAltitude = min([altitudes[0] for altitudes in dictOfLandscapes.values()])
        maxAltitude = max([altitudes[1] for altitudes in dictOfLandscapes.values()])
        randomAltitude = rd.uniform(minAltitude,maxAltitude)
        self._landscapeList.append(landscapeMaker.associateLandscape(randomAltitude))
        self._size = 1
#############################Calculate last change position#####################
################################################################################

    def lastChangePosition(self):
        nameList = [self._landscapeList[i].getName() for i in range(len(self._landscapeList))]
        i = len(self._landscapeList) - 1
        while (nameList[i] == nameList[len(self._landscapeList) - 1]) and (i >=0):
            i-=1
        if(i < 0):
            return 0
        else:
            return i
#############################Fill the landscape List############################
################################################################################

    def fillLandScapeList(self):
        i = 0
        while (i < self._size):
            ichange = self.lastChangePosition()
            self._landscapeList[i].nextAltitude(ichange,i)
