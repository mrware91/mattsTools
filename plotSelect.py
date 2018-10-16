import matplotlib.pyplot as plt

################################################################################
#~~~~~~~~~Default cycler
################################################################################
from cycler import cycler

def setLineCycler():
    ax = plt.gca()

    colors = ['k','k','k','k','k','k','k','k']
    linestyles = ['-','-','--','--',':',':','-.','-.']

    mycycler = cycler('linestyle', linestyles) + cycler('color',colors)

    # plt.rc('axes',prop_cycle=mycycler)
    ax.set_prop_cycle( mycycler )
    
################################################################################
#~~~~~~~~~Plot line, log, or errorbar
################################################################################
def plotSelect(plotType, newFigure, xData, yData, yerr=None, **plotOptions):
    
    if (plotType == 0) or (plotType is 'line'):
        plt.plot(xData, yData, **plotOptions)

    elif (plotType == 1) or (plotType is 'log'):
        plt.semilogy(xData, yData, **plotOptions)
    
    elif (plotType == 2) or (plotType is 'err'):
        plt.errorbar(xData, yData, yerr, fmt='none', **plotOptions)
        if newFigure:
            setLineCycler()
        plt.plot(xData, yData, **plotOptions)
        
    else:
        print('invalid plot type')