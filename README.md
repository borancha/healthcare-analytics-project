# Healthcare Claims & Patient Analytics

> **End-to-end Business Analyst & Data Analyst portfolio project using SQL, Python, and Power BI to analyze healthcare claims, costs, utilization, providers, insurance, and patient patterns.**

## Project Overview

This project demonstrates an end-to-end analytics workflow, from **business requirements and data profiling to SQL analysis, Python exploration, and interactive Power BI reporting**.

The objective is to transform healthcare claims data into actionable insights that can support **operational reporting, cost analysis, healthcare utilization analysis, and data-driven decision-making**.

---
## Project Snapshot

| Metric | Result |
|---|---:|
| Total Claims | 5,000 |
| Total Claim Amount | $41.29M |
| Average Claim Amount | $8,258.41 |
| Average Length of Stay | 4.7 days |
| Average Patient Age | 51.4 years |
| Paid Claims | 3,907 (78.14%) |
| Pending Claims | 711 (14.22%) |
| Denied Claims | 382 (7.64%) |

### Key Analysis Areas

- 💰 Claim cost and high-cost case analysis
- 🏥 Healthcare utilization and length-of-stay analysis
- 👨‍⚕️ Provider and diagnosis analysis
- 🏦 Insurance-type analysis
- 📈 Monthly claim trends
- 📋 Claim status analysis
- 👥 Patient demographic analysis
## Business Problem

---

Healthcare organizations manage large volumes of patient and claims data. Without effective analysis and reporting, stakeholders may have difficulty understanding healthcare utilization, claim costs, diagnosis patterns, provider activity, insurance distribution, and changes over time.

This project analyzes healthcare claims data and develops an interactive reporting solution to help stakeholders explore key healthcare metrics and identify patterns requiring further investigation.

---

## Business Objectives

- Analyze patient demographics and healthcare utilization.
- Identify high-cost claims and diagnosis patterns.
- Analyze claim amounts by provider and insurance type.
- Identify monthly healthcare claim trends.
- Analyze hospital length of stay.
- Examine claim status and claim type.
- Identify patterns across patient demographics and healthcare utilization.
- Develop an interactive Power BI dashboard for stakeholder reporting.
- Provide SQL and Python analysis to support deeper investigation.

---

## Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| **SQL / SQLite** | Data querying, aggregation, and business analysis |
| **Python** | Exploratory data analysis and data profiling |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical analysis |
| **Matplotlib** | Data visualization |
| **Power BI** | Interactive dashboard and business reporting |
| **CSV** | Source dataset |
| **Jupyter Notebook** | Python analysis environment |
| **GitHub** | Version control and portfolio documentation |

---

## Key Business Questions

1. What is the total healthcare claim amount?
2. What is the average claim amount?
3. Which diagnoses have the highest healthcare costs?
4. Which providers have the highest claim amounts and claim volumes?
5. Which insurance types account for the highest claim amounts?
6. How do healthcare claims change over time?
7. What is the average hospital length of stay?
8. What is the distribution of claims by status?
9. Which claims represent high-cost cases?
10. What patterns can be identified across patient demographics and healthcare utilization?

---

## Project Workflow

The project followed an end-to-end analytics workflow:

1. **Business Requirements**
2. **Data Understanding**
3. **Data Profiling & Quality Assessment**
4. **Data Preparation**
5. **SQL Business Analysis**
6. **Python Exploratory Data Analysis**
7. **Power BI Dashboard Development**
8. **Business Insights & Interpretation**
9. **GitHub Documentation**

---

# Business Analyst Perspective

This project demonstrates an end-to-end **Business Analyst workflow**, from defining the business problem through requirements, analysis, validation, and stakeholder reporting.

Key Business Analysis activities include:

* Defined the business problem and analytical objectives.
* Translated business questions into measurable requirements and KPIs.
* Identified stakeholder reporting and information needs.
* Defined analytical questions based on business requirements.
* Documented assumptions and acceptance criteria.
* Supported data validation and analytical interpretation.
* Translated analytical results into stakeholder-friendly reporting.
* Connected business requirements with SQL, Python, and Power BI solutions.

