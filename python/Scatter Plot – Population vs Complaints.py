import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("village.xlsx")

plt.figure(figsize=(8,6))

plt.scatter(
    df["Population"],
    df["Monthly Complaints"]
)

plt.xlabel("Population")
plt.ylabel("Monthly Complaints")

plt.title("Population vs Complaints")

plt.show()
