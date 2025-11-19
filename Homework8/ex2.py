import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

dataset = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/co2_emissions.csv", delimiter=',', index_col='Year', parse_dates=True)

dataset['CO2_Emissions'] = dataset['CO2_Emissions'].astype(float)

plt.figure()

dataset['CO2_Emissions'].plot(figsize=(8,6), title="CO2 Emissions")

decomp_co2 = seasonal_decompose(dataset['CO2_Emissions'], model='additive', period=1)

decomp_co2.plot()
plt.show()

# Respostas:
# A) A serie possui Tendência? Sim, a serie apresenta uma tendencia decrescente ao longo dos anos.

# B) A serie possui Sazonalidade? Não, a serie nao apresenta sazonalidade.

# C) A serie possui Ciclos? Sim, e possivel notar que existem ciclos nessa time series, 
#    podem estar relacionados com acontecimentos e fatores externos. 