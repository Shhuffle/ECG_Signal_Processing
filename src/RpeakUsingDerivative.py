'''
In this code I will try to implement  derivative of discrete time signal and calculate peak index.
Logic used:
derivative  = del(y)/del(x)
First to calculate the del(y) and del(X) I will take the difference between the ith and (i+1)th element for both list
Then divide the corresponding element to get the derivative list
In this way we can compute between which index the signal has the maximum rate of change

calcRpeakIndex: 
    It will calculate the peak index value based on threshold
    If the rate of change is greater than threshold, then register the index.
'''

'''
A issue occured while calculating the derivative, we cant just take the difference of each sample cause the y_n values might
take mutiple sample to reach the threshold meaning the rise of y_n is not ideal.
Suppose y_n takes 5 sample range or x axis values to reach the height greater than  threshold
If we calculate the difference of each y_n index then the difference might never reach greater than threshold
Say threshold is 0.3 and y_n reaches a peak of 0.5,
Then the differnce between the each 5 sample may be 0.1, which is less than the threshold and the peak value may never be observed.

So to solve this differene is taken in different manner
The difference will be calculated form ith index to ith+n index, i 


'''
import numpy as np
#x,y should be of same range
def derivative(x,y,lim=5):
    
    if  ((len(x) != len(y))):
        raise("Length Mismatch")
    N = len(x) - 1
    derivative_list = np.zeros(N)
    partial_diff = np.zeros(lim)
    for i in range (N):
        for k in range (lim):
            if(x[k] - x[k+1] == 0):
                raise("Divide by 0")
            if((i+k+1) >= len(x)):
                continue
            partial_diff[k] =  abs((y[i] - y[i+k+1])/(x[i+k] - x[i+k+1])) 
        derivative_list[i] =  np.max(partial_diff)
       
    return abs(derivative_list)




def calcRpeakIndex(x,y,threshold,samples_to_skip = 20):
    derivative_list = derivative(x,y)
    N = len(derivative_list)
    PeakIndex = []
    i = 0
    while i < N:
        
        if(derivative_list[i] > threshold):
            PeakIndex.append(i)
            i = i + samples_to_skip #skip the next n index cause they are the same peak value indexes.
        i += 1
    return np.array(PeakIndex)

if __name__ == "__main__":
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [1,2,9,9,0,4,1,3,1,4]
    deri_vative = derivative(x,y) 
    print("The observed derivative is: ",deri_vative)
    print("Peak Index: ", calcRpeakIndex(x,y,8))
        