# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
banks=pd.read_csv(path)
categorical_var=banks.select_dtypes(include='object')
print(categorical_var)
numerical_var=banks.select_dtypes(include='number')
print(numerical_var)
banks.drop('Loan_ID',axis=1,inplace=True)
print(banks.isnull().sum())
bank_mode=banks.mode()
print(bank_mode)
banks.fillna(bank_mode,inplace=True)
print(banks)
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)
loan_approved_se=len(banks[(banks['Self_Employed']=="Yes")&(banks['Loan_Status']=='Y')])
loan_approved_nse=len(banks[(banks['Self_Employed']=="No")&(banks['Loan_Status']=='Y')])
percentage_se=loan_approved_se*100/614
percentage_nse=loan_approved_nse*100/614
banks['loan_term']=banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=len(banks[banks['loan_term']>=25])
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome','Credit_History']
mean_values=loan_groupby.agg({'ApplicantIncome':np.mean})
#Code starts here




