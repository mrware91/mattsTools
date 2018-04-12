import numpy as np
from scipy.interpolate import interp1d

def symmeterize( x, y, interp_type='cubic' ):
    if x.min() <= 0:
        raise ValueError('x.min() must be greater than zero.')

    xs = np.array([-x,x]).flatten()
    xs.sort()

    f = interp1d( x , y , kind=interp_type )

    return { 'x':xs , 'y':f(np.abs(xs)) }
