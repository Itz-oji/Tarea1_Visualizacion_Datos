## 📊 Gráfico 4: Análisis de éxito de películas mediante cuadrantes

### 📌 Descripción general
Para la construcción del cuarto gráfico, se realizó un proceso de integración y limpieza de datos provenientes de múltiples fuentes. En particular, se trabajó con tres archivos CSV distintos, los cuales fueron combinados para obtener un conjunto de datos consolidado.

El proceso consistió en:
- **Fusión de datasets**: Se unificaron los archivos mediante un *fuzzy merge*, permitiendo identificar coincidencias entre películas a pesar de diferencias en nombres.
- **Filtrado de datos**: Se conservaron únicamente aquellas películas presentes en los tres datasets.
- **Limpieza de datos**: Se transformaron variables clave, especialmente la recaudación, eliminando símbolos de moneda y convirtiendo los valores a formato numérico.

---

### ⚙️ Metodología de generación del gráfico

El código fue generado utilizando el siguiente prompt:
```
Actúa como un experto en Ciencia de Datos y Visualización con Python. Tengo tres archivos CSV: Calificaciones.csv: con las columnas 'Película', 'Nota Público' y 'Nota Crítica'. Recaudaciones.csv: con 'Película', 'Recaudación mundial' y 'Presupuesto'. tmdb_5000_movies.csv: con 'title' y 'genres'. Tarea: Genera un Gráfico de Cuadrantes (Quadrant Chart) que clasifique las películas según su tipo de éxito.Requisitos técnicos: Limpieza y Cruce: Realiza un fuzzy merge de los archivos. Limpia la columna de 'Recaudación' eliminando símbolos de moneda y convirtiéndola a valor numérico (millones de USD). Ejes del Gráfico: El eje X debe ser la 'Nota Crítica' y el eje Y la 'Recaudación mundial'. Lógica de Cuadrantes: Dibuja una línea vertical en la media de las notas y una línea horizontal en la media de la recaudación para dividir el gráfico en 4 sectores. Etiquetado de Sectores: Usa anotaciones de texto en las esquinas del gráfico para identificar los cuadrantes como: 'Blockbuster Crítico' (superior derecha), 'Éxito Comercial/Pop' (superior izquierda), 'Joyas de Culto' (inferior derecha) y 'Bajo Impacto' (inferior izquierda). Estética: Diferencia los puntos por 'Género' usando colores y ajusta el tamaño de los puntos según el 'Presupuesto' (gráfico de burbujas dentro de cuadrantes). Agrega etiquetas de nombre solo a las 5 películas más atípicas (outliers). Librería: Utiliza Seaborn o Plotly para una visualización limpia y profesional
```
---

### 📈 Características de la visualización

El gráfico generado corresponde a un **Quadrant Chart (Gráfico de Cuadrantes)** que permite clasificar las películas según dos dimensiones principales:

- **Eje X:** Nota crítica  
- **Eje Y:** Recaudación mundial  

A partir de las medias de ambas variables, el gráfico se divide en cuatro cuadrantes:

| Cuadrante | Descripción |
|----------|------------|
| 🎬 Blockbuster Crítico | Películas con alta recaudación y alta valoración crítica |
| 🍿 Éxito Comercial / Pop | Alta recaudación pero baja valoración crítica |
| 💎 Joyas de Culto | Alta valoración crítica pero baja recaudación |
| 📉 Bajo Impacto | Baja recaudación y baja valoración crítica |

Adicionalmente:
- El **color** de cada punto representa el género de la película.
- El **tamaño de las burbujas** está asociado al presupuesto.
- Se destacan las **5 películas más atípicas (outliers)** mediante etiquetas.

---

### 💻 Implementación

El código y la visualización fueron desarrollados en Google Colab:

🔗 https://colab.research.google.com/drive/1vbk1-dGQSB8SQ24uyKMLCBrwsHbLzVW-?usp=sharing

---

### ▶️ Instrucciones de uso

Para ejecutar correctamente el notebook:

1. Abrir el enlace de Colab.
2. Subir los siguientes archivos:
   - `Calificaciones.csv`
   - `Recaudaciones.csv`
   - `tmdb_5000_movies.csv`
3. Ejecutar todas las celdas en orden.

#### En la creacion de este README se utilizo chatgpt para modificar la estetica del mismo 
