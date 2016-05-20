import pandas as pd

df=pd.read_csv('./accumulationFund_online_bank.tsv',sep='\t')
df=df.rename(columns={'TO_NUMBER(SUBSTR(A.CODE,2,4))-':'AGE'})
data=df.loc[:,['EDUBG','UNITKIND','COMPANYADDRESSPROVINCE','COMPANYTYPE','ONLINEBANK','AGE']]
data.sort_values(['COMPANYADDRESSPROVINCE','UNITKIND','COMPANYTYPE','EDUBG','AGE'])
print data.head()
