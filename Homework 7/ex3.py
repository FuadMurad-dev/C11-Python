import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds = pd.read_csv("C:/Users/murad/OneDrive/Documentos/C11-Python/space.csv" , delimiter= ";")

company_roscomos = ds[ds["Company Name"].str.contains("Roscosmos")]

status_success = company_roscomos[company_roscomos["Status Mission"] == "Success"].count()

status_fail = company_roscomos[company_roscomos["Status Mission"] == "Failure"].count()

x = status_success["Status Mission"]
y = status_fail["Status Mission"]

plt.pie([x, y], labels= ["Sucesso", "Falha"], autopct= "%1.1f%%")

plt.title("Status missions Roscomos")
plt.show()