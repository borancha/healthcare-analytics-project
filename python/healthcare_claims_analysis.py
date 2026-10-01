import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Healthcare Claims & Patient Analytics
# Exploratory Data Analysis
# ============================================================
# Purpose:
# Perform business-focused exploratory analysis of healthcare
# claims data using Python and Pandas.
#
# Analysis areas:
# - Claims and patient metrics
# - Claim status
# - Diagnosis
# - Insurance type
# - Provider
# - State
# - Demographics
# - Length of stay
# - Monthly trends
# - Cost patterns
# ============================================================


# ------------------------------------------------------------
# 1. Load Dataset
# ------------------------------------------------------------

file_path = "../data/healthcare_claims.csv"

df = pd.read_csv(file_path)

print("Healthcare Claims & Patient Analytics")
print("=" * 55)

print(f"Dataset Rows: {len(df):,}")
print(f"Dataset Columns: {len(df.columns):,}")


# ------------------------------------------------------------
# 2. Data Preparation
# ------------------------------------------------------------

df["Admission_Date"] = pd.to_datetime(
    df["Admission_Date"],
    errors="coerce"
)

df["Discharge_Date"] = pd.to_datetime(
    df["Discharge_Date"],
    errors="coerce"
)

print("\nData types converted successfully.")


# ------------------------------------------------------------
# 3. Overall Business Metrics
# ------------------------------------------------------------

print("\nOVERALL BUSINESS METRICS")
print("=" * 55)

total_claims = len(df)
unique_patients = df["Patient_ID"].nunique()
total_claim_amount = df["Claim_Amount"].sum()
average_claim_amount = df["Claim_Amount"].mean()
average_length_of_stay = df["Length_of_Stay"].mean()
average_patient_age = df["Age"].mean()

print(f"Total Claims: {total_claims:,}")
print(f"Unique Patients: {unique_patients:,}")
print(f"Total Claim Amount: ${total_claim_amount:,.2f}")
print(f"Average Claim Amount: ${average_claim_amount:,.2f}")
print(f"Average Length of Stay: {average_length_of_stay:.2f} days")
print(f"Average Patient Age: {average_patient_age:.2f} years")


# ------------------------------------------------------------
# 4. Claim Status Analysis
# ------------------------------------------------------------

print("\nCLAIM STATUS ANALYSIS")
print("=" * 55)

claim_status = df["Claim_Status"].value_counts()

claim_status_percentage = (
    df["Claim_Status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nClaim Counts:")
print(claim_status)

print("\nClaim Percentages:")
print(claim_status_percentage)

status_analysis = (
    df.groupby("Claim_Status")["Claim_Amount"]
    .agg(["count", "sum", "mean"])
    .round(2)
)

print("\nClaim Status Financial Analysis:")
print(status_analysis)


# ------------------------------------------------------------
# 5. Diagnosis Analysis
# ------------------------------------------------------------

print("\nDIAGNOSIS ANALYSIS")
print("=" * 55)

diagnosis_analysis = (
    df.groupby("Diagnosis")["Claim_Amount"]
    .agg(
        Total_Claims="count",
        Total_Claim_Amount="sum",
        Average_Claim_Amount="mean"
    )
    .sort_values("Total_Claim_Amount", ascending=False)
    .round(2)
)

print(diagnosis_analysis)


# Claim status by diagnosis
diagnosis_status = pd.crosstab(
    df["Diagnosis"],
    df["Claim_Status"]
)

print("\nClaim Status by Diagnosis:")
print(diagnosis_status)


# ------------------------------------------------------------
# 6. Insurance Analysis
# ------------------------------------------------------------

print("\nINSURANCE TYPE ANALYSIS")
print("=" * 55)

insurance_analysis = (
    df.groupby("Insurance_Type")["Claim_Amount"]
    .agg(
        Total_Claims="count",
        Total_Claim_Amount="sum",
        Average_Claim_Amount="mean"
    )
    .sort_values("Total_Claim_Amount", ascending=False)
    .round(2)
)

print(insurance_analysis)


insurance_status = pd.crosstab(
    df["Insurance_Type"],
    df["Claim_Status"],
    normalize="index"
).mul(100).round(2)

print("\nClaim Status Percentage by Insurance Type:")
print(insurance_status)


# ------------------------------------------------------------
# 7. Provider Analysis
# ------------------------------------------------------------

print("\nPROVIDER ANALYSIS")
print("=" * 55)

print(f"Unique Providers: {df['Provider'].nunique():,}")

provider_analysis = (
    df.groupby("Provider")["Claim_Amount"]
    .agg(
        Total_Claims="count",
        Total_Claim_Amount="sum",
        Average_Claim_Amount="mean"
    )
    .sort_values("Total_Claim_Amount", ascending=False)
    .round(2)
)

print(provider_analysis)


# ------------------------------------------------------------
# 8. State Analysis
# ------------------------------------------------------------

print("\nSTATE ANALYSIS")
print("=" * 55)

print(f"States Represented: {df['State'].nunique():,}")

state_analysis = (
    df.groupby("State")["Claim_Amount"]
    .agg(
        Total_Claims="count",
        Total_Claim_Amount="sum",
        Average_Claim_Amount="mean"
    )
    .sort_values("Total_Claim_Amount", ascending=False)
    .round(2)
)

print(state_analysis)


# ------------------------------------------------------------
# 9. Demographic Analysis
# ------------------------------------------------------------

print("\nDEMOGRAPHIC ANALYSIS")
print("=" * 55)

print("Gender Distribution:")
print(df["Gender"].value_counts())

print("\nAge Statistics:")
print(df["Age"].describe().round(2))


# Age groups
age_bins = [0, 18, 35, 50, 65, float("inf")]
age_labels = ["Under 18", "18-34", "35-49", "50-64", "65+"]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=age_bins,
    labels=age_labels,
    right=False
)

