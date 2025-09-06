import numpy as np
import pandas as pd


#1)

seriesAno1 = pd.Series({"Java" : 16.25, "C" : 16.04, "Python" : 9.85})
seriesAno2 = pd.Series({"C" : 16.25, "Python" : 16.04, "Java" : 9.85})

#2) 

porcent = seriesAno1 + seriesAno2

print(porcent)
