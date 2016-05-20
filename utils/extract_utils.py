# -*- coding: utf-8 -*-
'''
数据抽取模块

'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#从文件中读取字段列表
def get_field_list_from_file(file_name,field_index,separator,hashead=False):
    file  = open(file_name,'r')
    field_list = []
    if hashead==True:
        file.readline()
        line = file.readline()
        while line:
            datas = line.split('\n')[0].split(separator)
            field_list.append(datas[field_index])
            line=file.readline()
    else:
        line = file.readline()
        while line:
            datas = line.split('\n')[0].split(separator)
            field_list.append(datas[field_index])
            line.file.readline()

    return field_list
