import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Dados fictícios de clientes
data = {'Renda': [15, 16, 17, 60, 62, 64],
        'Gastos': [39, 41, 37, 8, 9, 10]}
df = pd.DataFrame(data)

# Aplica K-Means
kmeans = KMeans(n_clusters=2, random_state=0).fit(df)
df['Grupo'] = kmeans.labels_

# Visualiza resultado
plt.scatter(df['Renda'], df['Gastos'], c=df['Grupo'], cmap='viridis')
plt.xlabel('Renda (mil R$)')
plt.ylabel('Gastos (mil R$)')
plt.title('Agrupamento de Clientes')
plt.grid(True)
plt.show()