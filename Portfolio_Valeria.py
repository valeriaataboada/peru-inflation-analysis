# Peru's Inflation Analysis
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file. We skip the first two rows and specify the encoding
# because the dataset from the central bank is not in UTF-8.
inflacion = pd.read_csv(
    "data/inflacion_peru_2015_2024.csv",
    skiprows=2,
    header=None,
    encoding="cp1252"
)

# Rename columns for clarity
inflacion.columns = ["Year", "Inflation"]

# Convert values to numeric.
# If a value cannot be converted, it becomes NaN
inflacion["Year"] = pd.to_numeric(inflacion["Year"], errors="coerce")
inflacion["Inflation"] = pd.to_numeric(inflacion["Inflation"], errors="coerce")

# Remove empty rows and sort the dataset by year
inflacion = inflacion.dropna().sort_values("Year").reset_index(drop=True)

print("Clean dataset:")
print(inflacion)

# Compare inflation before and after the pandemic
pre = inflacion[inflacion["Year"] <= 2019]
post = inflacion[inflacion["Year"] >= 2020]

print(f"\nAverage inflation 2015–2019: {pre['Inflation'].mean():.2f}")
print(f"Average inflation 2020–2024: {post['Inflation'].mean():.2f}")

# Calculate volatility (standard deviation)
print("\nVolatility (standard deviation):")
print(f"2015–2019: {pre['Inflation'].std():.2f}")
print(f"2020–2024: {post['Inflation'].std():.2f}")

# Plot inflation over time
plt.figure()
plt.plot(inflacion["Year"], inflacion["Inflation"])
plt.title("Inflation in Peru (2015–2024)")
plt.xlabel("Year")
plt.ylabel("Inflation (%)")
plt.grid(True)
plt.show()