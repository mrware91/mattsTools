import matplotlib.font_manager as font_manager

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# matplotlib.rc('font', family='serif')
# matplotlib.rc('font', serif='CMU Serif')
matplotlib.rcParams.update({'font.size': 10})

matplotlib.rcParams['mathtext.fontset'] = "cm"
matplotlib.rcParams['font.serif'] = "CMU Serif"
# # Then, "ALWAYS use sans-serif fonts"
matplotlib.rcParams['font.family'] = "serif"
# matplotlib.rcParams['font.family'] = prop.get_name()

def blueRedMesh( X, Y, Z, xlabel='x', ylabel='y', vmax=None):
    absmax = np.abs(Z).max()
    if vmax is None:
        vmax = absmax

    plt.pcolormesh(X,Y,Z,
                   cmap='RdBu_r', vmin=-vmax ,vmax=vmax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    cbar = plt.colorbar()
    return cbar

def defaultMesh( X, Y, Z, xlabel='x', ylabel='y', vmin=None, vmax=None  ):
    plt.pcolormesh(X,Y,Z,cmap='inferno',vmin=vmin, vmax=vmax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    cbar = plt.colorbar()
    return cbar


def defaultCycleColors():
    colorCycle = matplotlib.rcParams['axes.prop_cycle']
    cycleColors = []
    for c in colorCycle:
        cycleColors.append(c['color'])
    return cycleColors


def generateTickLabels( ticks ):
    n = getLargestOrder(ticks)
    return [printTexFloatFor(tick,n) for tick in ticks]

def generateAxisLabel( label, n, units ):
    # if n == 1:
    #     return r'%s ($\times10$ %s)' % ( label, units )
    if (n==0)|(n==1):
        if (len(units)==0):
            return r'%s' % (label)
        else:
            return r'%s (%s)' % (label, units)
    else:
        return r'%s ($\times10^{%d}$ %s)' % ( label, n, units )

def generateTicks( data, nTicks, dMin = None, dMax = None ):
    if dMin is None:
        dMin = data.min()
    if dMax is None:
        dMax = data.max()

    ticks = np.linspace(dMin, dMax, nTicks)

    if ( dMin < 0 ) & ( dMax > 0 ):
        ticks = ticks - ticks[ np.abs(ticks).argmin() ]

    return ticks


def linePlot( xData, yData,
              nxTicks=5, nyTicks=5,
              xUnits='', yUnits='',
              xLabel='x', yLabel='y',
              xLims=[None,None],
              yLims=[None,None],
              newFigure=True,
              xIn=3, yIn=2, dpi=300,
              plotOptions={}):

    if newFigure:
        plt.figure(figsize=(xIn, yIn), dpi=dpi)

    plt.plot(xData, yData, **plotOptions)
    generateAxes(xData, yData, nxTicks=nxTicks, nyTicks=nyTicks,
                 xUnits=xUnits, yUnits=yUnits, xLabel=xLabel, yLabel=yLabel,
                 xLims=xLims, yLims=yLims)

def colorPlot( xData, yData, zData,
              nxTicks=5, nyTicks=5, nzTicks=5,
              xUnits='', yUnits='', zUnits='',
              xLabel='x', yLabel='y', zLabel='z',
              xLims=[None,None],
              yLims=[None,None],
              zLims=[None,None],
              newFigure=True,
              xIn=3, yIn=3, dpi=300,
              plotOptions={}):

    if newFigure:
        plt.figure(figsize=(xIn, yIn), dpi=dpi)

    cbar = defaultMesh( xData, yData, zData, xlabel='x', ylabel='y', vmin=None, vmax=None  )

    generateColorbar( cbar, zData, ncTicks=nzTicks, cUnits=zUnits, cLabel=zLabel, cLims=zLims )

    generateAxes(xData.flatten(), yData.flatten(), nxTicks=nxTicks, nyTicks=nyTicks,
                 xUnits=xUnits, yUnits=yUnits, xLabel=xLabel, yLabel=yLabel,
                 xLims=xLims, yLims=yLims)

def generateColorbar( cbar, cData, ncTicks=5, cUnits='', cLabel='z', cLims=[None,None] ):
    cTicks = generateTicks( cData, ncTicks, dMin=cLims[0], dMax=cLims[1] )
    cbar.set_ticks( cTicks )
    cbar.set_ticklabels( generateTickLabels( cTicks ) )
    ncMax = getLargestOrder( cTicks )

    plt.title( generateAxisLabel( cLabel , ncMax , cUnits ) )

    if cLims[0] is not None:
        plt.clim(np.array(cLims)*1.1)

def generateAxes(xData, yData,
              nxTicks=5, nyTicks=5,
              xUnits='', yUnits='',
              xLabel='x', yLabel='y',
              xLims=[None,None],
              yLims=[None,None]):
    # Get current axes
    ax = plt.gca()

    # Set the x axes
    xTicks = generateTicks( xData, nxTicks, dMin=xLims[0], dMax=xLims[1] )
    ax.set_xticks( xTicks )
    ax.set_xticklabels( generateTickLabels(xTicks) )


    # Set the y axes
    yTicks = generateTicks( yData, nyTicks, dMin=yLims[0], dMax=yLims[1] )
    ax.set_yticks( yTicks )
    ax.set_yticklabels( generateTickLabels(yTicks) )


    nxMax = getLargestOrder(xTicks)
    nyMax = getLargestOrder(yTicks)

    plt.xlabel( generateAxisLabel( xLabel, nxMax, xUnits ) )
    plt.ylabel( generateAxisLabel( yLabel, nyMax, yUnits ) )

    if xLims[0] is not None:
        absMax = np.abs(xLims).max()
        buffer = 0.1*absMax
        plt.xlim([xLims[0]-buffer,xLims[1]+buffer])
    if yLims[0] is not None:
        absMax = np.abs(yLims).max()
        buffer = 0.1*absMax
        plt.ylim([yLims[0]-buffer,yLims[1]+buffer])

def savefig( name ):
    plt.savefig( name , bbox_inches='tight' )

# Texifying text
def printFloat( f , d=2 ):
    return ('%.'+str(d)+'f')%f

def printTexFloat( f ):

    if f == 0.:
        return r'$0.0$'

    n = getOrder( f )
    if ( n > 1 ) | ( n < -1 ):
        front = ('%.1f' % (f/10**n))
        return r'$%s\times10^%d$' % (front,n)
    elif ( n == -1 ):
        return r'$%.2f$'%f
    elif ( n == 1 ):
        return r'$%.0f$'%f
    else:
        return r'$%.1f$'%f

def printTexFloatFor( f , n ):
    if f == 0.:
        return r'0.0'
    elif n == 1:
        if np.abs(f) == 10:
            front = (r'%.0f' % (f))+'.'
        else:
            front = (r'%.1f' % (f))
        return front
    else:
        front = (r'%.1f' % (f/10**n))
        return front

def getLargestOrder( floatList ):
    nmax = None
    for f in floatList:
        if f == 0:
            continue

        if nmax is None:
            nmax = getOrder(f)
        else:
            n = getOrder(f)
            if n > nmax:
                nmax = n
    return nmax


def getOrder( f ):
    n = 0
    f = np.abs(f)
    if ( f >= 10 ):
        while f >= 10:
            f = f/10.
            n += 1
    elif ( f < 1 ):
        while f <= 1:
            f = f*10.
            n -= 1
    return n


#