age_group_analysis = (
    df.groupby("Age_Group", observed=False)["Claim_Amount"]
    .agg(
        Total_Claims="count",
        Unique_Patients=("Patient_ID", "nunique"),
        Total_Claim_Amount="sum",
        Average_Claim_Amount="mean"
    )
    .round(2)
)

print("\nAge Group Analysis:")
print(age_group_analysis)


gender_analysis = (
    df.groupby("Gender")["Claim_Amount"]
    .agg(
        Total_Claims="count",
        Total_Claim_Amount="sum",
        Average_Claim_Amount="mean"
    )
    .round(2)
)

print("\nGender Financial Analysis:")
print(gender_analysis)


# ------------------------------------------------------------
# 10. Length of Stay Analysis
# ------------------------------------------------------------

print("\nLENGTH OF STAY ANALYSIS")
print("=" * 55)

los_analysis = (
    df.groupby("Length_of_Stay")["Claim_Amount"]
    .agg(
        Total_Claims="count",
        Total_Claim_Amount="sum",
        Average_Claim_Amount="mean"
    )
    .sort_index()
    .round(2)
)

print(los_analysis)

los_correlation = df[
    ["Length_of_Stay", "Claim_Amount"]
].corr().loc["Length_of_Stay", "Claim_Amount"]

print(
    f"\nCorrelation between Length of Stay and Claim Amount: "
    f"{los_correlation:.3f}"
)


# ------------------------------------------------------------
# 11. High-Cost Claims
# ------------------------------------------------------------

print("\nHIGH-COST CLAIM ANALYSIS")
print("=" * 55)

high_cost_threshold = 50000

high_cost_claims = (
    df[df["Claim_Amount"] > high_cost_threshold]
    [
        [
            "Patient_ID",
            "Diagnosis",
            "Provider",
            "Insurance_Type",
            "Claim_Amount",
            "Length_of_Stay",
            "Claim_Status"
        ]
    ]
    .sort_values("Claim_Amount", ascending=False)
)

print(
    f"Claims above ${high_cost_threshold:,.0f}: "
    f"{len(high_cost_claims):,}"
)

print("\nTop High-Cost Claims:")
print(high_cost_claims.head(10).to_string(index=False))


# ------------------------------------------------------------
# 12. Monthly Trend Analysis
# ------------------------------------------------------------

print("\nMONTHLY TREND ANALYSIS")
print("=" * 55)

df["Admission_Month"] = df["Admission_Date"].dt.to_period("M")

monthly_analysis = (
    df.groupby("Admission_Month")
    .agg(
        Total_Claims=("Claim_Amount", "count"),
        Total_Claim_Amount=("Claim_Amount", "sum"),
        Average_Claim_Amount=("Claim_Amount", "mean")
    )
    .round(2)
)

