import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("village.xlsx")

plt.figure(figsize=(8,6))

plt.hist(df["Population"])

plt.xlabel("Population")
plt.ylabel("Frequency")

plt.title("Population Distribution")

plt.show()
