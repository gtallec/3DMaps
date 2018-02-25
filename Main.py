# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/tallec/Documents/WORK/3DMaps')
import PlanetManager
import Displayer

newManager = PlanetManager.PlanetManager()
newManager.createPlanet(id = 0,\
                        latNb = 128,\
                        lonNb = 256,\
                        diameter = 12.5,\
                        verticalResolution = 0.1,\
                        horizontalResolution = 0.1,\
                        amplitude = 1,\
                        persistance = 1,\
                        startOctave = 0,\
                        endOctave = 5)

newDisplayer = Displayer.Displayer(newManager)
newDisplayer.displayPlanetById(0)
