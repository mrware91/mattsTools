import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# matplotlib.rc('font', family='serif')
# matplotlib.rc('font', serif='CMU Serif')
matplotlib.rcParams.update({'font.size': 10})

matplotlib.rcParams['font.serif'] = "CMU Serif"
# Then, "ALWAYS use sans-serif fonts"
# matplotlib.rcParams['font.family'] = "serif"
matplotlib.rcParams['font.family'] = "CMU Serif"

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
