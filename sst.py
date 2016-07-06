#!/usr/bin/python
#-*- coding=utf-8-*-
import numpy as np
from numpy import linalg as LA


# Using shifted time series.
def shift(arr, n, padding=0,order='forward'):
    if order == 'forward':
        shifted = arr[n:] + [padding] * n
    elif order == 'reversed':
        shifted = [padding] * n + arr[:-n]
    else:
        print("Order %s not recognized.  Try forward or reversed" % order)

    return shifted


# Singular spectrum analysis
def ssa(time_series,window_size,window_number=None,gamma=None,eta=3,rho=None):  

    # parameter setting 
    if window_number == None:
        window_number = window_size

    if gamma == None:
        gamma = window_size / 2

    if rho == None:
        rho = eta

    # construct embedded time series
    shifted_ = np.c_[time_series]
    for k in xrange(1,window_number):
        shifted_ = np.c_[shifted_,shift(time_series,k)]

    N = len(time_series)
    change_score = []
    start = t + window_size
    for t in range(N):
        if (t + window_size + gamma) > N:
            break
        subX1 = shifted_[t:(t+window_size):,:]
        subX2 = shifted_[(t+gamma):(t + window_size+gamma):,:]
        U,s,V = LA.svd(subX1)
        beta = U[:,:eta]
        U,s,V = LA.svd(subX2)
        alpha = U[:,:rho]
        phi = [0] * rho
        for i in range(rho):
            phi[i] = 1 - np.dot(alpha[:,i].transpose(),beta,alpha[:,i])
        change_score.append(np.average(np.array(phi),s[:rho]))
    return (change_score,start)

if __name__ == "__main__":
    ts = np.random.random(288)








