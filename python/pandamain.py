import pandas as pd

# ==========================================
# Read Excel File
# ==========================================
df = pd.read_excel("../data/village.xlsx")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# ==========================================
# Basic Information
# ==========================================
print("\nFIRST 5 ROWS")
print(df.head())

print("\nLAST 5 ROWS")
print(df.tail())

print("\nDATASET INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

# ==========================================
# Water Scarcity Analysis
# ==========================================
print("\nVILLAGES WITH WATER SCARCITY")
water_scarcity = df[df["Water"] < 5]
print(water_scarcity)

# ==========================================
# Poor Road Conditions
# ==========================================
print("\nVILLAGES WITH POOR ROAD CONDITIONS")
poor_roads = df[df["Road Service"] < 5]
print(poor_roads)

# ==========================================
# Poor Waste Management
# ==========================================
print("\nVILLAGES WITH POOR WASTE MANAGEMENT")
poor_waste = df[df["Waste Collection"] < 5]
print(poor_waste)

# ==========================================
# Poor Bus Service
# ==========================================
print("\nVILLAGES WITH POOR BUS SERVICE")
poor_bus = df[df["Bus Service"] < 5]
print(poor_bus)

# ==========================================
# Poor Internet Connectivity
# ==========================================
print("\nVILLAGES WITH POOR INTERNET")
poor_internet = df[df["Internet connection"] < 5]
print(poor_internet)

# ==========================================
# Healthcare Problems
# ==========================================
print("\nVILLAGES WITH FEW HEALTH CENTERS")
poor_health = df[df["Primary Health Centers"] <= 1]
print(poor_health)

# ==========================================
# Far From Hospitals
# ==========================================
print("\nVILLAGES FAR FROM HOSPITALS")
far_hospital = df[df["Hospital Distance"] > 5]
print(far_hospital)

# ==========================================
# High Complaint Villages
# ==========================================
print("\nHIGH COMPLAINT VILLAGES")
high_complaints = df[df["Monthly Complaints"] > 40]
print(high_complaints)

# ==========================================
# Average Values
# ==========================================
print("\nAVERAGE WATER SCORE")
print(df["Water"].mean())

print("\nAVERAGE POPULATION")
print(df["Population"].mean())

print("\nAVERAGE MONTHLY COMPLAINTS")
print(df["Monthly Complaints"].mean())

# ==========================================
# Best Villages
# ==========================================
print("\nBEST WATER AVAILABILITY")
print(df.loc[df["Water"].idxmax()])

print("\nBEST ROAD SERVICE")
print(df.loc[df["Road Service"].idxmax()])

print("\nBEST INTERNET CONNECTIVITY")
print(df.loc[df["Internet connection"].idxmax()])

print("\nMINIMUM COMPLAINTS")
print(df.loc[df["Monthly Complaints"].idxmin()])

# ==========================================
# District-wise Analysis
# ==========================================
print("\nDISTRICT-WISE AVERAGE WATER SCORE")
print(df.groupby("District")["Water"].mean())

print("\nDISTRICT-WISE AVERAGE COMPLAINTS")
print(df.groupby("District")["Monthly Complaints"].mean())

print("\nDISTRICT-WISE TOTAL POPULATION")
print(df.groupby("District")["Population"].sum())

# ==========================================
# Priority Score
# ==========================================
df["Priority Score"] = (
    (10 - df["Water"]) * 2
    + df["Hospital Distance"]
    + (10 - df["Road Service"])
    + (10 - df["Waste Collection"])
    + (10 - df["Bus Service"])
    + (10 - df["Internet connection"])
    + (df["Monthly Complaints"] / 10)
)
# ==========================================
# Priority Category
# ==========================================
def priority(score):
    if score >= 25:
        return "High"
    elif score >= 15:
        return "Medium"
    else:
        return "Low"

df["Priority"] = df["Priority Score"].apply(priority)

print("\nPRIORITY LEVELS")
print(df[["Village", "Priority Score", "Priority"]])

# Save updated dataset
df.to_excel("village_ai.xlsx", index=False)

print("\nANALYSIS COMPLETED SUCCESSFULLY!")

# ==========================================
# Top 10 Villages Needing Attention
# ==========================================
top_priority = df.sort_values(
    by="Priority Score",
    ascending=False
)

print("\nTOP 10 VILLAGES NEEDING IMMEDIATE ATTENTION")
print(top_priority[["Village", "Priority Score"]].head(10))

# ==========================================
# Resource Status
# ==========================================
def status(score):
    if score >= 7:
        return "Good"
    elif score >= 5:
        return "Average"
    else:
        return "Poor"

df["Water Status"] = df["Water"].apply(status)
df["Road Status"] = df["Road Service"].apply(status)
df["Internet Status"] = df["Internet connection"].apply(status)

print("\nRESOURCE STATUS")
print(df[["Village", "Water Status", "Road Status", "Internet Status"]])

# ==========================================
# Resource Score
# ==========================================
df["Resource Score"] = (
    df["Water"]
    + df["Road Service"]
    + df["Waste Collection"]
    + df["Bus Service"]
    + df["Internet connection"]
)

best_resources = df.sort_values(
    by="Resource Score",
    ascending=False
)

print("\nTOP 5 VILLAGES WITH BEST RESOURCES")
print(best_resources[["Village", "Resource Score"]].head())

# ==========================================
# Save Output
# ==========================================
df.to_excel("village_analysis_output.xlsx", index=False)

print("\nANALYSIS COMPLETED SUCCESSFULLY!")
