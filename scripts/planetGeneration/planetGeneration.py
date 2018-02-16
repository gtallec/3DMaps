# -*- coding: utf-8 -*-

import numpy as np
import bpy
import sys
sys.path.append('/home/antoine/3DMaps/scripts/planetGeneration')
import Planet
sys.path.append('/home/antoine/3DMaps/landscape')
import Globe


# Empty the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_all()
bpy.ops.object.delete()

#instanciate a dict with key the type of landscape and value the (altb,alth,gradient,lengthParameter)
dictOfLandscapes = {"sea" : (-4000,-2000,10),"transition" : (-2000,0,200), "plain" : (0,1000,10),"mountain" : (1000,7000,500)}
width = 256
height = 128
    
globe = Globe.Globe(5000,dictOfLandscapes, height, width)

alts = globe.getAltitudeMatrix()
lat = 0
while lat < 128:
    lon = 0
    while lon < 256:
        alts[lat][lon]=alts[lat][lon]/70000
        lon+=1
    lat+=1
    
newPlanet = Planet.Planet("test", 128, 256, alts,1)