import pandas as pd
import plotly.express as px
import ast
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ruta_csv = os.path.join(BASE_DIR, '..', '..', 'Datos', 'BenjaminUrrutia', 'tmdb_5000_movies.csv')

df = pd.read_csv(ruta_csv)

def obtener_generos(json_str):
    try:
        lista_generos = ast.literal_eval(json_str)
        return [g['name'] for g in lista_generos]
    except:
        return []


df['lista_generos'] = df['genres'].apply(obtener_generos)

df_exploded = df.explode('lista_generos')

genre_analysis = df_exploded.groupby('lista_generos').agg(
    count=('lista_generos', 'count'),
    avg_revenue=('revenue', 'mean')
).reset_index()

fig = px.treemap(
    genre_analysis, 
    path=['lista_generos'], 
    values='count',      
    color='avg_revenue', 
    color_continuous_scale='RdBu', 
    title='Análisis de Géneros: Tamaño por Cantidad, Color por Recaudación Promedio',
    labels={'count': 'N° de Películas', 'lista_generos': 'Género', 'avg_revenue': 'Recaudación Promedio'}
)

fig.show()