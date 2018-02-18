# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/antoine/3DMaps')
import PlanetManager
import Displayer
import bpy

newManager = PlanetManager.PlanetManager()
newManager.createPlanet(0, 128, 256, 1)

newDisplayer = Displayer.Displayer(newManager)
newDisplayer.displayPlanetById(0)

bpy.ops.export_scene.b4w_html(filepath="/home/antoine/test.html")

