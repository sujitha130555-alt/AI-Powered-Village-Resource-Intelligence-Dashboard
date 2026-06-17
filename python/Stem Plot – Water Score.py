import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("village.xlsx")

plt.figure(figsize=(12,6))

plt.stem(
    df["Village"],
    df["Water"]
)

plt.xticks(rotation=90)

plt.xlabel("Village")
plt.ylabel("Water Score")

plt.title("Water Scores")

plt.show()
