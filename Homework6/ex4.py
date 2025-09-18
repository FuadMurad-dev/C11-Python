import pandas as pd
import numpy as np

ds = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/Ex_class/paises.csv" , delimiter= ";")

cost_zero = ds[ds["Coastline (coast/area ratio)"] == 0]

cost_zero["Country"].to_csv("noCost.csv")