Business requirements are documented in the [`Documentation`](https://github.com/borancha/healthcare-analytics-project/tree/main/documentation) folder.


---

# Data Analyst Perspective

The project demonstrates an end-to-end **Data Analyst workflow**, including data preparation, validation, exploratory analysis, SQL analysis, and business intelligence reporting.

Key Data Analyst activities include:

* Profiled the healthcare claims dataset and assessed data quality.
* Validated data types, missing values, duplicates, and numerical fields.
* Performed exploratory data analysis using Python and Pandas.
* Developed SQL queries for aggregation, filtering, segmentation, and trend analysis.
* Analyzed claim costs, utilization, diagnoses, providers, insurance types, and claim status.
* Identified high-cost claims and healthcare utilization patterns.
* Analyzed length of stay and monthly claim trends.
* Developed interactive Power BI dashboards and KPI reporting.
* Translated analytical results into business-focused insights.

---

# Power BI Dashboard

The Power BI dashboard provides an interactive view of healthcare claims, costs, utilization, patient demographics, providers, insurance types, and claim status.

### Key Dashboard Areas

* Total claims and claim volume
* Total and average claim amounts
* Claim status distribution
* Diagnosis and healthcare cost analysis
* Provider activity
* Insurance type analysis
* Patient demographics
* Length-of-stay analysis
* Monthly claim trends
* Healthcare utilization

### Dashboard Preview

![Healthcare Claims Dashboard](https://github.com/borancha/healthcare-analytics-project/raw/main/images/claims-dashboard.png)

The Power BI source file and documentation are available in the [`PowerBI`](https://github.com/borancha/healthcare-analytics-project/tree/main/PowerBI) folder.

---

# SQL Analysis

SQL was used to perform structured analysis of healthcare claims data and answer key business questions related to cost, utilization, providers, insurance, and claim outcomes.

### Key SQL Analysis

* Total claims and total patients
* Total and average claim amounts
* Claims by diagnosis
* Claims by provider
* Claims by insurance type
* Claims by state
* Claims by claim status
* Monthly claim trends
* Claim status percentages
* Length-of-stay analysis
* High-cost claim identification
* Top 10 most expensive claims

The SQL queries are available in [`healthcare_claims_analysis.sql`](https://github.com/borancha/healthcare-analytics-project/blob/main/SQL/healthcare_claims_analysis.sql).

---

# Python Analysis

Python was used for data profiling, quality assessment, exploratory analysis, and analytical validation.

### Key Python Analysis

* Inspected dataset structure and dimensions
* Validated data types and data quality
* Analyzed missing values and duplicates
* Generated descriptive statistics
* Performed numerical and categorical analysis
* Analyzed claim amounts and healthcare utilization
* Examined diagnosis and provider patterns
* Analyzed length of stay
* Explored claim trends and distributions
* Created analytical visualizations
* Used Pandas and NumPy for data manipulation and analysis

The Python analysis files are available in the [`python`](https://github.com/borancha/healthcare-analytics-project/tree/main/python) folder.
---

## Project Structure

```text
healthcare-analytics-project/
│
├── PowerBI/
│   ├── Healthcare Dashboard
│   └── README.md
│
├── SQL/
│   ├── README.md
│   └── healthcare_claims_analysis.sql
│
├── documentation/
│   └── business-requirements.md
│
├── python/
│   ├── README.md
│   ├── data_profiling.py
│   ├── healthcare_claims_analysis.py
│   └── healthcare_claims_analysis.ipynb
│
├── data/
│   └── healthcare_claims.csv
│
├── images/
│   └── claims-dashboard.png
│
└── README.md
---

## Key Skills Demonstrated

### Business Analysis

* Requirements Gathering
* Business Requirements Documentation
* Stakeholder Analysis
* Business Questions & KPI Definition
* Acceptance Criteria
* Data & Reporting Requirements
* UAT & Validation

### Data Analytics

* SQL
* Python
* Pandas & NumPy
* Data Profiling
* Data Quality Assessment
* Exploratory Data Analysis
* Statistical & Descriptive Analysis
* Healthcare Claims Analytics

### Business Intelligence

* Power BI
* Dashboard Development
* KPI Reporting
* Interactive Visualization
* Business Insights
* Trend & Performance Analysis

### Tools & Platforms

* Jupyter Notebook
* SQLite
* GitHub
---
## Project Outcome

This project demonstrates how a Business Analyst and Data Analyst can take a healthcare business problem from **requirements definition through data analysis and stakeholder reporting**.

The project connects:

**Business Requirements → Data Validation → SQL Analysis → Python Analysis → Power BI Reporting → Business Insights**

It demonstrates practical experience in translating business questions into analytical requirements, validating and analyzing data, developing business intelligence reporting, and communicating results in a stakeholder-friendly format.
---

## Author

**Srikanth Borancha**

Business Analyst | Data Analyst

**Core Skills:** Business Analysis | SQL | Python | Power BI | Tableau | Healthcare Analytics
