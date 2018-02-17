# -*- coding: utf-8 -*-

import AltitudesGenerator

class Planet:
    
    def __init__(self, id, latNb, lonNb, diameter):
        self.id = id
        self.latNb = latNb
        self.lonNb = lonNb
        self.diameter = diameter
        self.altitudes = AltitudesGenerator.AltitudesGenerator().generateAltitudes(latNb, lonNb)
        print("Planet " + str(id) + " created")
        
    def getId(self):
        return self.id
        
    def getLatNb(self):
        return self.latNb
    
    def getLonNb(self):
        return self.lonNb
    
    def getDiameter(self):
        return self.diameter
    
    def getAltitudes(self):
        return self.altitudes