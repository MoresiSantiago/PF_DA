import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
pd.set_option('io.parquet.engine', 'fastparquet')
dfMetadata = pd.read_parquet("data/Cloud Upload/Google Maps/metadata-sitios.snappy.parquet")


def generar_nuevos_bancos(num_new_banks, min_rating):
    # Seleccionar las ubicaciones donde avg_rating es menor al valor especificado
    locations_to_cluster = dfMetadata[dfMetadata['avg_rating'] < min_rating][['latitude', 'longitude']].values

    # Aplicar KMeans para encontrar los centroides
    kmeans = KMeans(n_clusters=num_new_banks, random_state=42)
    kmeans.fit(locations_to_cluster)

    # Obtener las ubicaciones de los nuevos bancos (centroides)
    new_banks_centroids = kmeans.cluster_centers_

    # Crear un DataFrame con las coordenadas de los nuevos bancos
    df_nuevos_bancos = pd.DataFrame({
        'Latitud': new_banks_centroids[:, 0],
        'Longitud': new_banks_centroids[:, 1]
    })


    # # Mapa de dispersión geoespacial con centroides en rojo.
    # plt.figure(figsize=(12, 8))
    # sns.scatterplot(x='longitude', y='latitude', data=dfMetadata, hue='avg_rating', palette='viridis', size='num_of_reviews', sizes=(20, 200))
    # plt.scatter(new_banks_centroids[:, 1], new_banks_centroids[:, 0], c='red', marker='X', s=100, label='Nuevos Bancos')
    # plt.title(f'Nuevos bancos de acuerdo a la insatisfacción del cliente ({num_new_banks} bancos)')
    # plt.xlabel('Longitud')
    # plt.ylabel('Latitud')
    # plt.legend(title='Puntuación Promedio')
    # plt.show()

    return df_nuevos_bancos
