# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from region import city_level
from region import province_region

def get_pro_info_feature(pro_info):
    feature={}
    company_add_province=''
    company_add_city=''
    company_type=-1
    
    if 'COMPANYADDRESSPROVINCE' in pro_info:
        company_add_province=pro_info['COMPANYADDRESSPROVINCE'].encode('utf-8')
    if 'COMPANYADDRESSCITY' in pro_info:
        company_add_city=pro_info['COMPANYADDRESSCITY'].encode('utf-8')
    
    #print(company_add_province)
    #print(company_add_city)
    feature['city_level']=city_level.get_city_level(company_add_city)
    feature['region']=province_region.get_province_region(company_add_province)

    #print(feature)
    return feature