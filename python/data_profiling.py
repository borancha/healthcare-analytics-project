import pandas as pd

# ============================================================
# Healthcare Claims & Patient Analytics
# Data Profiling & Quality Assessment
# ============================================================
# Purpose:
# Profile the healthcare claims dataset and perform initial
# data-quality checks before SQL and Power BI analysis.
# ============================================================


# ------------------------------------------------------------
# 1. Load Dataset
# ------------------------------------------------------------

df = pd.read_csv("../data/healthcare_claims.csv")


# ------------------------------------------------------------
# 2. Dataset Overview
# ------------------------------------------------------------

print("HEALTHCARE CLAIMS DATASET PROFILE")
print("=" * 55)

print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]:,}")

print("\nColumn Names:")
for column in df.columns:
    print(f"- {column}")


# ------------------------------------------------------------
# 3. Data Types
# ------------------------------------------------------------

print("\nDATA TYPES")
print("=" * 55)

print(df.dtypes)


# ------------------------------------------------------------
# 4. Unique Patients
# ------------------------------------------------------------

print("\nPATIENT PROFILE")
print("=" * 55)

print(f"Unique Patients: {df['Patient_ID'].nunique():,}")


# ------------------------------------------------------------
# 5. Missing Value Assessment
# ------------------------------------------------------------

print("\nMISSING VALUE CHECK")
print("=" * 55)

missing_values = df.isnull().sum()

missing_summary = pd.DataFrame({
    "Missing_Values": missing_values,
    "Missing_Percentage": (missing_values / len(df) * 100).round(2)
})

print(missing_summary)


# ------------------------------------------------------------
# 6. Duplicate Record Check
# ------------------------------------------------------------

print("\nDUPLICATE RECORD CHECK")
print("=" * 55)

duplicate_rows = df.duplicated().sum()

print(f"Duplicate Rows: {duplicate_rows:,}")


# ------------------------------------------------------------
# 7. Numerical Data Summary
# ------------------------------------------------------------

print("\nNUMERICAL DATA SUMMARY")
print("=" * 55)

print(
    df[
        [
            "Age",
            "Claim_Amount",
            "Length_of_Stay"
        ]
    ].describe().round(2)
)


# ------------------------------------------------------------
# 8. Age Analysis
# ------------------------------------------------------------

print("\nAGE ANALYSIS")
print("=" * 55)

print(f"Minimum Age: {df['Age'].min()}")
print(f"Maximum Age: {df['Age'].max()}")
print(f"Average Age: {df['Age'].mean():.2f}")


# ------------------------------------------------------------
# 9. Claim Analysis
# ------------------------------------------------------------

print("\nCLAIM ANALYSIS")
print("=" * 55)

print(f"Total Claim Amount: ${df['Claim_Amount'].sum():,.2f}")
print(f"Average Claim Amount: ${df['Claim_Amount'].mean():,.2f}")
print(f"Minimum Claim Amount: ${df['Claim_Amount'].min():,.2f}")
print(f"Maximum Claim Amount: ${df['Claim_Amount'].max():,.2f}")


# ------------------------------------------------------------
# 10. Length of Stay Analysis
# ------------------------------------------------------------

print("\nLENGTH OF STAY ANALYSIS")
print("=" * 55)

print(f"Average Length of Stay: {df['Length_of_Stay'].mean():.2f} days")
print(f"Minimum Length of Stay: {df['Length_of_Stay'].min()} days")
print(f"Maximum Length of Stay: {df['Length_of_Stay'].max()} days")


# ------------------------------------------------------------
# 11. Date Validation and Range
# ------------------------------------------------------------

df["Admission_Date"] = pd.to_datetime(
    df["Admission_Date"],
    errors="coerce"
)

df["Discharge_Date"] = pd.to_datetime(
    df["Discharge_Date"],
    errors="coerce"
)

print("\nDATE RANGE")
print("=" * 55)

print(f"Admission Start: {df['Admission_Date'].min()}")
print(f"Admission End: {df['Admission_Date'].max()}")
print(f"Invalid Admission Dates: {df['Admission_Date'].isnull().sum():,}")
print(f"Invalid Discharge Dates: {df['Discharge_Date'].isnull().sum():,}")


# ------------------------------------------------------------
# 12. Categorical Analysis
# ------------------------------------------------------------

print("\nDIAGNOSIS DISTRIBUTION")
print("=" * 55)

print(df["Diagnosis"].value_counts())


print("\nINSURANCE TYPE DISTRIBUTION")
print("=" * 55)

print(df["Insurance_Type"].value_counts())


print("\nCLAIM STATUS DISTRIBUTION")
print("=" * 55)

print(df["Claim_Status"].value_counts())


print("\nGENDER DISTRIBUTION")
print("=" * 55)

print(df["Gender"].value_counts())


print("\nSTATE DISTRIBUTION")
print("=" * 55)

print(df["State"].value_counts())


# ------------------------------------------------------------
# 13. Business-Oriented Summary
# ------------------------------------------------------------

print("\nBUSINESS SUMMARY")
print("=" * 55)

print(f"Total Claims: {len(df):,}")
print(f"Unique Patients: {df['Patient_ID'].nunique():,}")
print(f"Total Claim Amount: ${df['Claim_Amount'].sum():,.2f}")
print(f"Average Claim Amount: ${df['Claim_Amount'].mean():,.2f}")
print(f"Average Length of Stay: {df['Length_of_Stay'].mean():.2f} days")

print("\nData profiling completed successfully.")
