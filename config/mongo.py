# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

RRX_XW_DB_TRAIN = 'xw_train_data_db'

RRX_MONGO_DB_SETTING = {
    'xw_train_data_db':{
        "host":"10.10.159.15",
        "port":27017,
        "db":"rrx_xwdb",
        "collection":"xw_users",
        "user":"rrx_xw",
        "password":"rrx_xw_pass"
    }  
}