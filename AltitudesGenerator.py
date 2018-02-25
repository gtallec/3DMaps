# -*- coding: utf-8 -*-
import perlinNoise
import numpy as np


class AltitudesGenerator:
    """ Sert a generer une matrice aleatoire d'altitudes a partir d'un
    nombre de latitudes et de longitudes"""

    def __init__(self):
        pass

    """La fonction qui genere les altitudes
    Doit retourner une np.array de forme (latNb-1, lonNb)"""

    def generateAltitudes(self, latNb, lonNb, verticalResolution = 1, horizontalResolution = 1, amplitude = 1, persistance = 1, startOctave = 0, endOctave = 5):
        print(amplitude*perlinNoise.PerlinMatrixGenerator(latNb - 1, lonNb, verticalResolution, horizontalResolution).generate(persistance,startOctave,endOctave))
        return amplitude*perlinNoise.PerlinMatrixGenerator(latNb - 1, lonNb, verticalResolution, horizontalResolution).generate(persistance,startOctave,endOctave)
