# -*- coding: utf-8 -*-
'''
从loan_info_analysis表中
提取是否有私家车
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#获取申请客户收入信息特征
#是否有私家车:hasCar
def get_loan_info_analysis(loan_info):
    feature = {
        'hasHouse':-1
    }
    if loan_info:
        if 'HASHOUSEINFO' in loan_info.keys() :
            feature['hasHouse'] = int(loan_info['HASHOUSEINFO'])

    return feature



