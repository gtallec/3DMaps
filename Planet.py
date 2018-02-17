# -*- coding: utf-8 -*-

class Planet:
    
    def __init__(self, id, latNb, lonNb, diameter, altitudes):
        self.id = id
        self.latNb = latNb
        self.lonNb = lonNb
        self.diameter = diameter
        self.altitudes = altitudes
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