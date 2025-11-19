import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

dataset = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/airtravel.csv", delimiter=',', parse_dates=True, index_col='Date')

air_series = dataset['Passengers']

plt.figure(figsize=(10,4))
air_series.plot(title='Air Travel Passengers')
plt.show()

decomp_air = seasonal_decompose(air_series, model='additive')

decomp_air.plot()
plt.show()

#Respostas: 

# A) A serie possui Tendência? Sim, a serie possui uma tendencia positiva e linear com o passar do tempo.
#  
# B) A serie possui Sazonalidade? Sim, a serie tem uma sazionalidade. O periodo de sua sazionalidade é anual, 
#    tendo picos notaveis ao longo dos meses de julho e agosto e com baixas no começo do ano. 
#  
# C) A serie possui Ciclos? Sim, a serie possui ciclos anuais, com picos de passageiros em meses especificos do ano.