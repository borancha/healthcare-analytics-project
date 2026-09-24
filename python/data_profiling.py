import pandas as pd

# Load healthcare claims data
df = pd.read_csv("../data/healthcare_claims.csv")

# Basic dataset information
print("DATASET PROFILE")
print("=" * 40)

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())

# Unique patients
print("\nUnique Patients:", df["Patient_ID"].nunique())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Rows:", df.duplicated().sum())

# Age information
print("\nAge Statistics:")
print("Minimum Age:", df["Age"].min())
print("Maximum Age:", df["Age"].max())
print("Average Age:", round(df["Age"].mean(), 2))

# Claim information
print("\nClaim Statistics:")
print("Total Claim Amount:", round(df["Claim_Amount"].sum(), 2))
print("Average Claim Amount:", round(df["Claim_Amount"].mean(), 2))
print("Maximum Claim Amount:", round(df["Claim_Amount"].max(), 2))

# Length of stay
print("\nLength of Stay:")
print("Average:", round(df["Length_of_Stay"].mean(), 2))
print("Maximum:", df["Length_of_Stay"].max())

# Date range
df["Admission_Date"] = pd.to_datetime(df["Admission_Date"])

print("\nAdmission Date Range:")
print("Start:", df["Admission_Date"].min())
print("End:", df["Admission_Date"].max())

# Category counts
print("\nDiagnoses:")
print(df["Diagnosis"].value_counts())

print("\nInsurance Types:")
print(df["Insurance_Type"].value_counts())

print("\nClaim Status:")
print(df["Claim_Status"].value_counts())
