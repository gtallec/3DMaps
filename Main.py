# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/antoine/3DMaps')
import PlanetManager
import Displayer
import numpy as np

newManager = PlanetManager.PlanetManager()
altitudes = np.zeros(32512)
altitudes.shape = (127, 256)
newManager.addPlanet(0, 128, 256, 1, altitudes)

newDisplayer = Displayer.Displayer(newManager)
newDisplayer.displayPlanetById(0)