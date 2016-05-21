# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from ap_pbc_credit_card_detail import get_credit_card_info_feature
from ap_pbc_loan_detail import get_loan_info_feature
def get_pbc_feature_dic(pbc_info):

    feature={}

    #获取信用卡明细
    if 'AP_PBC_CREDIT_CARD_DETAIL' in pbc_info:
        credit_card_feature=get_credit_card_info_feature(pbc_info['AP_PBC_CREDIT_CARD_DETAIL'])
    #提取房贷信息
    if 'AP_PBC_LOAN_DETAIL' in pbc_info:
         house_loan_feature = get_loan_info_feature(pbc_info['AP_PBC_LOAN_DETAIL'])

    for k in credit_card_feature:
        feature[k]=credit_card_feature[k]
    for k in house_loan_feature:
        feature[k]=house_loan_feature[k]
    #print(feature)
    return feature

