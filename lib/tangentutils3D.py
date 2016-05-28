from math import pow, sqrt
from numpy import array, tile, ones, zeros, dot, vstack, hstack
from scipy.linalg import qr, norm, solve
from utils import *
from geoutils3D import *
from sphere import *


def adjsphere(sphere1,sphere2,sphere3,newr,sens):

    c1 = sphere1.center()
    c2 = sphere2.center()
    c3 = sphere3.center()

    A = array([[c1.x(),c2.x(),c3.x()], [c1.y(),c2.y(),c3.y()], [c1.z(),c2.z(),c3.z()] ])
    d = array([[newr+sphere1.r()], [newr+sphere2.r()], [newr+sphere3.r()]])

    def kwad(x): return pow(x, 2)

    def distance(x,y):
        '''Distance between two points x,y'''
        def diff(x):
            return pow(x[0]-x[1], 2)
        if len(x) != len(y):
            raise ValueError('x and y must be vectors of the same length: %d != %d' %(len(x), len(y)))
        
        return sqrt(sum( map(diff, zip(x,y)) ) )


    def intersectionpoint(A, d, sens):
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
            z = sens * sqrt( kwad(dn) - kwad(norm(y)) )
        except ValueError:
            raise ValueError('Could only find a solution with imaginary coordinates. This does not mean that there is no real solution (I think).')
        x = dot(Q, vstack((y, z))) + an
    
        return x

    newcenter = intersectionpoint(A,d,sens)
    return Sphere(Point3D(newcenter[0][0],newcenter[1][0],newcenter[2][0]),newr)
