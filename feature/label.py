# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append('/Users/liben/PycharmProjects/Model_Analysis/rrx_model_income')


from utils import mongo_connect
from utils import extract_utils
from xw_apply import income

def get_income_label(user):
    label = {
        "income":-1
    }
    if 'XW' in user:
        xw_info = user['XW']
        label['income'] = income.get_income_feature(xw_info)

    return label


# if __name__ == '__main__':

    # db=mongo_connect.get_mongo_db('rrx_xwdb', '10.10.159.15', 27017, 'rrx_xw', 'rrx_xw_pass')
    # collection = db['xw_users']
    #
    # apply_file = '../income/accumulationfund_raw_data'
    # out_file = open('../income/label_accumulationfund','w')
    # field_index = 0
    # hashead = True
    # separator = '\t'
    # applycode_list = extract_utils.get_field_list_from_file(apply_file,field_index,separator,hashead)
    #
    # count = 0
    # out_file.write('applycode'+'\t'+'income'+'\n')
    #
    # for user in collection.find({'_id':{'$in':applycode_list}}):
    #     count+=1
    #     label = get_income_label(user)
    #     applycode = user['_id']
    #     out_file.write(applycode+'\t'+str(label)+'\n')
    #     if count % 100 ==0:
    #         print count
    #
    # print count

