# Healthcare Claims & Patient Analytics

## 1. Document Purpose

This Business Requirements Document (BRD) defines the business objectives, analytical requirements, data requirements, functional requirements, assumptions, stakeholders, and acceptance criteria for the **Healthcare Claims & Patient Analytics** project.

The project demonstrates an end-to-end Business Analyst and Data Analyst workflow for transforming healthcare claims data into structured analysis and stakeholder-friendly business intelligence reporting.

---

## 2. Business Problem

Healthcare stakeholders need a consolidated view of claims activity, healthcare utilization, claim costs, patient demographics, provider activity, insurance types, and claim outcomes.

Without structured reporting and analysis, stakeholders may have difficulty identifying:

* Major claim cost drivers
* Healthcare utilization patterns
* Claim status and denial patterns
* Provider and diagnosis-level cost differences
* Geographic variations in claim activity
* Changes in claim volume and spending over time

The proposed analytics solution will provide a centralized analytical view to support reporting, monitoring, and further investigation.

---

## 3. Business Objective

The primary objective is to analyze healthcare claims data and provide stakeholders with actionable visibility into:

* Claim volume and financial impact
* Healthcare utilization
* Claim cost patterns
* Provider and diagnosis activity
* Insurance-type patterns
* Claim status and denial metrics
* Geographic and time-based trends

The solution is intended to support **data-driven analysis and reporting**, rather than establish causation or make clinical decisions.

---

## 4. Project Scope

### In Scope

The project includes:

* Healthcare claims data profiling and validation
* Patient demographic analysis
* Claim cost analysis
* Claim volume analysis
* Diagnosis analysis
* Provider analysis
* Insurance-type analysis
* State-level analysis
* Claim status analysis
* Length-of-stay analysis
* Monthly trend analysis
* High-cost claim analysis
* SQL-based analytical queries
* Python-based exploratory analysis
* Power BI dashboard development
* Business requirements and acceptance criteria documentation

### Out of Scope

The project does not include:

* Clinical diagnosis or treatment recommendations
* Individual patient care decisions
* Fraud determinations
* Medical outcome evaluation
* Predictive clinical modeling
* Production claims-processing changes
* Real-world financial or reimbursement decisions

---

## 5. Stakeholders

Potential stakeholders for this analytical solution include:

| Stakeholder                            | Information Need                                     |
| -------------------------------------- | ---------------------------------------------------- |
| Healthcare Operations Management       | Utilization, claim volume, and operational trends    |
| Finance / Revenue Management           | Claim costs and financial trends                     |
| Claims Management Team                 | Claim status, pending claims, and denial patterns    |
| Provider Management Team               | Provider-level claim activity and cost patterns      |
| Business Intelligence / Analytics Team | Data analysis, reporting, and dashboard requirements |

---

## 6. Analytical Requirements

### 6.1 Cost Analysis

The solution should:

* Calculate total claim amount.
* Calculate average claim amount.
* Identify high-cost claims.
* Analyze claim amounts by diagnosis.
* Analyze claim amounts by provider.
* Analyze claim amounts by insurance type.
* Analyze claim amounts by state.

### 6.2 Utilization Analysis

The solution should:

* Calculate total claim volume.
* Calculate the number of unique patients.
* Analyze claims by diagnosis.
* Analyze claims by state.
* Analyze claims by provider.
* Analyze average length of stay.
* Analyze utilization patterns across relevant patient demographics.

### 6.3 Trend Analysis

The solution should:

* Analyze monthly claim volume.
* Analyze monthly claim amounts.
* Identify changes in claim activity over time.
* Identify changes in healthcare utilization over time.

### 6.4 Claim Status Analysis

The solution should:

* Analyze paid claims.
* Analyze pending claims.
* Analyze denied claims.
* Calculate claim status percentages.
* Calculate the claim denial rate.
* Support comparison of claim outcomes across relevant dimensions.

---

## 7. Key Performance Indicators

The Power BI dashboard should provide the following core KPIs:

| KPI                    | Definition                                             |
| ---------------------- | ------------------------------------------------------ |
| Total Patients         | Count of unique patients in the dataset                |
| Total Claims           | Total number of healthcare claims                      |
| Total Claim Amount     | Sum of claim amounts                                   |
| Average Claim Amount   | Average claim amount per claim                         |
| Average Length of Stay | Average number of days between admission and discharge |
| Paid Claims            | Number and percentage of paid claims                   |
| Pending Claims         | Number and percentage of pending claims                |
| Denied Claims          | Number and percentage of denied claims                 |
| Claim Denial Rate      | Denied claims as a percentage of total claims          |

---

## 8. Key Business Questions

The analysis should help stakeholders answer the following questions:

1. What is the total healthcare claim amount?
2. What is the average claim amount?
3. Which diagnoses are associated with higher claim amounts?
4. Which providers have the highest claim amounts or claim volumes?
5. Which insurance types account for the largest claim amounts?
6. Which states have the highest claim volume?
7. Which patient age groups have the highest claim utilization?
8. What are the monthly claim volume and spending trends?
9. What percentage of claims are denied?
10. How are claims distributed across paid, pending, and denied statuses?
11. Are there observable patterns between length of stay and claim amount?
12. Which claims represent the highest individual claim amounts?

