import pandas as pd
import numpy as np

ds = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/Ex_class/paises.csv" , delimiter= ";")

def saude (deathrate):

    if deathrate < 9:
        return "Balanced"
    
    else:
        return "Urgent"
    
ds["Humanitarian Help"] = ds["Deathrate"].apply(saude)

print(ds["Humanitarian Help"])