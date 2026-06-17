import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel("village.xlsx")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Horizontal Bar Chart
plt.figure(figsize=(10, 8))

plt.barh(
    df["Village"],
    df["Internet connection"]
)

plt.xlabel("Internet Score")
plt.ylabel("Village")
plt.title("Internet Connectivity Across Villages")

plt.show()
