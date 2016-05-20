# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import random
from operator import itemgetter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import city_level

def get_data():
    #f_r=open('./accumulationfund_raw_data','r')
    f_r=open('./raw_data','r')
    
    data={}
    province_set=[]
    print f_r.readline()
    for line in f_r.readlines():
        line=line.split('\r')[0]
        
        items=line.split('\t')
        province=items[3][0:6]
        if province not in province_set:
            province_set.append(province)
        province_set.sort()
    for item in province_set:
        print item
        
    f_r.close()


def get_salary_data():
    #f_r=open('./accumulationfund_raw_data','r')
    f_r=open('./salary_raw_data','r')
    f_w=open('./raw_data','w')
    data={}
    lines=f_r.readlines()[0]
    lines=lines.split('\r')
    count=0
    print(len(lines))
    for line in lines:
        f_w.write(str(line)+'\n')
        count+=1
        if count%1000==0:
            print count
        
    f_r.close()
    f_w.close()
    
def analysis_salary_data():
    #f_r=open('./salary_raw_data','r')
    f_r=open('./accumulationfund_raw_data','r')

    salary_data={}
    test_data={}
    print f_r.readline()
    c=0
    for line in f_r.readlines():
        line=line.split('\n')[0]
#        print line
        items=line.split('\t')
        
        applycode=items[0]
        if applycode<'A20150803530796':
            continue
        edubg=items[1]
        unitkind=items[2]
        province=items[3][0:6]
        city=items[4]
        companytype=items[5]
        onlinebank=items[7]
        verifiedincome_first=items[8]
        verifiedincome_final=items[9]
        age=items[10][0:len(items[10])-1]
        province=str(city_level.get_city_level(city))
        salary=-1

        if  onlinebank != '' and onlinebank != None and float(onlinebank)!=0:
            onlinebank=float(onlinebank)
            salary=onlinebank
        if verifiedincome_first != '' and verifiedincome_first != None and float(verifiedincome_first)!=0:
            verifiedincome_first=float(verifiedincome_first)
            if salary==-1:
                salary=verifiedincome_first
            else:
                salary=min(salary,verifiedincome_first)
        if verifiedincome_final != '' and verifiedincome_final != None and float(verifiedincome_final)!=0:
            verifiedincome_final=float(verifiedincome_final)
            if salary==-1:
                salary=verifiedincome_final
            else:
                salary=min(salary,verifiedincome_final)

        if salary>=17000 or salary<=0:
            print(applycode,salary)
            continue

    
        ''' 

        if province not in salary_data:
            salary_data[province]=[]
        
        if companytype not in salary_data:
            salary_data[companytype]=[]
    
        if unitkind not in salary_data:
            salary_data[unitkind]=[]
        '''
        if edubg not in salary_data:
            salary_data[edubg]=[]
        salary_data[edubg].append(salary)

    #oprint(salary_data)
    data={}
    for k in salary_data:
        print('k',k)
        data[k]=-1
        data[k]=sum(salary_data[k])/(len(salary_data[k])+0.0)
    y=sorted(data.iteritems(),key=itemgetter(1))
    i=0
    for k in range(0,len(y)):
        print(str(k+1)+'\t'+str(y[k][0])+'\t'+str(y[k][1]))
        #y.append(sum(Y[k])/(len(Y[k]+0.0)))
    #plot_PR_line(salary_data)
    f_r.close()

def plot_PR_line(Y):
    import matplotlib.pyplot as plt2
    plt2.figure()
    #plt2.plot( rec,pre, label='AUC = %0.2f\nKS = %0.2f\n' % (roc_auc, ks_test*100))
    predict = {}
    label={}

    X=[]
    y=[]
    #plt2.plot( X,Y)

    y=[i[1] for i in sorted_label]
    pre=[predict[i[0]] for i in sorted_label]
    #plt2.plot( X,Y)
    plt2.plot( X,y)
    plt2.plot(X,pre)
    #plt2.plot( X, predict_Y, label='prediction')
    plt2.xlabel('policy')
    plt2.ylabel('value')
    plt2.title('loss ration distribution ')
    plt2.legend(loc="lower right")
    
    
   # plt2.xlim([0.0, 1.0])
    #plt2.ylim([-0.5, 5])
    plt2.savefig("./result.png")
    plt2.show()
    
if __name__=='__main__':
    #get_data()
    #get_salary_data()
    analysis_salary_data()
