# Portfolio Valeria - Proyecto Macro
import pandas as pd
import matplotlib.pyplot as plt

# Leémos el archivo csv. omitiendo las 2 primeras filas, y aclarando el encoding. 
inflacion = pd.read_csv(
    "data/inflacion_peru_2015_2024.csv",
    skiprows=2,
    header=None,
    encoding="cp1252"
    )

   
#  Renombramos columnas 
inflacion.columns = ["Año", "Inflacion"]

# Convertimos a números los datos y aquellos que no son reconocible en blanco
inflacion["Año"] = pd.to_numeric(inflacion["Año"], errors="coerce")
inflacion["Inflacion"] = pd.to_numeric(inflacion["Inflacion"], errors="coerce")

# Limpiar filas vacías (por si acaso)
inflacion = inflacion.dropna().sort_values("Año").reset_index(drop=True)

print("Dataset limpio:")
print(inflacion)

# Comparación pre vs post pandemia
pre = inflacion[inflacion["Año"] <= 2019]
post = inflacion[inflacion["Año"] >= 2020]

print(f"\nPromedio inflación 2015-2019: {pre["Inflacion"].mean():.2f}")
print(f"Promedio inflación 2020-2024: {post["Inflacion"].mean():.2f}")

print("\nVolatilidad (desviación estándar):")
print(f"2015-2019: {pre["Inflacion"].std():.2f}")
print(f"2020-2024: {post["Inflacion"].std():.2f}")


#  Gráfico
plt.figure()
plt.plot(inflacion["Año"], inflacion["Inflacion"])
plt.title("Inflación en Perú (2015-2024)")
plt.xlabel("Año")
plt.ylabel("Inflación (%)")
plt.show()

