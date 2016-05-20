# -*- coding: utf-8 -*-
'''
提取收入
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#获取贷款类型
def get_productcode(apply_info):
    productcode = None
    if apply_info:

        if 'PRODUCTCODE' in apply_info.keys() :
            productcode = apply_info['PRODUCTCODE']

    return productcode

def get_submitstaus(apply_info):
    submitstaus = None
    if apply_info:

        if 'SUBMITSTATUS' in apply_info.keys() :
            submitstaus = apply_info['SUBMITSTATUS']
    return submitstaus

#获取发薪方式
def get_payType(loan_info):
    paytype = None
    if loan_info:
        if 'PAYTYPE' in loan_info.keys() :
            paytype = loan_info['PAYTYPE']
    return paytype
#获取终审核实收入
def get_verifiedincome(final_approve_info):
    verifiedincome = None
    if final_approve_info:
        if 'VERIFIEDINCOME' in final_approve_info.keys() :
            verifiedincome = final_approve_info['VERIFIEDINCOME']

    return verifiedincome


#提取收入特征,提取规则:薪金贷,网银发薪,终审核实收入
def get_income_feature(xw_info):
    income = -1

    #获取贷款类型
    if 'APPLY_INFO' in xw_info:
        productcode = get_productcode(xw_info['APPLY_INFO'])
        submitstatus = get_submitstaus(xw_info['APPLY_INFO'])

    #获取发薪
    if 'LOANINFO_ANALYSIS' in xw_info:
        paytype = get_payType(xw_info['LOANINFO_ANALYSIS'])

    if 'FINAL_APPROVE_OPINION' in xw_info:
        verifiedincome = get_verifiedincome(xw_info['FINAL_APPROVE_OPINION'])

    #申请状态必须为2
    if submitstatus == 2 and paytype == 0:
        if productcode =='salary' or productcode =='accumulationFund':
            income = verifiedincome

    return income