import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel("village.xlsx")

# Remove extra spaces
df.columns = df.columns.str.strip()

# Replace "Bus Service" below with the exact column name
bus_data = df["Bus Service"]

# Create x values
x = range(len(df))

# Area chart
plt.figure(figsize=(12,6))

plt.fill_between(x, bus_data)

plt.xticks(x, df["Village"], rotation=90)

plt.xlabel("Village")
plt.ylabel("Bus Service Score")
plt.title("Bus Service Availability Across Villages")

plt.tight_layout()
plt.show()
