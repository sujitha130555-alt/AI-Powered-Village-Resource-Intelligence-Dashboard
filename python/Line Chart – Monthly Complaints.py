import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("village.xlsx")
df.columns = df.columns.str.strip()

plt.figure(figsize=(12,6))

plt.plot(
    df["Village"],
    df["Monthly Complaints"],
    marker="o"
)

plt.xlabel("Village")
plt.ylabel("Monthly Complaints")
plt.title("Monthly Complaints by Village")

plt.xticks(rotation=90)

plt.show()
