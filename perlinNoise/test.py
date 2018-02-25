from PerlinMatrixGenerator import PerlinMatrixGenerator
import matplotlib.pyplot as plt
import numpy as np

############################Variables###########################################
height = 128
width = 256
verticalResolution = 0.1
horizontalResolution = 0.1
startOctave = 0
endOctave = 3
persistance = 0.5
################################################################################

perlinMatrixGenerator = PerlinMatrixGenerator(height, width, verticalResolution, horizontalResolution)
generation = perlinMatrixGenerator.generate(persistance, startOctave, endOctave)
plt.imshow(generation, cmap = 'gray')
plt.show()
