from Landscape import Landscape
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

################################Probability computation#########################
################################################################################
