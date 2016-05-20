# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from utils import mongo_connect
from feature.xw_apply import xw_apply_feature
from feature.pbc import pbc_feature

def get_feature_dic(user):
    feature={}
    xw_apply_info={}
    pbc_info={}
    if 'XW' in user:
        xw_apply_info=user['XW']
    if 'PBC' in user:
        pbc_info=user['PBC']
    #print(xw_apply_info)
    xw_feature=xw_apply_feature.get_xw_apply_feature_dic(xw_apply_info)
    pbc_featue = pbc_feature.get_pbc_feature_dic(pbc_info)
    for k in xw_feature.keys():
        feature[k]=xw_feature[k]

    for k in pbc_featue.keys():
        feature[k]=pbc_featue[k]

    print(feature)
    return feature


if __name__ == '__main__':
    db=mongo_connect.get_mongo_db('rrx_xwdb', '10.10.159.15', 27017, 'rrx_xw', 'rrx_xw_pass')
    collection = db['xw_users']
    
    applycode_list=[
        'A20160304864714',
        'A20160307866631'
        ]
    for user in collection.find({'_id':{'$in':applycode_list}}):
        get_feature_dic(user)
        print user
        #break