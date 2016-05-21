# -*- coding: utf-8 -*-
'''
从apply_customer_income_info表中
提取是否有私家车
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#获取申请客户收入信息特征
#是否有私家车:hasCar
def get_apply_customer_income_info(apply_customer_income_info):
    feature = {
        'hasCar':-1
    }
    if apply_customer_income_info:
        if 'HASCAR' in apply_customer_income_info.keys() :
            feature['hasCar'] = int(apply_customer_income_info['HASCAR'])

    return feature



