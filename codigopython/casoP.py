import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Leer los datos desde un archivo CSV
bigcity = pd.read_csv("C:/Users/sthev/OneDrive/Documentos/bigcity.csv")

# Revisar estructura y posibles valores faltantes
print("Estructura de los datos:")
print(bigcity.info())
print("\nResumen estadístico:")
print(bigcity.describe())

# Visualización inicial para detectar outliers o datos atípicos
print("\nGráfico de puntos para detección de outliers:")
sns.scatterplot(data=bigcity, x='u', y='x')
plt.title("Detección de Outliers en poblaciones de 1920 vs 1930")
plt.show()

# Análisis descriptivo detallado
print("\nAnálisis descriptivo detallado:")
print(bigcity[['u', 'x']].agg(['min', 'quantile', 'median', 'mean', 'quantile', 'max', lambda x: skew(x), lambda x: kurtosis(x)]))

# Histogramas con densidad para examinar la distribución y sesgo
print("\nHistogramas con densidad:")
sns.histplot(data=bigcity, x='u', bins=20, kde=True, alpha=0.6)
sns.histplot(data=bigcity, x='x', bins=20, kde=True, alpha=0.6, color='orange')
plt.title("Distribución de poblaciones con densidad")
plt.legend(['1920', '1930'])
plt.show()

# Diagrama de dispersión mejorado con modelo lineal y línea de identidad
print("\nDiagrama de dispersión con ajuste lineal:")
sns.scatterplot(data=bigcity, x='u', y='x', color='blue')
sns.regplot(data=bigcity, x='u', y='x', scatter=False, color='red')
plt.plot([0, max(bigcity['u'])], [0, max(bigcity['x'])], '--', color='grey')
plt.title("Relación entre población en 1920 y 1930 con ajuste lineal")
plt.xlabel("Población en 1920")
plt.ylabel("Población en 1930")
plt.show()

# Cálculo e interpretación de la correlación
correlation = bigcity['u'].corr(bigcity['x'])
print("\nCorrelación entre la población en 1920 y 1930:", round(correlation, 2))

# Filtrar y visualizar ciudades con cambios inusuales en la población entre 1920 y 1930
# Calcular la diferencia en la población entre 1930 y 1920
bigcity['difference'] = bigcity['x'] - bigcity['u']

# Definir un umbral para identificar cambios inusuales
umbral_inf, umbral_sup = bigcity['difference'].quantile([0.05, 0.95])

# Crear un histograma de las diferencias en la población para todas las ciudades
sns.histplot(data=bigcity, x='difference', bins=20, color='skyblue', kde=True)
plt.axvline(umbral_inf, linestyle='--', color='red')
plt.axvline(umbral_sup, linestyle='--', color='red')
plt.text(umbral_inf - 30, 5, "Umbral inferior", color='red')
plt.text(umbral_sup + 30, 5, "Umbral superior", color='red')
plt.title("Diferencia en población entre 1920 y 1930 para todas las ciudades")
plt.xlabel("Diferencia en población (1930 - 1920)")
plt.ylabel("Frecuencia")
plt.show()


