import numbers as np
import pandas as pd

indices = ['a', 'b', 'c', 'd']
valores =[10,20,30,40]

dic = {"a" : 10, 'b' :20 , "c" : 30}

series = pd.Series(index=indices, data = valores)
series2 = pd.Series(dic)

print(series)
print (type(series))
print(series['a'])

#Operacoes entre series

print(series + series2)
print(series - series2)

# fazendo operacao com o valor padrao 

print(series.add(series2, fill_value=0)) # this fill_value sett a default value = 0
print(series.sub(series2, fill_value=0))

#condition pandas 

print(series[series <= 20])

#Data frame pandas
np.random.seed(10)

df =pd.DataFrame(index=['A', 'B', 'C','D'] ,columns=['W', 'X', 'Y','Z'], data= np.random.radient(1,50, [5,4]))

print(df)

#slicing wifh iloc (index numbers)
print(df.iloc[0:2, :])

#slicing wifh loc

print(df.loc[['A', "B"], ['W', "X", "Y", "Z"]])

