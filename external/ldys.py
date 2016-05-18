# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xlrd

from tool.hsitogram import plot_histogram
from tool.line_chart import plot_chart_line
from tool.line_chart import plot_chart_line_test

def get_label_from_xw_json(data_info ):
    label = 0
    if "APPLY_INFO" in data_info['XW'] and "SUBMITSTATUS" in data_info['XW']["APPLY_INFO"]:
        if data_info['XW']["APPLY_INFO"]["SUBMITSTATUS"] == 2:
            if "TM_RESCHEDULE_ACCT" in data_info['XW']:
                label = 1
            elif "TM_ACCOUNT" in data_info['XW'] and "OVER_DUE_DAYS" in data_info['XW']["TM_ACCOUNT"]:
                if data_info['XW']["TM_ACCOUNT"]["OVER_DUE_DAYS"]>=30:
                    label=1
    return label

def get_salary_label():
    mobile_salary={}
    f_r=open('./ldys_data/apply_phone_income.txt')
    
    from utils import mongo_connect

    db=mongo_connect.get_mongo_db('rrx_xwdb', '10.10.159.15', 27017, 'rrx_xw', 'rrx_xw_pass')
    collection = db['xw_users']

    for line in f_r.readlines():
        line=line.split('\n')[0]
        items=line.split(',')
        applycode=items[0]
        
        for user in collection.find({'_id':applycode}).sort([('_id',-1)]):
            label=get_label_from_xw_json(user)
            #print (user['_id'],label)
            break
        if items[1] not in mobile_salary:
            #mobile_salary[items[1]]=float(items[2])
            mobile_salary[items[1]]=label
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
        feature_dic={}

        #if feature_name[j][len(feature_name[j])-2:] not in ['数量','等级','实名','指数']:
        if feature_name[j][len(feature_name[j])-2:] not in ['年限','帐龄']:
            continue
        #if '金额' not in feature_name[j]:
        #if '余额' not in feature_name[j]:
        #if '笔数' not in feature_name[j]:
            #continue
        for i in range(1,nrows):
            value=sheet.cell(i,j).value
            if value==None or value=='':
                value=100
            else:
                value=float(value)
            if mobile_list[i-1] not in mobile_salary:
                #print('lost:',mobile_list[i-1])
                continue
            else:
                salary_value.append(mobile_salary[mobile_list[i-1]])
        
            feature_value.append(value)

            if value not in feature_dic:
                feature_dic[value]=0
            feature_dic[value]+=1
        print(len(feature_value), len(salary_value))
        #plot_histogram(feature_dic,feature_name[j])
        plot_chart_line_test(feature_value, salary_value, feature_dic, feature_name[j])
        #plot_histogram(feature_dic,feature_name[j])
        #print(len(feature_value))
        #break
        #break
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
        print(feature_name[i][len(feature_name[i])-2:])
        
    mobile_list=[]
    for i in range(1,nrows):
        mobile_list.append(sheet.cell(i,0))
    print(len(mobile_list))    
        
    for j in range(1,ncols):
        feature_value=[]
        feature_dic={}
        
#        if '金额' not in feature_name[j]:
        #if '余额' not in feature_name[j]:
        #if feature_name[j][len(feature_name[j])-2:] not in ['数量','等级','实名','指数']:
        if feature_name[j][len(feature_name[j])-2:] not in ['年限','帐龄']:
            continue
        #if '笔数' not in feature_name[j]:
            #continue
        for i in range(1,nrows):
            value=sheet.cell(i,j).value
            if value==None or value=='':
                value=100
            else:
                value=float(value)
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
    #analysis_data_percent()
    analysis_data()
