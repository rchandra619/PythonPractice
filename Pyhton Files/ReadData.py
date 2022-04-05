import pandas as pd

# def read_csv_file(location):
#     df = pd.read_csv(location)
#     return df
#
#
# def read_excl_file(location):
#     df = pd.read_excel(location)
#     return df
location = 'E:/Captures/Datasets/diabetes.csv'

diabetes = pd.read_csv('E:/Captures/Datasets/diabetes.csv')
print(diabetes.head(5))
ff = diabetes.loc[diabetes['Age'] < 22 ]
print(ff.loc[diabetes['Outcome'] == 1].sort_values('Glucose') , ['BMI'])
diabetes.loc[[255,577] , ['Age'] ] = 50
print(diabetes.iloc[577,7])
print(diabetes.loc[diabetes['Outcome'] == 1].sort_values('Age') , ['BMI'])
print(diabetes.size)
print(ff.size)
