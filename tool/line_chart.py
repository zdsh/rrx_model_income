# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from pylab import *

def plot_chart_line_test(feature_value, salary_value,data, title):
    mpl.rcParams['font.sans-serif']=['SimHei']

    key_list=[k for k in set(feature_value)]
    key_list.sort()
    
    value_list=[]
    t_x=[]
    y=[]
    for k in key_list:
        y.append(data[k])
        t_x.append(str(k))
        value=[]
        for i in range(0,len(feature_value)):
            if feature_value[i]==k:
                value.append(salary_value[i])
        value_list.append(np.mean(value))
    
    #plt.figure() 
    f,axarr=plt.subplots(2,sharex=True)
    #plt.step(axarr,  xticks=key_list, xticklabels=t_x)
    axarr[0].set_title(title+'-分布占比')
    axarr[0].set_ylabel('percent')

    #axarr[0].set_xticklabels(t_x,rotation=90)

    axarr[0].hist(range(len(y)), weights=y,bins=range(len(key_list)+1), normed=True )
    #axarr[0].se
    #ax=plt.axes([np.min(value_list)-1000,np.max(value_list)+2000,0,len(value_list)+1])
    
    #plt.title(title)
    #ax=plt.axes([np.min(value_list)-1000,np.max(value_list)+2000,0,len(value_list)+1])
    #ax.set_xticklabels(t_x,rotation=90)
    axarr[1].set_xticks(range(len(t_x)))
    axarr[1].set_xticklabels(t_x,rotation=90)
    axarr[1].set_title(title+'-坏账率')
    axarr[1].set_xlabel(title)
    axarr[1].set_ylabel('claim percent')
    axarr[1].plot(value_list,'-*')
    
    
    print(key_list)
    print(y)
    print(np.sum(y))
    print(value_list)
    
    #plt.show()
    '''
    ax=f.axes([0.1,0.1,0.8,0.8])
    ax.set_xticks(np.arange(0,len(value_list)+1,1))
    ax.set_xticklabels(t_x,rotation=90)
    '''
    
    plt.savefig('../external/ldys_data/result/'+title+'.png', dpi=300)
    

def plot_chart_line(feature_value, salary_value,title):
    
    mpl.rcParams['font.sans-serif']=['SimHei']

    key_list=[k for k in set(feature_value)]
    key_list.sort()
    
    value_list=[]
    t_x=[]
    for k in key_list:
        t_x.append(str(k))
        value=[]
        for i in range(0,len(feature_value)):
            if feature_value[i]==k:
                value.append(salary_value[i])
        value_list.append(np.mean(value))
    
    #plt.figure()
    ax=plt.axes([0.1,0.1,0.8,0.8])
   
    #ax=plt.axes([np.min(value_list)-1000,np.max(value_list)+2000,0,len(value_list)+1])
    ax.set_xticks(np.arange(0,len(value_list)+1,1))
    ax.set_xticklabels(t_x,rotation=90)

    plt.title(title)
    plt.plot(value_list,'-*')
    #plt.show()
    plt.savefig('../external/ldys_data/test/'+title+'.png')
    plt.close()