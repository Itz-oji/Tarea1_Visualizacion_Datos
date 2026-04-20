# Fuentes de Datos Grafico 2

Este directorio contiene el conjunto de datos central utilizado para el análisis de divergencia en las calificaciones cinematográficas.

## Archivo: `Calificaciones.xlsx - DatosUserCritica.csv`

### Descripción
El dataset contiene una selección de las 30 películas con mayor impacto en el ranking de IMDb. El objetivo es contrastar la percepción de la audiencia masiva frente a la crítica especializada.

### Estructura de los Datos
* **Pelicula:** Nombre de la obra cinematográfica de IMDb.
* **Nota Público:** Calificación promedio otorgada por usuarios de la plataforma IMDb (escala 1 a 10).
* **Nota Crítica (Normalizada):** Calificación basada en el Metascore de Metacritic, normalizada a una escala de 1 a 10 (Original / 10).

### Origen de los Datos
* **IMDb:** Datos de los usuarios. [https://www.imdb.com/es-es/search/title/?groups=top_100&sort=user_rating%2Cdesc]
* **Metacritic:** Consolidado de reseñas críticas profesionales. [https://www.metacritic.com/browse/movie/]
* **Fecha de consulta:** Abril 2026.

### Procesamiento
Se aplicó una limpieza manual para asegurar que todas las películas de la muestra cuenten con ambas calificaciones, permitiendo un análisis de brecha íntegro.
