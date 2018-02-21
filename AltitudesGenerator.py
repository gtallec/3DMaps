# -*- coding: utf-8 -*-
from perlinGenerator import PerlinGenerator
import numpy as np


class AltitudesGenerator:
    """ Sert a generer une matrice aleatoire d'altitudes a partir d'un
    nombre de latitudes et de longitudes"""

    def __init__(self):
        pass

    """La fonction qui genere les altitudes
    Doit retourner une np.array de forme (latNb-1, lonNb)"""

    def generateAltitudes(self,res, latNb, lonNb, amplitude):
        altitudes = PerlinGenerator(res,res,latNb,lonNb,amplitude)._perlinMatrix
        altitudes = altitudes[:-1]
        return altitudes
