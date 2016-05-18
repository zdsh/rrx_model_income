# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from credit_card_info import get_credit_card_info_feature

def get_pbc_feature_dic(pbc_info):

    feature={}
    credit_card_info={}

    if 'AP_PBC_CREDIT_CARD_DETAIL' in pbc_info:
        credit_card_info=pbc_info['AP_PBC_CREDIT_CARD_DETAIL']

    credit_card_feature=get_credit_card_info_feature(credit_card_info)
    for k in credit_card_feature:
        feature[k]=credit_card_feature[k]
    print(feature)
    return feature
