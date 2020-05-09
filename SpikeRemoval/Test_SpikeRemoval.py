from SpikeRemoval import SpikeRemoval
import random
import numpy as np
import math
import matplotlib.pyplot as plt

# Get x values of the sine wave
time = np.arange(0, 20, 0.01)

# Amplitude of the sine wave is sine of a variable like time
amplitude = np.sin(2* np.pi* 0.5* time)
amplitude2 = np.sin(2* np.pi* time)

x = 0.1*amplitude + 0.2*amplitude2

r = np.random.randint(1, len(x), 10)

mu = 2* np.std(x)
x[r] = 0.5
x[1] = 1.5
x[-1] = 2
  	
plt.plot(x)
plt.plot(SpikeRemoval(x, mu),'r')
plt.grid(True)
plt.savefig('OutputImage/SpikeRemoval.jpg')
