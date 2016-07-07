#!/usr/bin/python
# --*-- coding=utf-8 --*--

import numpy as np
import math

import numpy.linalg as LA 

def detection(x,base,window_size=12,matching_size=None,step=1,rho=0.05):

    if matching_size == None:
        matching_size = window_size / 2

    N = len(x)

    assert(N == len(base))
    assert(matching_size < window_size)
    assert((step < matching_size) and (step >= 1))
    assert(window_size <= N)

    x = np.asarray(x)
    base = np.asarray(base)



    for k in xrange(0,N - window_size + 1,step):
        end = k + window_size
        if end > N:
            end = N

        subx = x[k:end:]
        subbase = base[k:end:]

        subbase += (subx[:matching_size].mean() - subbase[:matching_size].mean())

        deviation = subx - subbase
        avg = subx.mean()


def drmf(M,k,e,**options):

    U, s, V = LA.svd(M)
    U = U[:,:k]
    s = s[:k]
    V = V[:k]

    S = np.zeros((k,k))
    np.fill_diagonal(S,s)

    L = np.dot(U,S,V.transpose())
