import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("village.xlsx")
df.columns = df.columns.str.strip()

district_population = df.groupby("District")["Population"].sum()

plt.figure(figsize=(8,8))

plt.pie(
    district_population,
    labels=district_population.index,
    autopct="%1.1f%%"
)

plt.title("District-wise Population")

plt.show()
