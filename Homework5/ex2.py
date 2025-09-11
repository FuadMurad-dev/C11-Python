import pandas as pd
import numpy as np


np.random.seed(10)

dataframe = pd.DataFrame(
    index = ['A', 'B', 'C', 'D', 'E'],
    columns = ['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1,50,[5,4])
)

menor_30 = dataframe[dataframe['X'] < 30]['X']

media_menor_30 = menor_30.mean()

print(f"Media na coluna X dos elementos menores que 30: ",{media_menor_30})

print("\n")

media_d = dataframe.loc['D'].mean()

print(f"Media da linha D: ", {media_d})

soma_e = dataframe.iloc[4].sum()

print(f"Soma da linha E: ", {soma_e})

print('\n')

dataframe_slice = dataframe.loc[['A', 'C', 'E'], ['X', 'Y']]

print(dataframe_slice)

print('\n')

soma_slice_linha = dataframe_slice.sum(axis= 1)

print(f"Soma das linhas:\n{soma_slice_linha}")



print('\n')

soma_slice_coluna = dataframe_slice.sum(axis= 0)

print(f"Soma das colunas:\n{soma_slice_coluna}")