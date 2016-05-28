#!/usr/bin/env python
'''A script to calculate the intersection points of n-dimensional spheres.

Based on the Orthogonal decompostion method in 

I. D. Coope. Reliable computation of the points of intersection of n spheres in Rn. Australian
and New Zealand Industrial and Applied Mathematics Journal (ANZIAM), 42(E):C461-C477, 2000.

DEPENDENCIES:
    You will need to install:
        - Numpy (http://numpy.scipy.org)
        - Scipy (http://www.scipy.org)

USAGE:
    >>> testA
    array([[0, 1],
           [0, 0]])
    >>> testd
    array([[ 1.        ],
           [ 1.41421356]])


    >>> x = intersectionpoint(testA, testd)
    >>> x
    array([[ -2.22044605e-16],
           [  1.00000000e+00]])
           
    >>> distance(x, testA[:, 0])
    1.0
    >>> distance(x, testA[:, 1])
    1.4142135623730951
    

EXPLANATION:
    testA is a matrix with two points in a 2-dimensional plane with XY-axes:
   
    Y  
     |
     |
     |
     |
     |
     |
     |
    (1)-----------(2)----  X
    
    
    Point (1) has coordinates (0, 0) (column0 in testA)
    Point (2) has coordinates (1, 0) (column1 in testA)
    
    intersectionpoint() can be used to compute the coordinates
    of point (3) which is at given distances from points (1) and (2).
    
    Let's take the distance (1)-(3) to be 1 (element0 in testd)
    Let's take the distance (2)-(3) to be sqrt(2) (=1.4142) (element1 in testd)
    
    Now the function intersectionpoint() returns (-2.22044605e-16, 1.00000000e+00)
    which is virtually the same as (0, 1).
    
    And indeed, if we draw point (3) on the plane we can infer easily that this is correct:
    
    Y
     |
    (3)
     |
     |
     |
     |
     |
    (1)-----------(2)---- X
    
    
    The advantage of intersection point() is that it can handle higher dimensional spaces.'''
__author__ = 'Vincent Van Asch'
__date__ = 'March 2011'
__version__ = '1.0'

from math import pow, sqrt
from numpy import array, tile, ones, zeros, dot, vstack, hstack
from scipy.linalg import qr, norm, solve


# Example matrix A with center points and vector d with radii
#testA = array([[0, 1],[0, 0]])
#testd = array([[1], [sqrt(2)]])

testA = array([[0, 0, 0],[0, 1, 0],[0, 0.5, 0.5]])
testd = array([[10], [10], [10]])

def kwad(x): return pow(x, 2)

def distance(x,y):
    '''Distance between two points x,y'''
    def diff(x):
        return pow(x[0]-x[1], 2)
    if len(x) != len(y):
        raise ValueError('x and y must be vectors of the same length: %d != %d' %(len(x), len(y)))
        
    return sqrt(sum( map(diff, zip(x,y)) ) )


def intersectionpoint(A, d):
    '''
    Takes a matrix A (nxn) in which the columns are
    the coordinates of the center points of the n-spheres.
    d is a vertical vectors (nx1) containing the radii of
    the corresponding center points in A.
    Returns the coordinates of the intersection point of
    the n-spheres (if it exists)
    '''
    if isinstance(A, list): A = array(A)
    if isinstance(d, list): d = array(d, ndmin=2).T
        
    # Get the dimension
    n = A.shape[1]
      
    # Get the last sphere
    an = A[:, -1]
    an.shape = (1, an.shape[0])
    an = an.T
    
    dn = d[-1]
    
    # Shift A matrix
    As = A[:,:-1] - tile(A[:,-1], (n-1, 1)).T

    # QR factorisation
    Q,R = qr(As)
    R = R[:-1,:]

    # Construct c
    dn2 = kwad(dn) * ones((n-1, 1))
    dj2 = d[:-1] ** 2
    
    rj2 = []
    for i in range(n-1):
        rj2.append( [kwad(norm(R[:, i]))] )
    rj2 = array(rj2)
            
    c = 0.5 * (dn2 - dj2 + rj2)
    
    # Get solution for the intersection point x
    y = solve(R.T, c)
    
    try:
        z = sqrt( kwad(dn) - kwad(norm(y)) )
    except ValueError:
        raise ValueError('Could only find a solution with imaginary coordinates. This does not mean that there is no real solution (I think).')
    x = dot(Q, vstack((y, z))) + an
    
    return x

x = intersectionpoint(testA, testd)
print("x" + str(x))

