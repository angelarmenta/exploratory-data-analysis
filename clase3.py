#developed by Roberto Ángel Meléndez-Armenta
#https://www.youtube.com/@educar-ia

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde el archivo CSV
file_path = 'RUTA DEL DATASET'
data = pd.read_csv(file_path)

# Gráfica de distribución para la edad
sns.histplot(data['age'], bins=10, kde=True)
plt.title('Distribución de edades')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Gráfica de distribución para el ingreso anual
plt.figure(figsize=(10, 6))
sns.histplot(data['income'], bins=10, kde=True)
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.title('Distribución de ingreso anual')
plt.show()

# Gráfica de dispersión para el ingreso anual vs el puntaje de gasto
sns.scatterplot(x='income', y='spending_score', data=data, 
                hue='preferred_category')
plt.title('Relación entre income y spending_score')
plt.show()

# Boxplot del income por gendre
sns.boxplot(x='gender', y='income', data=data)
plt.title('Boxplot del income por género')
plt.show()

# Gráfica del ingreso por preferred_category
sns.barplot(x="preferred_category", y="income", data=data)
plt.title('Ingreso por preferred_category')
plt.show()

# Correlación de variables numéricas
var_numericas = data.select_dtypes(include=['int64', 'float64'])
sns.heatmap(var_numericas.corr(), annot=True)
plt.title('Correlación de variables numéricas')
plt.show()

# Gráfica de regresión entre purchase_frequency y spending_score
plt.figure(figsize=(10, 6))
sns.regplot(x='purchase_frequency', y='spending_score', data=data,
            line_kws={"color": "red"})
plt.title('Regresión entre purchase_frequency y spending_score')
plt.show()
