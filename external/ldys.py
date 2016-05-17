# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xlrd

from tool.hsitogram import plot_histogram


if __name__=='__main__':
    workbook=xlrd.open_workbook('./ldys_data/ldys_1000.xlsx')
    sheet=workbook.sheet_by_index(0)
    nrows=sheet.nrows
    ncols=sheet.ncols
    
    feature_name=['']
    for i in range(1,ncols):
        feature_name.append(sheet.cell(0,i))
        
    mobile_list=[]
    for i in range(1,nrows):
        mobile_list.append(sheet.cell(i,0))
    print(len(mobile_list))    
        
    for j in range(1,ncols):
        feature_value=[]
        feature_dic={}
        for i in range(1,nrows):
            value=sheet.cell(i,j).value
            if value==None or value=='':
                value=-1
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