# -*- coding: utf-8 -*-

import numpy as np

class AltitudesGenerator:
    
    def __init__(self):
        pass
    
    def generateAltitudes(self, latNb, lonNb):
        altitudes = np.zeros((latNb-1)*lonNb)
        altitudes.shape = (latNb-1, lonNb)
        return altitudes
        