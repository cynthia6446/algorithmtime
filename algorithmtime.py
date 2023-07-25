# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 15:28:56 2023

@author: be
"""

import numpy as np
import matplotlib.pyplot as plt

## define a function that computes the n+1 st Fibonnaci number, given
# the previous two fibonnaci numbers

def aliens(F, n):
    
    """
    Parameters
    ----------
    F : float array
    F[n] is the n-th Fibonnaci number
    n : integer
    index into F
    Returns
    -------
    F[n+1], the (n+1)-st Fibonnaci number
    """
    
    F[n] = F[n-1] + F[n-2]
    return F[n]

def aliens2(F, n):
    
    """
    Parameters
    ----------
    F : float list
    list of fibonacci numbers
    n : integer
    compute the n-th fibonacci number F[n]
    given F[n-1] and F[n-2]
    Returns
    -------
    None.
    """
    if len(F) < 2:
        print(' F is not long enough')
        return(0)
    
    F.append(F[n-1]+F[n-2])
    return F[n]

if __name__ == "__main__":
    
    ## first use an array
    
    F = np.zeros(100)
    F[0] = 0
    F[1] = 1
    for n in range(2, 20):
        F[n] = aliens(F, n)
        
intF = [int(x) for x in F[:20]]
print(intF)

## now use a list
F = []
F.append(0)
F.append(1)
print(F)

for n in range(2,19):
    F[n] = aliens2(F, n)
    print(F[n])
    
## to finish this, comput d[n] = F[n]/F[n-1]
## and for n=1 to 20 plot d[n]
    
d = F
plt.plot(d,'.')