from SimplexeNoiseMatrixGenerator import SimplexeNoiseMatrixGenerator
import numpy as np
import matplotlib.pyplot as plt

################################################################################
height = 128
width = 256
horizontalResolution = 0.1
verticalResolution = 0.1
amplitude = 1
################################################################################
simplexeNoiseMatrixGenerator = SimplexeNoiseMatrixGenerator(height, width, horizontalResolution, verticalResolution, amplitude)
plt.imshow(simplexeNoiseMatrixGenerator.generate())
plt.show()
