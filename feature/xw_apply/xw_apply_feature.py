# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from base_info import get_base_info_feature
from pro_info import get_pro_info_feature
from loaninfo_analysis import get_loan_info_analysis
from apply_customer_income_info import get_apply_customer_income_info
def append_feature(feature,append_feature):
    for k in append_feature:
        feature[k]=append_feature[k]
    return feature

def get_xw_apply_feature_dic(xw_apply_info):
    
    feature = {}
     
    if 'APPLY_CUSTOMER_BASE_INFO' in xw_apply_info:
        base_info_feature = get_base_info_feature(xw_apply_info['APPLY_CUSTOMER_BASE_INFO'])
        append_feature(feature,base_info_feature)
    if 'APPLY_CUSTOMER_PRO_INFO' in xw_apply_info:
        pro_info_feature = get_pro_info_feature(xw_apply_info['APPLY_CUSTOMER_PRO_INFO'])
        append_feature(feature,pro_info_feature)
    if 'APPLY_CUSTOMER_INCOME_INFO' in xw_apply_info:
        apply_customer_income_feature=get_apply_customer_income_info(xw_apply_info['APPLY_CUSTOMER_INCOME_INFO'])
        append_feature(feature,apply_customer_income_feature)
    if 'LOANINFO_ANALYSIS' in xw_apply_info:
        loaninfo_analysis_feature=get_loan_info_analysis(xw_apply_info['LOANINFO_ANALYSIS'])
        append_feature(feature,loaninfo_analysis_feature)

    #print(feature)
    return feature
