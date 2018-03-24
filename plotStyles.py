import matplotlib.pyplot as plt

def blueRedMesh( X, Y, Z, xlabel='x', ylabel='y' ):
    absmax = np.abs(Z).max()
    plt.pcolormesh(X,Y,Z,
                   cmap='RdBu_r', vmin=-absmax ,vmax=absmax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar()

def defaultMesh( X, Y, Z, xlabel='x', ylabel='y'  ):
    plt.pcolormesh(X,Y,Z,cmap='inferno')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar()