print(monthly_analysis)


# ------------------------------------------------------------
# 13. Visual Analysis
# ------------------------------------------------------------

# Claim status
claim_status.plot(kind="bar")

plt.title("Healthcare Claims by Claim Status")
plt.xlabel("Claim Status")
plt.ylabel("Number of Claims")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Total claim amount by diagnosis
diagnosis_cost = (
    df.groupby("Diagnosis")["Claim_Amount"]
    .sum()
    .sort_values(ascending=False)
)

diagnosis_cost.plot(kind="bar")

plt.title("Total Claim Amount by Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Total Claim Amount ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# Average claim amount by diagnosis
diagnosis_average = (
    df.groupby("Diagnosis")["Claim_Amount"]
    .mean()
    .sort_values(ascending=False)
)

diagnosis_average.plot(kind="bar")

plt.title("Average Claim Amount by Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Average Claim Amount ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# Total claim amount by insurance type
insurance_cost = (
    df.groupby("Insurance_Type")["Claim_Amount"]
    .sum()
    .sort_values(ascending=False)
)

insurance_cost.plot(kind="bar")

plt.title("Total Claim Amount by Insurance Type")
plt.xlabel("Insurance Type")
plt.ylabel("Total Claim Amount ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Claim volume by insurance type
insurance_count = df["Insurance_Type"].value_counts()

insurance_count.plot(kind="bar")

plt.title("Number of Claims by Insurance Type")
plt.xlabel("Insurance Type")
plt.ylabel("Number of Claims")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Total claim amount by provider
provider_cost = (
    df.groupby("Provider")["Claim_Amount"]
    .sum()
    .sort_values(ascending=False)
)

provider_cost.plot(kind="bar")

plt.title("Total Claim Amount by Provider")
plt.xlabel("Provider")
plt.ylabel("Total Claim Amount ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# Total claim amount by state
state_cost = (
    df.groupby("State")["Claim_Amount"]
    .sum()
    .sort_values(ascending=False)
)

state_cost.plot(kind="bar")

plt.title("Total Claim Amount by State")
plt.xlabel("State")
plt.ylabel("Total Claim Amount ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Length of stay vs claim amount
plt.scatter(
    df["Length_of_Stay"],
    df["Claim_Amount"]
)

plt.title("Length of Stay vs Claim Amount")
plt.xlabel("Length of Stay (Days)")
plt.ylabel("Claim Amount ($)")
plt.tight_layout()
plt.show()


# Claims by age group
age_group_count = df["Age_Group"].value_counts().sort_index()

age_group_count.plot(kind="bar")

plt.title("Number of Claims by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Claims")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Average claim amount by gender
gender_average = (
    df.groupby("Gender")["Claim_Amount"]
    .mean()
)

gender_average.plot(kind="bar")

plt.title("Average Claim Amount by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Claim Amount ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Monthly claim volume
monthly_claims = (
    df.groupby("Admission_Month")
    .size()
)

monthly_claims.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Healthcare Claim Volume")
plt.xlabel("Month")
plt.ylabel("Number of Claims")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Monthly claim amount
monthly_cost = (
    df.groupby("Admission_Month")["Claim_Amount"]
    .sum()
)

monthly_cost.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Healthcare Claim Amount")
plt.xlabel("Month")
plt.ylabel("Total Claim Amount ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Claim status by diagnosis
diagnosis_status_counts = pd.crosstab(
    df["Diagnosis"],
    df["Claim_Status"]
)

diagnosis_status_counts.plot(
    kind="bar",
    stacked=True
)

plt.title("Claim Status Distribution by Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Number of Claims")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Claim Status")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 14. Final Analysis Summary
# ------------------------------------------------------------

print("\nANALYSIS COMPLETED")
print("=" * 55)

print("Python exploratory analysis completed successfully.")

print("\nKey analytical areas covered:")
print("- Claim volume and financial metrics")
print("- Claim status and denial patterns")
print("- Diagnosis and provider analysis")
print("- Insurance type analysis")
print("- Geographic analysis")
print("- Patient demographics")
print("- Length of stay")
print("- High-cost claims")
print("- Monthly trends")
print("- Exploratory visualizations")
