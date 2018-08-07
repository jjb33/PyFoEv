import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns = ['COL1', 'COL2', 'COL3'], index = ['First', 'Second'])
print(df1)

df2 = pandas.DataFrame([{'Name':'John', 'Surname':'Smith'}, {'Name':'Rick'}])
print(df2)

#operating on
print('df1.mean() is: ', df1.mean())
print('df1.mean().mean()) is: ', df1.mean().mean())
