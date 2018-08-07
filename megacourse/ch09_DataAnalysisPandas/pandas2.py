import pandas
import os

print('CWD:')
print(os.getcwd())

print('Files in Directory:')
print(os.listdir())

fp = (str(os.getcwd()) + '\\megacourse\\ch09_DataAnalysisPandas\\')
print('fp: ', fp)

print(os.listdir(fp))

df1 = pandas.read_json(fp + 'supermarkets.json')
df1 = df1.set_index('ID')
print(df1)

#Slice from above df1
print(df1.loc['3':'5', 'Name':'Address']) #didn't work. empty df. Needs order left to right apparently
print(df1.loc['3':'5', 'Address':'Name'])
print('Intersect:\n', df1.loc[3,'Name']) #Intersect uses comma sep. Also, this is a num not a string for index??
print(list(df1.loc[:'Name']))
print('iloc locates by index:\n', df1.iloc[1:3, 1:4])
'''
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing
#print('ix locates by combination of indexes and labels\n', df1.ix[1:'Name'])
'''

'''
dropping rows or columns
'''
print('dropping a row ID = 1:\n', df1.drop(1, 0)) #drop ID 1 and 0 specifies dropping a row, not column
print('dropping colum Country:\n', df1.drop('Country', 1))

print('Get index names:\n', df1.index)
print('Get index names:\n', df1.columns)
print('Get the shape of DataFrame (no of rows and columns:\n', df1.shape)
'''
UPdating and adding and transposing
'''
#Adding
df1['Continent'] = df1.shape[0] * ['North America']
print(df1)

#Updating
df1['Continent'] = df1['Country'] + ', ' + 'North America'
print(df1)

#Transposing
df1_t = df1.T
print(df1_t)




# df2 = pandas.read_excel(fp + 'name+tel+email+website.xlsx', sheet_name=0, header=None)
# print(df2)