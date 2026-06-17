import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("village.xlsx")

plt.figure(figsize=(6,6))

plt.boxplot(df["Road Service"])

plt.ylabel("Road Score")

plt.title("Road Service Distribution")

plt.show()
