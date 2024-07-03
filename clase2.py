#developed by Roberto Ángel Meléndez-Armenta
#https://www.youtube.com/@educar-ia

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
import numpy as np

# Cargar los datos desde el archivo CSV
file_path = 'RUTA DEL DATASET'
data = pd.read_csv(file_path)

# Gráfica de barras de la variable company_size
data['company_size'].value_counts().plot(kind='bar')
plt.xlabel('Tamaño de la empresa')
plt.ylabel('Frecuencia')
plt.title('Gráfica de barras de company_size')
plt.show()

# Gráfica de pastel de la variable experience_level
data['experience_level'].value_counts().plot(kind='pie')
plt.show()

# Histograma de frecuencia de la variable salary_in_usd
plt.hist(data['salary_in_usd'], bins=10)
plt.xlabel('Salario en USD')
plt.ylabel('Frecuencia')
plt.title('Histograma')
plt.show()

# Boxplot de la variable salary_in_usd
fig, ax = plt.subplots()
ax.boxplot(data['salary'])
plt.ylabel('Salario en USD')
plt.title('Boxplot de salary_in_usd')
plt.show()

# Boxplot de las variables salary y salary_in_usd en diferentes subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.boxplot(data['salary'])
ax1.set_ylabel('Salario')
ax1.set_title('Salary')
ax2.boxplot(data['salary_in_usd'])
ax2.set_ylabel('Salario en USD')
ax2.set_title('Salary in USD')
ax3.hist(data['salary_in_usd'], bins=10)
ax3.set_ylabel('Frecuencia')
ax3.set_title('Histograma (Salary in USD)')
plt.show()

# Gráfica de barras horizontales de job_title y salary_in_usd
average_salary_in_usd = data.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=True)
top_10_jobs = average_salary_in_usd.head(10)
top_10_jobs.plot(kind='barh')
plt.xlabel('Salario en USD')
plt.ylabel('Job')
plt.title('Salario promedio por Job')
plt.show()

# Line plot de work_year con media de salary_in_usd
average_salary_by_work_year = data.groupby('work_year')['salary_in_usd'].mean()
plt.plot(average_salary_by_work_year.index, average_salary_by_work_year.values,'o-')
plt.xlabel('Año')
plt.ylabel('Salario promedio en USD')
plt.title('Relación entre año y salario promedio en USD')
plt.show()

# Histograma de frecuencia de la variable salary_in_usd con línea de distribución
plt.hist(data['salary_in_usd'], bins=10, density=True, alpha=0.7)
plt.xlabel('Salario en USD')
plt.ylabel('Frecuencia')
plt.title('Histograma de frecuencia (salario en USD)')
# Ajustar una distribución normal a los datos
mu, sigma = norm.fit(data['salary_in_usd'])
x = np.linspace(min(data['salary_in_usd']), max(data['salary_in_usd']), 100)
y = norm.pdf(x, mu, sigma)
plt.plot(x, y, '-', linewidth=2)
plt.legend(['Distribución normal'])
plt.show()



