'''
Before doing any further procssing on the available data we need to remove the noise form the signal.
ECG signals contains following noise signals:

Baseline wander             : < 0.5Hz (caused by breathing,movement)
Muscle noise (EMG)          : 20-200Hz
Powerline interference      : 50Hz or 60hz(US)

So we need to implement a bandPass filter of range 0.5hz - 40hz

'''
import numpy as np

def windowedimpulseResponse(FL,FH,fs,N):
    
    w1 = (2 * np.pi * FL)/fs
    w2 = (2 * np.pi * FH)/fs
    hn = []
    for n in range (N):
        k = (n-(N-1)/2)
        if k == 0:
            hn.append((w2-w1)/2 *np.pi)
        else: 
            hn.append((np.exp(1j * ((w2+w1)/2) * k)) * np.sin(((w2-w1)/2) * k))
    w = np.hanning(N)
    return hn * w

