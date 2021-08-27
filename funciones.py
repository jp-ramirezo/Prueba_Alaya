# Librerías básicas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Clustering
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

##################################################

def grapher(dataframe):
    '''
    Devuelve una serie de gráficos de los diferentes valores asociados a sensores (float o integer), mostrando una línea roja que representa la media de los datos.

    Argumentos:
    - dataframe: Dataframe a analizar.
    '''

    fig, axs = plt.subplots(3,7, figsize=(30,10))
    for i in range(3):
        if i == 0:
            for j in range(7):
                axs[i,j].hist(dataframe[f's_{j+1}'])
                axs[i,j].set_title(f's_{j+1}')
                axs[i,j].axvline(dataframe[f's_{j+1}'].mean(), color = 'tomato')
        elif i == 1:
            for j in range(7):
                axs[i,j].hist(dataframe[f's_{j+8}'])
                axs[i,j].set_title(f's_{j+8}')
                axs[i,j].axvline(dataframe[f's_{j+8}'].mean(), color = 'tomato')
        elif i == 2:
            for j in range(7):
                axs[i,j].hist(dataframe[f's_{j+15}'])
                axs[i,j].set_title(f's_{j+15}')
                axs[i,j].axvline(dataframe[f's_{j+15}'].mean(), color = 'tomato')

def kmeans_clustering_map(clusters, fit_transformed, labels = False):
    '''
    Devuelve una gráfico de dispersión de puntos con los conglomerados generados mediante K-Means, a partir de una matriz de datos tratada con reducción de dimensionalidad. Para cada conglomerado, se muestra su centroide (en escala de negro transparente).
    Argumentos:
    - clusters: número de conglomerados a formar.
    - fit_transformed: matriz de datos sometida a reducción de dimensionalidad en forma previa.
    - labels: Si es True, etiqueta cada uno de los puntos con el número del conglomerado al que pertenece (False por defecto).
    '''
    km_model = KMeans(n_clusters=clusters, random_state=11238)

    # K-means (from number of features in input matrix to n_clusters)
    km_model.fit(fit_transformed)
    df_centers = pd.DataFrame(km_model.cluster_centers_, columns=['x', 'y'])

    plt.figure(figsize=(20,20))
    plt.title('Clusters obtenidos mediante KMeans (en negro se muestran los centroides)', fontsize=15)
    plt.scatter(fit_transformed[:, 0], fit_transformed[:, 1], c=km_model.labels_, s=50, cmap='jet')
    plt.scatter(df_centers['x'], df_centers['y'], c='black', s=500, alpha=0.6);
    
    if labels == True:
        dy = 0.04
        for i, txt in enumerate(km_model.labels_):
            plt.annotate(txt, (fit_transformed[i, 0], fit_transformed[i, 1] + dy))