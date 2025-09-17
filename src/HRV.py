'''
This file contains the function to calculate 
Mean, SDNN, RMSSD
'''
import numpy as np
def computeHRV(r_interval):
    mean = np.mean(r_interval)
    sdnn = np.std(r_interval)
    #compute rmssd
    N = len(r_interval) - 1
    diff_square = np.zeros(N)
    for i in range (N):
        diff_square[i] = (r_interval[i+1] - r_interval[i]) ** 2
    
    rmssd = np.sqrt(np.mean(diff_square[:]))
    return mean,sdnn,rmssd

r_interval = [0.8,0.82,0.79,0.81]
_,_,rmssd =computeHRV(r_interval)
print("Val: ",rmssd)

