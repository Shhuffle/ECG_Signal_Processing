import numpy as np

def heartbeat(r_peak_time):
    
    r_interval = np.zeros(len(r_peak_time)-1)
    for i in range (len(r_peak_time)-1):
        r_interval[i] = r_peak_time[i+1] - r_peak_time[i]

    mean = np.sum(r_interval) / len(r_interval)
    HB = 60/mean
    
    return HB
