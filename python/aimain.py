import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# ==========================================
# Read Dataset
# ==========================================
df = pd.read_excel("village_ai.xlsx")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# ==========================================
# Features (Inputs)
# ==========================================
X = df[
    [
        "Water",
        "Hospital Distance",
        "Road Service",
        "Waste Collection",
        "Bus Service",
        "Internet connection",
        "Monthly Complaints"
    ]
]

# ==========================================
# Target (Output)
# ==========================================
y = df["Priority"]

# ==========================================
# Split Data
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# Create and Train AI Model
# ==========================================
model = DecisionTreeClassifier()

model.fit(X_train, y_train)

# ==========================================
# Test Accuracy
# ==========================================
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAI MODEL ACCURACY =", accuracy)

# ==========================================
# Predict Priority for All Villages
# ==========================================
df["AI Prediction"] = model.predict(X)

print("\nAI PREDICTIONS")
print(df[["Village", "AI Prediction"]])

# ==========================================
# High Priority Villages
# ==========================================
high_priority = df[df["AI Prediction"] == "High"]

print("\nVILLAGES NEEDING IMMEDIATE ATTENTION")
print(high_priority[["Village", "AI Prediction"]])

# ==========================================
# AI Recommendations
# ==========================================
print("\nAI RECOMMENDATIONS")

for index, row in high_priority.iterrows():

    print("\n--------------------------------")
    print("Village :", row["Village"])
    print("Priority Level :", row["AI Prediction"])

    print("\nSuggested Actions:")

    if row["Water"] < 5:
        print("✓ Improve water supply")

    if row["Road Service"] < 5:
        print("✓ Repair roads")

    if row["Waste Collection"] < 5:
        print("✓ Improve waste collection")

    if row["Bus Service"] < 5:
        print("✓ Increase bus services")

    if row["Internet connection"] < 5:
        print("✓ Improve internet connectivity")

    if row["Hospital Distance"] > 5:
        print("✓ Build more health centers")

    if row["Monthly Complaints"] > 40:
        print("✓ Address public complaints immediately")

# ==========================================
# Feature Importance
# ==========================================
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print("\nMOST IMPORTANT FACTORS")
print(importance.sort_values(by="Importance", ascending=False))

# ==========================================
# Top 10 Villages by Priority Score
# ==========================================
top10 = df.sort_values(
    by="Priority Score",
    ascending=False
)

print("\nTOP 10 VILLAGES NEEDING ATTENTION")
print(top10[["Village", "Priority Score"]].head(10))

# ==========================================
# Save Output File
# ==========================================
df.to_excel("village_ai_output.xlsx", index=False)

print("\nAI ANALYSIS COMPLETED SUCCESSFULLY!")

# ==========================================
# USER INPUT SYSTEM
# ==========================================
village_name = input("\nEnter Village Name: ")

result = df[df["Village"].str.lower() == village_name.lower()]

if not result.empty:

    row = result.iloc[0]

    print("\n========== VILLAGE REPORT ==========")

    print("Village :", row["Village"])
    print("District :", row["District"])
    print("Population :", row["Population"])
    print("Primary Health Centers :", row["Primary Health Centers"])

    print("\nRESOURCE SCORES")
    print("Water :", row["Water"])
    print("Road Service :", row["Road Service"])
    print("Waste Collection :", row["Waste Collection"])
    print("Bus Service :", row["Bus Service"])
    print("Internet Connection :", row["Internet connection"])

    print("\nOTHER DETAILS")
    print("Hospital Distance :", row["Hospital Distance"], "km")
    print("Monthly Complaints :", row["Monthly Complaints"])

    print("\nAI PREDICTION")
    print("Priority Level :", row["AI Prediction"])

    print("\nRECOMMENDATIONS")

    found = False

    if row["Water"] < 5:
        print("✓ Improve water supply")
        found = True

    if row["Road Service"] < 5:
        print("✓ Repair roads")
        found = True

    if row["Waste Collection"] < 5:
        print("✓ Improve waste management")
        found = True

    if row["Bus Service"] < 5:
        print("✓ Increase bus services")
        found = True

    if row["Internet connection"] < 5:
        print("✓ Improve internet connectivity")
        found = True

    if row["Hospital Distance"] > 5:
        print("✓ Build more health centers")
        found = True

    if row["Monthly Complaints"] > 40:
        print("✓ Resolve public complaints immediately")
        found = True

    if found == False:
        print("✓ Resources are good. No immediate action required.")

else:
    print("\nVillage not found in dataset!")
