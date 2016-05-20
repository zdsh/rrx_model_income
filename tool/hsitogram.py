# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def plot_histogram(data, title, xlabel='x', ylabel='y'):

    mpl.rcParams['font.sans-serif']=['SimHei']
    x=data.keys()
    x.sort()
    y=[]
    t_x=[]
    for k in x:
        y.append(data[k])
        t_x.append(str(k))
    #print(data)
    #data=np.array(data)
    print(x)
    print(y)
    bar_width=0.15
    
    plt.figure()
    ax=plt.axes([0.1,0.1,0.8,0.8])
    plt.hist(x, weights=y,bins=range(len(x)),normed=True)
    print(title)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    ax.set_xticks(np.arange(0,len(x)+1,1))
    ax.set_xticklabels(t_x, rotation=90)
    print(ax)
    #fig=plt.gcf()
    #plt.show()
    plt.savefig('../external/ldys_data/test/histom_'+title+'.png')
    #plot_url = py.plot_mpl(fig, filename='mpl-basic-histogram')

if __name__=='__main__':
    plot_histogram([],'test')