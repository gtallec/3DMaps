from LandscapeMaker import LandscapeMaker
from Planete import Planete
from Landscape import Landscape
from Globe import Globe


########################Variables###############################################
################################################################################
#instanciate a dict with key the type of landscape and value the (altb,alth,gradient,lengthParameter)
dictOfLandscapes = {"sea" : (-4000,-2000,10),"transition" : (-2000,0,200), "plain" : (0,1000,10),"mountain" : (1000,7000,500)}
width = 10
height = 10


#########################SuccessFull Test#######################################
################################################################################
def Test():
    print('display elements of the list')
    planete = Planete(5000,dictOfLandscapes,size)
    print([planete._landscapeList[i]._currentAlt for i in range(len(planete._landscapeList))])
    print([planete._landscapeList[i]._name for i in range(len(planete._landscapeList))])

    print('display Transition Probability')
    landscapeMaker = LandscapeMaker(0,dictOfLandscapes)
    print(landscapeMaker.calculateTransitionProbability('mountain',1550,1,1))
    pass


#########################Pending Test###########################################
################################################################################
globe = Globe(4000,dictOfLandscapes,height,width)
globe.getAltitudeMatrix()
