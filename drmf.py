#!/usr/bin/python
# --*-- coding=utf-8 --*--
import numpy as np 
import numpy.linalg as LA



def sdvex(M,K):
    U, s, K = LA.svd(M)
    U = U[:,:k]
    s = s[:k]
    V = V[:,:k]

    D = np.zeros((k,k))
    np.fill_diagonal(D,s)

    return (U, D, V)  

def rmse(A,B):

    return np.sqrt(np.mean(((A - B) ** 2)))

def drmf(M,k,e,**options):

    max_iter = 100 if not options.has_key('max_iter') else options['max_iter']
    epsilon = 1e-4 if not options.has_key('epsilon') else options['epsilon']



    m,n = M.shape

    U, D, V = svdex(M, K)




    L = np.dot(np.dot(U, D), V.transpose())


    S = np.zeros((m,n))
    objs = []

    for it in range(max_iter):
        # BACKUP
        old = {
           'L': np.copy(L),
           'S': np.copy(S)
        }

        # update S
        A = M - L

        idx = np.abs(A) < np.percentile(np.abs(A),(1 - e) * 100)

        S = np.copy(A)
        S[idx] = 0

        # update L
        B = M - S

        U, D, V = svdex(B, K)

        L = np.dot(np.dot(U, D), V.transpose())

        # Root Mean Squared Error
        objs.append(rmse(B,L))

        # convergence check

        if (it > 1) and ((objs[-2] - objs[-1]) / objs[-2] < epsilon or objs[-1] < 1e-7):
            L, S = old['L'], old['S']
            break
    return (L,S)





    

if __name__ == "__main__":
    M = np.array([[1,2,3,4],[4,5,8,9],[9,0,8,0]])
    print M
    K = 3
    L = drmf(M,K,0)
    print L
    print M - L
