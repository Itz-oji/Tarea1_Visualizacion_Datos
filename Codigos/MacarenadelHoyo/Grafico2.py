import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_excel('Calificaciones.xlsx')
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit()

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
plt.savefig('Visualizacion_Grafico2.png', dpi=300, bbox_inches='tight')
plt.show()
