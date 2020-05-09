import math
import numpy as np

def SpikeRemoval(x, mu):
    #This function removes spikes that go over the threshold value mu
    #Each array element that is over mu is averaged between previous and subsequent element
    
	#If spikes occur in the first or last element of the array, it filters out using the nearest value
	
	if(x[1] > mu):
    		
    		x[1] = x[2]

	if(x[-1]> mu):
    		
    		x[-1] = x[-2]

	for i in range(2, len(x)-1):
    		
    		if(x[i] > mu):
    				x[i] = np.mean([x[i-1], x[i+1]])

	return x
