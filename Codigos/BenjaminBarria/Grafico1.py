import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

archivo = "Recaudaciones.csv"

df = pd.read_csv(archivo, encoding='latin1')
df.columns = df.columns.str.strip()

print("\nColumnas disponibles:")
for col in df.columns:
    print("-", col)

col_x = "Roi"
col_y = "Duración (minutos)"
col_size = "Recaudación mundial"

def clean_monetary_string(s):
    if s.dtype == 'object':
        return s.astype(str).str.replace(r'[^\d.]', '', regex=True)
    return s

df[col_x] = clean_monetary_string(df[col_x])
df[col_y] = clean_monetary_string(df[col_y])
df[col_size] = clean_monetary_string(df[col_size])

df[col_x] = pd.to_numeric(df[col_x], errors='coerce')
df[col_y] = pd.to_numeric(df[col_y], errors='coerce')
df[col_size] = pd.to_numeric(df[col_size], errors='coerce')

df = df.dropna(subset=[col_x, col_y, col_size])


print(f"\nDataFrame head after cleaning and conversion (first 5 rows):")
display(df.head())
print(f"\nDataFrame info after cleaning:")
df.info()

plt.figure(figsize=(16, 9))
sns.scatterplot(x=col_x, y=col_y, size=col_size, sizes=(20, 2000), data=df, hue=col_size, legend='full')


plt.title(f"Relación entre {col_y}, {col_x} y {col_size} (Tamaño de burbuja) - Archivo: {archivo}")
plt.xlabel(col_x)
plt.ylabel(col_y)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.grid(True, linestyle='--', alpha=0.7)

plt.savefig('bubble_chart.png', bbox_inches='tight')

plt.show()