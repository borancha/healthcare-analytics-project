# Python Analysis – Healthcare Claims Analytics

## Overview

This folder contains the Python-based **data profiling, validation, and exploratory analysis** performed on the Healthcare Claims & Patient Analytics dataset.

Python was used to understand the dataset structure, assess data quality, analyze healthcare utilization and claim costs, and identify patterns that support subsequent SQL analysis and Power BI reporting.

### Analysis Workflow

**Business Requirements → Data Profiling → Data Validation → Exploratory Analysis → SQL Analysis → Power BI Reporting → Business Insights**

---

## Python Tools

* Python
* Pandas
* NumPy
* Jupyter Notebook
* Matplotlib

---

## Analysis Performed

The Python analysis includes:

* Dataset structure and dimensions
* Column and data type inspection
* Missing-value analysis
* Duplicate-record checks
* Descriptive statistics
* Numerical variable analysis
* Categorical variable analysis
* Claim amount analysis
* Length-of-stay analysis
* Healthcare utilization analysis
* Claim status analysis
* Data quality assessment
* Exploratory pattern identification

---

## Key Data Fields

The analysis works with healthcare claims information including:

* Patient ID
* Age
* Gender
* State
* Diagnosis
* Provider
* Admission Date
* Discharge Date
* Insurance Type
* Claim Amount
* Length of Stay
* Claim Status

---

## Python Files

### `data_profiling.py`

Python script used for initial dataset profiling and data-quality assessment.

The script examines:

* Dataset dimensions
* Column names
* Data types
* Missing values
* Duplicate records
* Basic dataset structure

### `healthcare_claims_analysis.py`

Python script containing the primary exploratory analysis of the healthcare claims dataset.

The analysis supports examination of:

* Claim volumes
* Claim amounts
* Patient demographics
* Diagnoses
* Providers
* Insurance types
* Claim status
* Length of stay
* Utilization patterns

### `healthcare_claims_analysis.ipynb`

Interactive Jupyter Notebook containing the Python analysis, calculations, and results.

The notebook provides a step-by-step view of the exploratory analysis performed during the project.

---

## Business Analysis Applications

The Python analysis supports several business-focused questions:

* What is the overall volume and financial value of healthcare claims?
* Which diagnoses and providers are associated with higher claim amounts?
* How does utilization vary across patient demographics?
* How do claim outcomes differ by status?
* What patterns can be observed in length of stay and claim costs?
* Are there data-quality issues that could affect downstream reporting?

These analyses provide a foundation for developing SQL queries and Power BI reporting.

---

## Data Quality & Validation

Python was also used as an initial data-validation layer before downstream analysis.

Quality checks include:

* Missing values
* Duplicate records
* Data types
* Numerical field distributions
* Categorical values
* Claim amount consistency
* Length-of-stay values
* Key analytical fields

Identified data-quality considerations should be reviewed before using the
