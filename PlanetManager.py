# -*- coding: utf-8 -*-

import Planet

class PlanetManager:
    """ Sert a gerer un ensemble de planetes """
    
    def __init__(self):
        self.planets = []
    
    def createPlanet(self, id, latNb, lonNb, diameter):
        planet = Planet.Planet(id, latNb, lonNb, diameter)
        self.planets.append(planet)
        print("Planet " + str(planet.getId()) + " added")
        
    def deletePlanetById(self, planetId):
        for planet in self.planets:
            if planet.getId() == planetId:
                self.planets.remove(planet)
                print("Planet " + str(planet.getId()) + " deleted")
                
    def getPlanetById(self, planetId):
        for planet in self.planets:
            if planet.getId() == planetId:
                return planet