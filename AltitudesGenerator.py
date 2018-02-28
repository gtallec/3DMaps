# -*- coding: utf-8 -*-
import perlinNoise
import simplexeNoise
import numpy as np


class AltitudesGenerator:
    """ Sert a generer une matrice aleatoire d'altitudes a partir d'un
    nombre de latitudes et de longitudes"""

    def __init__(self):
        pass

    """La fonction qui genere les altitudes
    Doit retourner une np.array de forme (latNb-1, lonNb)"""

    def generateAltitudes(self, latNb, lonNb, verticalResolution = 1, horizontalResolution = 1, amplitude = 1):
        return simplexeNoise.SimplexeNoiseMatrixGenerator(latNb - 1, lonNb, horizontalResolution, verticalResolution, amplitude).generate()
