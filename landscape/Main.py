from LandscapeMaker import LandscapeMaker
from Planete import Planete
from Landscape import Landscape


########################Variables###############################################
################################################################################
#instanciate a dict with key the type of landscape and value the (altb,alth,gradient)
dictOfLandscapes = {"sea" : (-4000,0,400),"plain" : (0,1000,100),"mountain" : (1000,7000,700)}


#########################SuccessFull Test#######################################
################################################################################
def Test():
    print('display elements of the list')
    planete = Planete(dictOfLandscapes)
    print([planete._landscapeList[i]._currentAlt for i in range(len(planete._landscapeList))])
    print([planete._landscapeList[i]._name for i in range(len(planete._landscapeList))])

    print('display Transition Probability')
    landscapeMaker = LandscapeMaker(0,dictOfLandscapes)
    print(landscapeMaker.calculateTransitionProbability('mountain',1550,1,1))
    pass


#########################Pending Test###########################################
################################################################################
planete = Planete(dictOfLandscapes)
planete.fillLandScapeList()
planete.display()
