
from LandscapeMaker import LandscapeMaker
################################################################################
import random as rd
import matplotlib.pyplot as plt
################################################################################
################################################################################
class Planete:

    def __init__(self,firstAltitude,dictOfLandscapes,size):
        #Instanciate a landscapeMaker which match altitudes with Landscapes
        landscapeMaker = LandscapeMaker(self,dictOfLandscapes)
        #Initialize the planet List
        self._landscapeList = []
        #Initialize with random altitudes
        self._landscapeList.append(landscapeMaker.associateLandscape(firstAltitude))
        self._size = size
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
            self._landscapeList[i].nextAltitude(i,ichange)
            i+=1
    def appendLandscape(self,landscape):
        self._landscapeList.append(landscape)

################################################################################
##############################Display Curves####################################
################################################################################

    def display(self):
        Lx = [i for i in range(len(self._landscapeList))]
        Ly = [landscape._currentAlt for landscape in self._landscapeList]
        plt.plot(Lx,Ly)
        plt.show()
##########################Get and sets##########################################
################################################################################
    def getLandscapeList(self,index):
        return self._landscapeList[index]

    def setLandscapeList(self,index,landscape):
        self._landscapeList[index] = landscape
