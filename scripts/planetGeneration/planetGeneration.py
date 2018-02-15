# -*- coding: utf-8 -*-

import numpy as np
import bpy
import sys
sys.path.append('/home/antoine/3DMaps/scripts/planetGeneration')
import Planet



# Empty the scene
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_all()
bpy.ops.object.delete()

alts = np.zeros(482)

index = 0
for alt in alts:
    if(index%2 == 0):
        alts[index] = 1
    index+=1

newPlanet = Planet.Planet("test", 32, 16, alts,1)
newPlanet.display()