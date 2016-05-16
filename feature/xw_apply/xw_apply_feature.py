# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from base_info import get_base_info_feature
from pro_info import get_pro_info_feature

def get_xw_apply_feature_dic(xw_apply_info):
    
    base_info={}
    pro_info={}
     
    if 'APPLY_CUSTOMER_BASE_INFO' in xw_apply_info:
        base_info=xw_apply_info['APPLY_CUSTOMER_BASE_INFO']
    if 'APPLY_CUSTOMER_PRO_INFO' in xw_apply_info:
        pro_info=xw_apply_info['APPLY_CUSTOMER_PRO_INFO']
            
    #print( base_info)
    feature=get_base_info_feature(base_info)   
    #print(pro_info)     
    pro_info_feature=get_pro_info_feature(pro_info)
    for k in pro_info_feature:
        feature[k]=pro_info_feature[k]
    print(feature)
    return feature
