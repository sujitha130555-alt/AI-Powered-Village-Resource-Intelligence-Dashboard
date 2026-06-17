import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("village.xlsx")
df.columns = df.columns.str.strip()

plt.figure(figsize=(12,6))

plt.bar(df["Village"], df["Water"])

plt.xlabel("Village")
plt.ylabel("Water Score")
plt.title("Water Availability Across Villages")

plt.xticks(rotation=90)

plt.show()
