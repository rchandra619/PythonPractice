import pandas as pd

ata = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
       'Age': [27, 24, 22, 32],
       'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
       'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

df = pd.DataFrame(ata)

#print(df.sort_values['Age'])
print(df)
print(list(df.columns))
colu = list(df)

age_list = list(df['Age'])
print(age_list)
print('%'*15)
for i in colu:
    print(df[i],[1])
print('*' * 15)
print(colu)

print(df.loc[df['Age'] > 25])

# for index , row in df.iterrows():
#     if row['Age'] > 25:
#         #print(row['Age'])
#         print(df['Age'])
print('%'*15)
print(df['Age'])