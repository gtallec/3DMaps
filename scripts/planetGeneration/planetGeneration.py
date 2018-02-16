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

alts = np.zeros(480)
alts.shape = (15, 32)
idx = 0
ex = 0
while idx < 32:
    alts[1][idx] = ex
    idx += 1
    ex += 0.1

idx = 0
while idx < 32:
    alts[5][idx] = 1
    idx += 1
    
newPlanet = Planet.Planet("test", 16, 32, alts,1)