import pandas as pd
df = pd.read_csv('lunch_box.csv', sep=',')
df.head(3)
print(df.head(3))

df.head()
print(df.head())

df.tail()
print(df.tail())

print('dataframeの行数・列数の確認==>\n', df.shape)
print('indexの確認==>\n', df.index)
print('columnの確認==>\n', df.columns)
print('dataframeの各列のデータ型を確認==>\n', df.dtypes)