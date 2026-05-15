import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Datos proporcionados (copiados manualmente para este entorno)
data = {
    "Marca temporal": ["11/5/2026 21:08:41", "11/5/2026 21:09:15", "11/5/2026 21:21:08", "11/5/2026 21:21:30", 
                       "11/5/2026 21:23:03", "11/5/2026 21:24:01", "11/5/2026 21:24:44", "11/5/2026 21:27:02", 
                       "11/5/2026 21:28:34", "11/5/2026 21:29:05", "11/5/2026 21:35:03", "11/5/2026 21:39:57", 
                       "11/5/2026 21:47:55", "11/5/2026 21:50:18", "11/5/2026 22:10:10", "11/5/2026 23:23:02", 
                       "12/5/2026 0:13:07", "12/5/2026 0:57:56", "12/5/2026 8:49:43", "12/5/2026 9:03:17", 
                       "12/5/2026 10:12:21", "12/5/2026 11:37:57", "12/5/2026 11:46:40", "12/5/2026 11:47:43", 
                       "12/5/2026 11:52:48", "12/5/2026 12:16:46", "12/5/2026 12:20:02", "12/5/2026 12:47:05", 
                       "12/5/2026 13:45:32"],
    "Género": ["Ciencia ficción", "Ciencia ficción", "Acción", "Comedia", "Ciencia ficción", "Drama", "Terror", "Acción", 
               "Animación", "Comedia", "Terror", "Ciencia ficción", "Ciencia ficción", "Comedia", "Drama", "Comedia", 
               "Animación", "Comedia", "Comedia", "Drama", "Animación", "Acción", "Ciencia ficción", "Ciencia ficción", 
               "Terror", "Terror", "Terror", "Comedia", "Drama"],
    "Frecuencia": ["una vez cada 3 meses", "una vez cada 3 meses", "una vez al año", "una vez cada 3 meses", "una vez al año", 
                   "Una vez al mes", "una vez al año", "una vez cada 3 meses", "una vez al año", "una vez al año", 
                   "una vez al año", "una vez cada 3 meses", "una vez al año", "una vez cada 3 meses", "una vez al año", 
                   "Una vez al mes", "una vez cada 3 meses", "una vez al año", "una vez cada 3 meses", "una vez al año", 
                   "una vez cada 3 meses", "Una vez por semana", "una vez cada 3 meses", "una vez al año", "una vez al año", 
                   "una vez cada 3 meses", "Una vez al mes", "Una vez al mes", "una vez cada 3 meses"],
    "Ganancias=Buena": ["No", "Depende del caso", "No", "No", "Depende del caso", "No", "No", "No", "Depende del caso", 
                        "No", "No", "Sí", "No", "No", "No", "No", "No", "No", "No", "No", "Depende del caso", "No", 
                        "Depende del caso", "Depende del caso", "No", "Depende del caso", "No", "No", "Depende del caso"],
    "Influencia": ["Popularidad / tendencia", "Actores o director", "Actores o director", "Actores o director", "Tráiler", 
                   "Popularidad / tendencia", "Tráiler", "Actores o director", "Recomendaciones de amigos", "Recomendaciones de amigos", 
                   "Tráiler", "Actores o director", "Popularidad / tendencia", "Actores o director", "Redes sociales", "Redes sociales", 
                   "Redes sociales", "Recomendaciones de amigos", "Recomendaciones de amigos", "Popularidad / tendencia", 
                   "Popularidad / tendencia", "Críticas y reseñas", "Redes sociales", "Actores o director", "Tráiler", 
                   "Popularidad / tendencia", "Tráiler", "Críticas y reseñas", "Tráiler"]
}
df = pd.DataFrame(data)

# Mapeo de frecuencia a veces por año
freq_map = {
    "Una vez por semana": 52,
    "Una vez al mes": 12,
    "una vez cada 3 meses": 4,
    "una vez al año": 1
}
df["frecuencia_anual"] = df["Frecuencia"].map(freq_map)

# Opinión: codificar como numérico para proporción de 'No' (consideramos 'No' como desacuerdo)
df["no_ganancia_calidad"] = (df["Ganancias=Buena"] == "No").astype(int)

# Datos externos: recaudación promedio por género (millones USD, aproximación realista)
recaudacion_por_genero = {
    "Acción": 400,
    "Comedia": 200,
    "Drama": 80,
    "Ciencia ficción": 350,
    "Terror": 150,
    "Animación": 300
}
df["recaudacion_promedio"] = df["Género"].map(recaudacion_por_genero)

# Agrupar por género para métricas agregadas
grouped = df.groupby("Género").agg(
    frecuencia_promedio=("frecuencia_anual", "mean"),
    proporcion_no=("no_ganancia_calidad", "mean"),
    count=("no_ganancia_calidad", "count"),
    recaudacion=("recaudacion_promedio", "first"),
    factor_influencia_moda=("Influencia", lambda x: x.mode()[0] if not x.mode().empty else "Desconocido")
).reset_index()

# Mapear factor de influencia a un valor numérico para el eje X (ordinal)
factores = ["Actores o director", "Críticas y reseñas", "Popularidad / tendencia", 
            "Recomendaciones de amigos", "Redes sociales", "Tráiler"]
factor_to_num = {f: i for i, f in enumerate(factores)}
grouped["influencia_num"] = grouped["factor_influencia_moda"].map(factor_to_num)

# Tamaño de burbuja proporcional al número de respuestas (normalizado)
size = grouped["count"] * 15  # factor de escala

# Crear gráfico 3D de burbujas
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=grouped["influencia_num"],
    y=grouped["recaudacion"],
    z=grouped["frecuencia_promedio"],
    mode="markers+text",
    marker=dict(
        size=size,
        color=grouped["proporcion_no"],
        colorscale="RdYlBu_r",  # rojo = alta proporción de "No" (desacuerdo con ganancias=calidad)
        showscale=True,
        colorbar=dict(title="Proporción que cree que<br>ganancias ≠ buena película"),
        line=dict(width=1, color="black")
    ),
    text=grouped["Género"],
    textposition="top center",
    textfont=dict(size=10, color="black"),
    hoverinfo="text",
    hovertext=[
        f"Género: {g}<br>Frecuencia anual: {f:.1f} veces<br>Recaudación: {r} M USD<br>Proporción 'No': {p:.0%}<br>Influencia principal: {inf}"
        for g, f, r, p, inf in zip(grouped["Género"], grouped["frecuencia_promedio"], 
                                   grouped["recaudacion"], grouped["proporcion_no"], 
                                   grouped["factor_influencia_moda"])
    ]
))

# Personalizar ejes
fig.update_layout(
    title="Relación entre Género, Recaudación, Frecuencia de Visita y Percepción de Calidad",
    scene=dict(
        xaxis=dict(title="Factor de influencia principal", tickvals=list(range(len(factores))), ticktext=factores),
        yaxis=dict(title="Recaudación promedio (millones USD)", type="log"),
        zaxis=dict(title="Frecuencia de visita (veces por año)"),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
    ),
    width=1000,
    height=800,
    margin=dict(l=0, r=0, b=0, t=50),
    font=dict(family="Arial", size=12),
    template="plotly_white"
)

# Mostrar la figura (en entorno interactivo se verá rotable)
fig.show()

# Opcional: guardar como HTML para compartir
# fig.write_html("visualizacion_peliculas_3d.html")
