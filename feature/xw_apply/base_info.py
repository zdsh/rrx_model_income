# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_base_info_feature(base_info):
    feature={}
    sex=-1
    if 'SEX' in base_info:
        sex=base_info['SEX']
    if sex in [0,1,-1]:
        feature['sex']=sex
    else:
        print('sex value error:',sex)
        
    edubg_map={
        10: 6, 
        20: 5,
        40: 4, 
        30: 3, 
        60: 2,
        70: 1,
        None:-1
    }
    edubg=-1
    if 'EDUBG' in base_info:
        if base_info['EDUBG'] in edubg_map:
            edubg=edubg_map[base_info['EDUBG']]
        
    marriage_status=-1
    if 'MARITALSTATUS' in base_info:
        marriage_status=base_info['MARITALSTATUS']

    feature['sex']=sex
    feature['edubg']=edubg
    feature['marriage_status']=marriage_status
    
    return feature
    
