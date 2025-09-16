'''
Before doing any further procssing on the available data we need to remove the noise form the signal.
ECG signals contains following noise signals:

Baseline wander             : < 0.5Hz (caused by breathing,movement)
Muscle noise (EMG)          : 20-200Hz
Powerline interference      : 50Hz or 60hz(US)

So we need to implement a bandPass filter of range 0.5hz - 40hz

'''
import numpy as np
import wfdb 
from scipy.signal import fftconvolve


def windowedimpulseResponse(FL, FH, fs, N):
    w1 = (2 * np.pi * FL)/fs
    w2 = (2 * np.pi * FH)/fs
    hn = np.zeros(N, dtype=complex)   # <-- make complex
    for n in range(N):
        k = n - (N-1)/2
        if k == 0:
            hn[n] = (w2-w1)/(2*np.pi)
        else:
            hn[n] = (np.exp(1j*((w2+w1)/2)*k) * np.sin(((w2-w1)/2)*k)) / (k*np.pi)
    w = np.hamming(N)
    hn = np.real(hn * w)
    fc = (FL + FH)/2  # center frequency
    H_fc = np.sum(hn * np.exp(-1j * 2 * np.pi * fc * (np.arange(N) - (N-1)/2) / fs))
    hn = hn / np.abs(H_fc)
    return hn  

def record_annotation(record_path,starting_sample=0,ending_sample=1000,channel_size=1):
    record = wfdb.rdrecord(record_path, sampfrom=starting_sample, sampto=ending_sample, channels=[0,channel_size])
    annotation = wfdb.rdann(record_path, 'atr', sampfrom=starting_sample, sampto=ending_sample)
    return record,annotation

def yn(x,h):
    return fftconvolve(x,h,mode='same')
