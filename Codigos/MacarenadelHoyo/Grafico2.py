import pandas as pd
import matplotlib.pyplot as plt
import requests
import io

user = "Itz-oji"
repo = "Tarea1_Visualizacion_Datos"
branch = "main"
folder_path = "Datos/MacarenadelHoyo"

url_calificaciones = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{folder_path}/Calificaciones.xlsx"

try:
    response = requests.get(url_calificaciones)
    if response.status_code == 200:
        df = pd.read_excel(io.BytesIO(response.content))
    else:
        print(f"Error: No se encontró el archivo. Código de estado: {response.status_code}")
except Exception as e:
    print(f"Ocurrió un error al intentar leer el Excel: {e}")

df = df.iloc[:31]

df.dropna(subset=['Película'], inplace=True)
df = df.sort_values('Nota Crítica (Normalizada)', ascending=True)
plt.figure(figsize=(10, 14))
plt.hlines(y=df['Película'], xmin=df['Nota Crítica (Normalizada)'], xmax=df['Nota Público'],
           color='#bdc3c7', alpha=0.6, linewidth=2)

plt.scatter(df['Nota Crítica (Normalizada)'], df['Película'], color='#e74c3c',
            label='Crítica (Metascore)', s=100, zorder=3)

plt.scatter(df['Nota Público'], df['Película'], color='#2ecc71',
            label='Público (User Score)', s=100, zorder=3)

df_coincide = df[df['Nota Crítica (Normalizada)'] == df['Nota Público']]
if not df_coincide.empty:
    plt.scatter(df_coincide['Nota Crítica (Normalizada)'], df_coincide['Película'],
                color='purple', label='Coinciden', s=100, zorder=4)

plt.title('Brecha de Opinión: Crítica vs. Público',
          loc='left', pad=30, fontsize=16, fontweight='bold')
plt.xlabel('Calificación Normalizada (Escala 1-10)', fontsize=12, labelpad=15)

plt.grid(axis='x', linestyle='--', alpha=0.4)
plt.xlim(5, 10.5)

plt.legend(loc='lower right', frameon=True, shadow=True, borderpad=1)
ax = plt.gca()
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig('Grafico2.png', dpi=300, bbox_inches='tight')
plt.show()
