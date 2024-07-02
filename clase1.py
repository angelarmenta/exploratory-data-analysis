#developed by Roberto Ángel Meléndez-Armenta
#https://www.youtube.com/@educar-ia

import pandas as pd

# Cargar los datos desde el archivo CSV
file_path = '/Users/angelarmenta/Dropbox/Tec Misantla/2024 - 01 - Verano/MSC/Propedéutico/dataset_salary_2024.csv'
data = pd.read_csv(file_path)

# Mostrar la información general del dataset
print(data.info())

# Mostrar los primeros 5 registros
print(data.head())

# Mostrar nombre de las columnas
print(data.columns)

# Estadísticas descriptivas de las variables
print(data.describe())

# Mostrar las frecuencias de las variables
print(data['company_size'].value_counts())