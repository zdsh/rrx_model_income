
import matplotlib.pyplot as plt
import numpy as np


def plot_histogram(data, title, xlabel='x', ylabel='y'):

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
    ax=plt.axes([0.15,0.15,0.75,0.75])
    plt.hist(x, weights=y,bins=range(len(x)),normed=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    ax.set_xticks(np.arange(0,len(x),1))
    ax.set_xticklabels(t_x)
    print(ax)
    #fig=plt.gcf()
    plt.show()
    #plot_url = py.plot_mpl(fig, filename='mpl-basic-histogram')

if __name__=='__main__':
    plot_histogram([],'test')