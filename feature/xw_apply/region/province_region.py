# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

east_region=[
    '北京',
    '天津',
    '河北',
    '上海',
    '江苏',
    '浙江',
    '福建',
    '山东',
    '广东',
    '海南'
]

middle_region=[
    '山西',
    '安徽',
    '江西',
    '河南',
    '湖北',
    '湖南'
]

west_region=[
    '内蒙',
    '广西',
    '重庆',
    '四川',
    '贵州',
    '云南',
    '西藏',
    '陕西',
    '甘肃',
    '青海',
    '宁夏',
    '新疆'
]

north_ease_region=[
    '辽宁',
    '吉林',
    '黑龙'
]

def get_province_region(province):
    region=-1
    if len(province)<6:
        return region
    province=province[0:6]
    if province in east_region:
        region=0
    elif province in middle_region:
        region=1
    elif province in west_region:
        region=2
    elif province in north_ease_region:
        region=3
    else:
        pass
    return region