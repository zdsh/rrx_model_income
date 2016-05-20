# -*- coding: utf-8 -*-
'''
根据申请号,从MongoDB中提取信用卡额度feature

'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/Users/liben/PycharmProjects/Model_Analysis/rrx_model_income')

from utils import mongo_connect
from feature.pbc import pbc_feature

def get_apply_list_from_file(file_name,index,separator,hashead=False):
    file  = open(file_name,'r')
    apply_list = []
    if hashead==True:
        file.readline()
        line = file.readline()
        while line:
            datas = line.split('\n')[0].split(separator)
            apply_list.append(datas[index])
            line=file.readline()
    else:
        line = file.readline()
        while line:
            datas = line.split('\n')[0].split(separator)
            apply_list.append(datas[index])
            line.file.readline()

    return apply_list


def extract_credit_amount_feature(apply_list,out_file_name):
    #连接数据库
    db=mongo_connect.get_mongo_db('rrx_xwdb', '10.10.159.15', 27017, 'rrx_xw', 'rrx_xw_pass')
    collection = db['xw_users']
    count = 0
    error_count = 0
    out_file = open(out_file_name,'w')
    for apply in apply_list:
        featue={}
        pbc_info={}
        for user in collection.find({'_id':apply}):
            count+=1
            if count ==10:
                 break
             #央行征信feature
            if 'PBC' in user:
                pbc_info=user['PBC']

            try:
                featue = pbc_feature.get_pbc_feature_dic(pbc_info)
                line = apply+'\t'+str(featue['AmountMean'])+'\t'+str(featue['AmountMedian'])+'\t'+str(featue['AmountMax'])+'\t'+str(featue['AmountMin'])
                out_file.write(line+'\n')
            except:
                error_count+=1
                print apply,featue

            if count%100==0:
                print count,error_count
    print count


def extract_data():
    #提取信用卡额度信息
    apply_file = 'salary_raw_data'
    out_file = 'credit_data/salary_credit_amount'
    # apply_file = 'accumulationfund_raw_data'
    # out_file = 'credit_data/accumulationfund_credit_mount'
    index = 0
    separator='\t'
    hashead = True
    apply_list = get_apply_list_from_file(apply_file,index,separator,hashead)
    extract_credit_amount_feature(apply_list,out_file)

#分析信用卡额度和收入的关系
def analysis_credit_income():
    pass

if __name__=='__main__':
    pass



