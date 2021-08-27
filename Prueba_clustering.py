#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Librerías básicas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Clustering
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Warnings
import warnings
warnings.filterwarnings(action='ignore')

# Funciones auxiliares
import funciones as func


# In[2]:


df = pd.read_csv('data.csv')


# In[3]:


df.info()


# In[4]:


df.sample()


# In[5]:


df.describe()


# In[6]:


# Inspección general de los datos de calibración
plt.figure(figsize=(8,5))
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.hist(df[f'setting_{i+1}'])
    plt.title(f'setting_{i+1}')
    plt.axvline(df[f'setting_{i+1}'].mean(), color = 'tomato')
plt.tight_layout()


# In[7]:


df_work = df.drop(columns=['unique_id', 'unit_nr', 'setting_1', 'setting_2', 'setting_3'])


# In[8]:


# Inspección general de los datos de sensores
func.grapher(df_work)


# In[9]:


inertia = []
for i in range(1,11):
    inertia.append(KMeans(n_clusters=i, random_state=11238).fit(df_work).inertia_)


# In[10]:


plt.plot(range(1,11), inertia, 'o-', color='tomato')
plt.xlabel('Cantidad de Cluster')
plt.ylabel('Inercia Estimada')


# In[11]:


# Se reduce la dimensionalidad con PCA
pca = PCA(n_components=2)
pca.fit(df_work)
X_pca = pca.transform(df_work)

print("Ahora el dataframe posee 2 columnas:")
print(X_pca)


# In[12]:


# Entrenamiento K-Means y ajuste con datos con reducción de dimensionalidad
km_model = KMeans(n_clusters=4, random_state=11238)
km_model.fit(X_pca)

# Preparación de los centroides
df_centers = pd.DataFrame(km_model.cluster_centers_, columns=['x', 'y'])


# In[13]:


# Gráfico de los conglomerados formados a partir del modelo entrenado de K-Means
plt.figure(figsize=(20,20))
plt.title('Clusters obtenidos mediante KMeans (en negro se muestran los centroides)', fontsize=20)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=km_model.labels_, s=50, cmap='jet') # Distribución de puntos
plt.scatter(df_centers['x'], df_centers['y'], c='black', s=500, alpha=0.6); # Integración de los centroides

# Etiqueta de cada punto (eliminar si solo quiere verse los puntos sin etiqueta)
dy = 0.04
for i, txt in enumerate(km_model.labels_):
    plt.annotate(txt, (X_pca[i, 0], X_pca[i, 1] + dy))


# In[14]:


# Integración del número de cluster a cada dato respectivo del dataframe principal en el formato estado_{i}
state = []
for i in km_model.labels_:
    state.append(f'estado_{i}')
df['state'] = state


# In[15]:


# Formación del dataframe final en el formato solicitado
df_final = df.loc[:,['unique_id', 'state']]
df_final.head()


# In[17]:


# Exportación final a CSV
df_final.to_csv('cluster_detection.csv', index=False)

