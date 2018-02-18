# -*- coding: utf-8 -*-

import numpy as np

class AltitudesGenerator:
    """ Sert a generer une matrice aleatoire d'altitudes a partir d'un
    nombre de latitudes et de longitudes"""

    def __init__(self):
        pass

    """La fonction qui genere les altitudes
    Doit retourner une np.array de forme (latNb-1, lonNb)"""

    def generateAltitudes(self, latNb, lonNb):
        altitudes = np.zeros(shape = (latNb-1,lonNb))
        whiteNoise = np.random.normal(size = (latNb-1,lonNb) )
        altitudes = 0.007*whiteNoise
        return altitudes
