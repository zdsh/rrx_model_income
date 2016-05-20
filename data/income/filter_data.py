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
        age=items[10]
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

        if salary>=15000 or salary<=0:
            print(applycode,salary)
            continue

        rand_num=random.randint(1,7)
    
        if rand_num%7==3:
            
            if province not in test_data:
                test_data[province]={}
            if companytype not in test_data[province]:
                test_data[province][companytype]={}
            if unitkind not in test_data[province][companytype]:
                test_data[province][companytype][unitkind]={}
                test_data[province][companytype][unitkind]['age']=[]
                test_data[province][companytype][unitkind]['salary']=[]

            test_data[province][companytype][unitkind]['age'].append(int(age))
            test_data[province][companytype][unitkind]['salary'].append(salary)
            c+=1
            print('c:',c)
            continue

        if province not in salary_data:
            salary_data[province]={}
        if companytype not in salary_data[province]:
            salary_data[province][companytype]={}
        if unitkind not in salary_data[province][companytype]:
            salary_data[province][companytype][unitkind]={}
            salary_data[province][companytype][unitkind]['age']=[]
            salary_data[province][companytype][unitkind]['salary']=[]

        salary_data[province][companytype][unitkind]['age'].append(int(age))
        salary_data[province][companytype][unitkind]['salary'].append(salary)

    test_salary=[]
    predict_salary=[]
    for province in test_data:
        #print(province)
        for companytype in test_data[province]:
            #print(companytype)
            for unitkind in test_data[province][companytype]:
                #print(unitkind)
                if province in salary_data and companytype in salary_data[province] and unitkind in salary_data[province][companytype]:
                    age_list=salary_data[province][companytype][unitkind]['age']
                    salary_list=salary_data[province][companytype][unitkind]['salary']
                    test_age_list=test_data[province][companytype][unitkind]['age']
                    test_salary_list=test_data[province][companytype][unitkind]['salary']
                    for t in range(0,len(test_age_list)):
                        age=test_age_list[t]
                        salary=test_salary_list[t]
                        cnt=0
                        sum_salary=0
                        salary_range=[]
                        for p in range(0,len(age_list)):
                            if abs(age-age_list[p])<=2:
                                cnt+=1
                                salary_range.append(salary_list[p])
                                sum_salary+=salary_list[p]
                        if cnt>0:
                            test_salary.append(test_salary_list[t])
                            #predict_salary.append(salary_range[len(salary_range)/2])
                            predict_salary.append(sum(salary_range)/(len(salary_range)+0.0))
                        else:
                            print('lost------:',province+'\t'+companytype+'\t'+unitkind+'\t'+str(age))

                else:
                    print('lost:',province+'\t'+companytype+'\t'+unitkind)
    #df=pd.DataFrame({'age':age_list,'salary':salary_list})
    #    plt.show(sns.lmplot('age','salary',df))             
    #sns.lmplot('age','salary',df).savefig('./salary_fig/'+province+'_'+companytype+'_'+unitkind+'_'+'.png')
    print(len(test_salary),len(predict_salary))
    plot_PR_line(test_salary,predict_salary)
    f_r.close()

def plot_PR_line(Y, predict_Y):
    import matplotlib.pyplot as plt2
    plt2.figure()
    #plt2.plot( rec,pre, label='AUC = %0.2f\nKS = %0.2f\n' % (roc_auc, ks_test*100))
    predict = {}
    label={}

    X=[]
    for i in range( 0, len(Y)):
        X.append( i)
        predict[i]=predict_Y[i]
        label[i]=Y[i]
    sorted_label=sorted(label.iteritems(),key=itemgetter(1))
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
