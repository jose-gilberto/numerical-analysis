# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(10))
y = x**2

plt.plot(x, x*0)
plt.plot(x, y - 3)

# Function that will be used in this example
def func(x):
    return x**2 - 3

# lower, higher interval endpoints, tolerance TOL and initial iterations
LOWER, HIGHER, EPSILON, NMAX, i = 1, 2, 0.01, 10000, 1

while i <= NMAX:
    p = LOWER + (HIGHER - LOWER)/2 # compute P_i
    f_p, f_lower = func(p), func(LOWER)
    plt.plot([p], [f_p], color = 'red', marker = 'o', markersize = 2)
    
    if (f_p == 0) or ((HIGHER - LOWER)/2 < EPSILON):
        print('Procedure completed successfully, the result is {}'.format(p))
        break
    
    i = i + 1 # increments the number of iterations
    # computes LOWER_i and HIGHER_i
    if f_lower * f_p > 0: 
        LOWER = p
    else: 
        HIGHER = p

if i == NMAX:
    print('Method failed after NMAX iterations, NMAX = {}'.format(NMAX))
    print('The procedure was unsuccessful.')

print('Graph representation:')
plt.axis([1,2,-1,1])
plt.show()
