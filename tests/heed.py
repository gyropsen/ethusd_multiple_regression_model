import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage

# Загрузка данных
data = sns.load_dataset("iris")

# Просмотр первых строк данных
print(data.head())
print(data.isnull().sum())
print(data.describe())

clean_data = data.drop(["species"], axis=1)

# Вычисление корреляционной матрицы
correlation_matrix = clean_data.corr()

# Вывод корреляционной матрицы
print(correlation_matrix)

# Создание тепловой карты
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", center=0)

# Настройка заголовка и отображение графика
plt.title("Корреляционная матрица для набора данных о цветах ириса")

sns.lmplot(x="sepal_length", y="petal_length", data=data)

sns.pairplot(clean_data)

Z = linkage(correlation_matrix, "ward")
dendrogram(Z)
plt.show()
