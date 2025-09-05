import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
boston = fetch_openml(name='boston', version=1, as_frame=True)
df_boston = boston.frame

df_sample = df_boston.sample(n=300, random_state=4713)
print(df_sample.head())

print(df_sample.describe())

plt.figure(figsize=(10,6))
sns.heatmap(df_sample.corr(), cmap="coolwarm", annot=False)
plt.show()

df_sample.hist(figsize=(12,8))
plt.show()

sns.scatterplot(x="LSTAT", y="MEDV", data=df_sample)
plt.title('Gráfico de dispersión: LSTAT vs MEDV')
plt.show()

