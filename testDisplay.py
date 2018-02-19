import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from AltitudesGenerator import AltitudesGenerator

#################################Variables######################################
latitude = 128
longitude = 256
resolution = 8
amplitude = 4000
################################################################################
altitudeGenerator = AltitudesGenerator()
matrix = altitudeGenerator.generateAltitudes(resolution,latitude,longitude,amplitude)
