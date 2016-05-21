# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/Users/liben/PycharmProjects/Model_Analysis/rrx_model_income')
from utils import mongo_connect
from feature.xw_apply import xw_apply_feature
from feature.pbc import pbc_feature

import label

def get_feature_dic(user):
    feature={}
    xw_apply_info={}
    pbc_info={}
    #小微申请信息
    if 'XW' in user:
        xw_apply_info=user['XW']
    #央行征信信息
    if 'PBC' in user:
        pbc_info=user['PBC']
    #print(xw_apply_info)

    #提取小微申请信息中的feature
    xw_feature=xw_apply_feature.get_xw_apply_feature_dic(xw_apply_info)
    #提取央行征信信息中的feature
    pbc_featue = pbc_feature.get_pbc_feature_dic(pbc_info)
    #提取收入label
    income_label = label.get_income_label(user)

    #合并小微申请和央行征信中的所有的feature
    for k in xw_feature.keys():
        feature[k]=xw_feature[k]
    for k in pbc_featue.keys():
        feature[k]=pbc_featue[k]
    for k in income_label.keys():
        feature[k]=income_label[k]

    return feature


if __name__ == '__main__':
    db=mongo_connect.get_mongo_db('rrx_xwdb', '10.10.159.15', 27017, 'rrx_xw', 'rrx_xw_pass')
    collection = db['xw_users']

    applycode_list=[
        'A2014011600397',
        'A2014011700603'
        ]
    for user in collection.find({'_id':{'$in':applycode_list}}):
        featue = get_feature_dic(user)
        print user
        #break