# -*- coding: utf-8 -*-

import AltitudesGenerator

class Planet:
    """ Classe representant une planete avec ses attributs :
    _ Identifiants
    _ Nombre de latitudes
    _ Nombre de longitudes
    _ Diametre"""
    
    # Recupere les attributs passes en parametre et genere des altitudes
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