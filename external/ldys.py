# -*- coding: utf-8 -*-
import sys
from Canvas import Line
reload(sys)
sys.setdefaultencoding('utf-8')

import xlrd

from tool.hsitogram import plot_histogram
from tool.line_chart import plot_chart_line

def get_salary_label():
    mobile_salary={}
    f_r=open('./ldys_data/apply_phone_income.txt')
    for line in f_r.readlines():
        line=line.split('\n')[0]
        items=line.split(',')
        if items[1] not in mobile_salary:
            mobile_salary[items[1]]=float(items[2])
        else:
            print(items[1])
    return mobile_salary




def analysis_data():
    
    mobile_salary=get_salary_label()
    
    workbook=xlrd.open_workbook('./ldys_data/ldys_1000.xlsx')
    sheet=workbook.sheet_by_index(0)
    nrows=sheet.nrows
    ncols=sheet.ncols
    
    feature_name=['']
    for i in range(1,ncols):
        feature_name.append(sheet.cell(0,i).value)
        
    mobile_list=[]
    for i in range(1,nrows):
        mobile_list.append(sheet.cell(i,0).value)
    print(len(mobile_list))    
        
    for j in range(1,ncols):
        feature_value=[]
        salary_value=[]
        
        if '金额' not in feature_name[j]:
            continue
        for i in range(1,nrows):
            value=sheet.cell(i,j).value
            if value==None or value=='':
                value=100
            else:
                value=int(value)
            feature_value.append(value)
            if mobile_list[i-1] not in mobile_salary:
                print(mobile_list[i-1])
            else:
                salary_value.append(mobile_salary[mobile_list[i-1]])
        print(len(feature_value), len(salary_value))
        plot_chart_line(feature_value, salary_value,feature_name[j])
        #plot_histogram(feature_dic,feature_name[j])
        #print(len(feature_value))
        
    print(nrows)
    print(ncols)
    
def analysis_data_percent():
    workbook=xlrd.open_workbook('./ldys_data/ldys_1000.xlsx')
    sheet=workbook.sheet_by_index(0)
    nrows=sheet.nrows
    ncols=sheet.ncols
    
    feature_name=['']
    for i in range(1,ncols):
        feature_name.append(sheet.cell(0,i).value)
        print(feature_name[i])
        print(feature_name[i][7:len(feature_name[i])-1])
        
    mobile_list=[]
    for i in range(1,nrows):
        mobile_list.append(sheet.cell(i,0))
    print(len(mobile_list))    
        
    for j in range(1,ncols):
        feature_value=[]
        feature_dic={}
        
        if '金额' not in feature_name[j]:
            continue
        
        for i in range(1,nrows):
            value=sheet.cell(i,j).value
            if value==None or value=='':
                value=100
            else:
                value=int(value)
            feature_value.append(value)
            if value not in feature_dic:
                feature_dic[value]=0
            feature_dic[value]+=1
        plot_histogram(feature_dic,feature_name[j])
        #print(len(feature_value))
            
    print(nrows)
    print(ncols)
    
if __name__=='__main__':
    #get_salary_label()
    #analysis_data()
    analysis_data_percent()