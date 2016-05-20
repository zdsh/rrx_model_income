# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


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
    f_r=open('./salary_raw_data','r')
    #f_r=open('./accumulationfund_raw_data','r')

    salary_data={}
    province_set=[]
    print f_r.readline()

    for line in f_r.readlines():
        line=line.split('\n')[0]
    
#        print line
        items=line.split('\t')
        
        applycode=items[0]
        edubg=items[1]
        unitkind=items[2]
        province=items[3][0:6]
        city=items[4]
        companytype=items[5]
        onlinebank=items[7]
        verifiedincome_first=items[8]
        verifiedincome_final=items[9]
        age=items[10][0:len(items[10])]
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

        if province not in salary_data:
            salary_data[province]={}
        if companytype not in salary_data[province]:
            salary_data[province][companytype]={}
        if unitkind not in salary_data[province][companytype]:
            salary_data[province][companytype][unitkind]={}
        if edubg not in salary_data[province][companytype][unitkind]:
            salary_data[province][companytype][unitkind][edubg]={}
            salary_data[province][companytype][unitkind][edubg]['age']=[]
            salary_data[province][companytype][unitkind][edubg]['salary']=[]

        salary_data[province][companytype][unitkind][edubg]['age'].append(int(age))
        salary_data[province][companytype][unitkind][edubg]['salary'].append(salary)

    for province in salary_data:
        #print(province)
        for companytype in salary_data[province]:
            #print(companytype)
            for unitkind in salary_data[province][companytype]:
                #print(unitkind)
                for edubg in salary_data[province][companytype][unitkind]:
                    age_list=salary_data[province][companytype][unitkind][edubg]['age']
                    salary_list=salary_data[province][companytype][unitkind][edubg]['salary']
                df=pd.DataFrame({'age':age_list,'salary':salary_list})
            #    plt.show(sns.lmplot('age','salary',df))
                sns.lmplot('age','salary',df).savefig('./20160512_fig/'+province+'_'+companytype+'_'+unitkind+'_'+edubg+'.png')

    f_r.close()

if __name__=='__main__':
    #get_data()
    #get_salary_data()
    analysis_salary_data()
