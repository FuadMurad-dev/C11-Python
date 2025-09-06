import numpy as np
import pandas as pd


#1)

seriesAno1 = pd.Series({"Java" : 16.25, "C" : 16.04, "Python" : 9.85})
seriesAno2 = pd.Series({"C" : 16.25, "Python" : 16.04, "Java" : 9.85})

#2) 

print("Mostrando a soma das linguagens nos dois anos: ")

print(seriesAno1.add(seriesAno2, fill_value=0))

print("\n")
#3) 

print("Apresentando o aumento e declinio das linguagens: " )

popularidade =  seriesAno2.sub(seriesAno1, fill_value=0)

print(popularidade)

print("\n")

#4)
print("Mostrando as linguagens que teve um crescimento: ")

print(popularidade[popularidade >= 0])

print("\n")
#5)

two_years = popularidade * 2 # linguagem popular daqui a 2 anos 

print("Mostrando a linguagem que mais cresceu em 2 anos: ") 
print(two_years.nlargest(1))