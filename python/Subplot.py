import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("../data/village.xlsx")

plt.figure(figsize=(12,8))

# Water
plt.subplot(2,2,1)
plt.bar(df["Village"],df["Water"])
plt.xticks(rotation=90)
plt.title("Water")

# Complaints
plt.subplot(2,2,2)
plt.plot(df["Village"],df["Monthly Complaints"])
plt.xticks(rotation=90)
plt.title("Complaints")

# Population
plt.subplot(2,2,3)
plt.hist(df["Population"])
plt.title("Population")

# Road
plt.subplot(2,2,4)
plt.boxplot(df["Road Service"])
plt.title("Road")

plt.tight_layout()

plt.show()
