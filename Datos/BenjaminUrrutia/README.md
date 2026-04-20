# Análisis de Datos: TMDb Movie Metadata


## 📌 Origen de los Datos

Los datos han sido obtenidos son de  **The Movie Database (TMDb)** , publicados originalmente en Kaggle.

* **Fuente:** [TMDb Movie Metadata en Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 📝 Descripción de los Datos

El dataset se divide en dos archivos principales que se relacionan mediante la columna `id`.
Para nuestro caso solo usarenos el primer archivo (`tmdb_5000_movies.csv`)

### 1. Películas (`tmdb_5000_movies.csv`)
Contiene metadatos de 5,000 películas. Las columnas clave son:

| Columna | Descripción |
| :--- | :--- |
| `budget` | Presupuesto en USD (los valores en 0 indican datos faltantes). |
| `genres` | Lista de géneros asociados (formato JSON). |
| `popularity` | Puntaje de popularidad asignado por TMDb. |
| `revenue` | Ingresos globales de la película. |
| `vote_average` | Calificación promedio de los usuarios. |
| `release_date` | Fecha de estreno oficial. |

### 2. Créditos (`tmdb_5000_credits.csv`)
Contiene la información detallada del personal involucrado:

* **`movie_id`**: Identificador único para el cruce de datos.
* **`cast`**: JSON que incluye todos los actores, sus IDs y los personajes interpretados.
* **`crew`**: JSON con el equipo técnico (Director, Editor, Productor, Guionista, etc.).

---