---

## 9. Functional Requirements

The solution should allow authorized users to:

### FR-01 — View Overall KPIs

View key healthcare claims and patient KPIs through a centralized dashboard.

### FR-02 — Filter Data

Filter analytical results by relevant dimensions such as:

* Age
* Gender
* State
* Diagnosis
* Provider
* Insurance Type
* Claim Status
* Admission Date

### FR-03 — Analyze Claim Costs

Review total and average claim amounts across relevant dimensions.

### FR-04 — Analyze Utilization

Review claim volume, patient counts, and length-of-stay metrics.

### FR-05 — Analyze Claim Status

Review paid, pending, and denied claims and their respective percentages.

### FR-06 — Analyze Trends

Review monthly claim volume and claim amount trends.

### FR-07 — Identify High-Cost Claims

Identify individual claims with comparatively high claim amounts.

### FR-08 — Analyze Providers and Diagnoses

Compare claim volume and claim amounts across providers and diagnoses.

### FR-09 — Support Interactive Reporting

Allow users to interact with Power BI visuals and filters to investigate business questions.

---

## 10. Data Requirements

The analysis requires the following data elements available in the healthcare claims dataset:

| Data Element   | Purpose                                  |
| -------------- | ---------------------------------------- |
| Patient ID     | Identify unique patients                 |
| Age            | Analyze patient demographics             |
| Gender         | Analyze demographic patterns             |
| State          | Analyze geographic patterns              |
| Diagnosis      | Analyze medical-condition categories     |
| Provider       | Analyze provider activity                |
| Admission Date | Support utilization and trend analysis   |
| Discharge Date | Support length-of-stay analysis          |
| Insurance Type | Analyze insurance-related claim patterns |
| Claim Amount   | Analyze healthcare costs                 |
| Length of Stay | Analyze utilization                      |
| Claim Status   | Analyze paid, pending, and denied claims |

---

## 11. Data Quality Requirements

Before analysis, the dataset should be assessed for:

* Missing values
* Duplicate records
* Invalid data types
* Invalid or inconsistent dates
* Negative or invalid claim amounts
* Invalid length-of-stay values
* Inconsistent categorical values
* Missing patient identifiers
* Unexpected claim-status values

Data-quality issues identified during profiling should be documented and considered when interpreting analytical results.

---

## 12. Assumptions

* The dataset represents a sample healthcare claims population for portfolio and analytical demonstration purposes.
* The dataset is not assumed to represent an actual healthcare organization's complete claims population.
* Claim amounts are assumed to use a consistent monetary unit within the dataset.
* Patient identifiers are treated as identifiers for analytical purposes.
* Missing or inconsistent data may affect certain calculations.
* Calculated metrics are based on the available dataset.
* Analytical relationships do not necessarily establish causation.
* Findings should be validated with appropriate stakeholders before being used for operational decision-making.

---

## 13. Expected Deliverables

The project should produce:

1. Business Requirements Document
2. Data profiling and quality assessment
3. SQL analytical queries
4. Python exploratory analysis
5. Power BI interactive dashboard
6. Business insights and analytical findings
7. Supporting project documentation

---

## 14. Acceptance Criteria

The project will meet the defined requirements when:

### AC-01 — Data Availability

The required healthcare claims fields are available and suitable for analysis.

### AC-02 — KPI Availability

The dashboard displays the defined healthcare claims and utilization KPIs.

### AC-03 — Filtering

Users can filter the dashboard using relevant patient, claim, provider, diagnosis, insurance, geographic, and date attributes.

### AC-04 — Cost Analysis

Users can analyze total and average claim amounts across relevant dimensions.

### AC-05 — Utilization Analysis

Users can review claim volume, unique patient counts, and length-of-stay metrics.

### AC-06 — Claim Status

Users can review paid, pending, and denied claims and corresponding percentages.

### AC-07 — Trend Analysis

Users can review monthly claim volume and claim amount trends.

### AC-08 — High-Cost Claims

Users can identify and review high-cost claims.

### AC-09 — Analytical Support

SQL and Python analysis support the defined analytical requirements and business questions.

### AC-10 — Reporting Usability

The Power BI dashboard presents the required information in a clear, structured, and stakeholder-friendly format.

### AC-11 — Documentation

Project documentation clearly describes the business problem, requirements, analytical approach, assumptions, and deliverables.

---

## 15. Success Criteria

The project will be considered successful when the completed solution provides a clear analytical workflow from:

**Business Problem → Requirements → Data → Analysis → Visualization → Insights**

The solution should enable stakeholders to:

* Understand overall claim volume and financial impact.
* Review healthcare utilization patterns.
* Monitor claim status and denial metrics.
* Analyze provider, diagnosis, insurance, and geographic patterns.
* Review trends over time.
* Investigate high-cost claims.
* Use interactive reporting to explore the available data.

---

## 16. Analytical Limitations

The following limitations should be considered when interpreting the results:

* The analysis is based on a sample dataset.
* The dataset may not represent the full complexity of real-world healthcare claims.
* Observed relationships should not be interpreted as causal relationships.
* Analytical results depend on the quality and completeness of the available data.
* The analysis is intended for portfolio and demonstration purposes and should not be used as a substitute for validated operational, clinical, financial, or regulatory analysis.
