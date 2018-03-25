import matplotlib.pyplot as plt
import numpy as np

def blueRedMesh( X, Y, Z, xlabel='x', ylabel='y', vmax=None):
    absmax = np.abs(Z).max()
    if vmax is None:
        vmax = absmax

    plt.pcolormesh(X,Y,Z,
                   cmap='RdBu_r', vmin=-vmax ,vmax=vmax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar()

def defaultMesh( X, Y, Z, xlabel='x', ylabel='y', vmin=None, vmax=None  ):
    plt.pcolormesh(X,Y,Z,cmap='inferno',vmin=vmin, vmax=vmax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar()
