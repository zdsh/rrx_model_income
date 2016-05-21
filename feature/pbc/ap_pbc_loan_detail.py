# -*- coding: utf-8 -*-
'''
获取PBC中的feature
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/Users/liben/PycharmProjects/Model_Analysis/rrx_model_income')

#from utils import mongo_connect

# 提取贷款信息特征
#房贷额度:HouseLoanAmount
def get_loan_info_feature(loan_detail):
    return_feature={
        'HouseLoanAmount':-99,
        'LoanStatus':-1
        }
    if loan_detail:
        for k,v in loan_detail.items():
            per_loan = v
            #获取贷款类型
            if 'TYPE' in per_loan.keys() :
                loanType = per_loan['TYPE']
            #获取贷款额度
            if 'AMOUNT' in per_loan.keys():
                LoanAmount = per_loan['AMOUNT']
            if 'STATUS' in per_loan.keys():
                loanStatus = per_loan['STATUS']
            #获取房贷额度(暂定获取最后一条记录,以后根据规则修改)
            if loanType in ['11','12','13']:
                return_feature['HouseLoanAmount'] = LoanAmount
                return_feature['LoanStatus'] = loanStatus

    return return_feature
