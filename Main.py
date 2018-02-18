# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/antoine/3DMaps')
import PlanetManager
import Displayer

newManager = PlanetManager.PlanetManager()
newManager.createPlanet(0, 128, 256, 12.5)

newDisplayer = Displayer.Displayer(newManager)
newDisplayer.displayPlanetById(0)