# SQL Analysis — Healthcare Claims Analytics

## Overview

This folder contains the SQL analysis performed on the **Healthcare Claims & Patient Analytics** dataset.

The SQL analysis translates business questions into structured queries to evaluate healthcare claim volume, costs, utilization, providers, diagnoses, insurance types, claim status, and trends.

The analysis supports the broader project workflow:

**Business Requirements → SQL Analysis → Business Insights → Power BI Reporting**

---

## SQL Environment

| Item     | Details                          |
| -------- | -------------------------------- |
| Database | SQLite                           |
| SQL File | `healthcare_claims_analysis.sql` |
| Dataset  | `healthcare_claims.csv`          |

---

## Analysis Performed

The SQL analysis includes:

1. Total number of claims
2. Total number of unique patients
3. Total claim amount
4. Average claim amount
5. Claims by diagnosis
6. Claims by provider
7. Claims by insurance type
8. Claims by state
9. Claims by claim status
10. Monthly claim trends
11. High-cost claim analysis
12. Length-of-stay analysis
13. Claim status percentages
14. Top 10 most expensive claims

---

## Business Questions Addressed

The SQL analysis was designed to answer questions such as:

* How many healthcare claims are in the dataset?
* How many unique patients are represented?
* What is the total healthcare claim amount?
* What is the average claim amount?
* Which diagnoses are associated with higher claim costs?
* Which providers have the highest claim volumes or costs?
* How do claim costs vary by insurance type?
* Which states have the highest claim activity?
* What is the distribution of paid, pending, and denied claims?
* How do claim volumes and costs change over time?
* Which claims represent the highest individual claim amounts?
* What patterns can be observed between length of stay and claim amount?

---

## SQL Techniques Demonstrated

The analysis demonstrates practical SQL techniques including:

* `SELECT`
* `WHERE`
* `GROUP BY`
* `ORDER BY`
* `COUNT`
* `COUNT(DISTINCT)`
* `SUM`
* `AVG`
* `ROUND`
* `LIMIT`
* Subqueries
* Date and time functions
* Aggregation
* Filtering and sorting
* Business-oriented analytical querying

---

## Business Analysis Applications

The SQL analysis supports several common Business Analyst and Data Analyst use cases:

### Cost Analysis

Evaluate total, average, and high-cost claims across business dimensions.

### Utilization Analysis

Analyze claim volume, patient counts, and length of stay.

### Provider Analysis

Compare claim activity and costs across healthcare providers.

### Insurance Analysis

Evaluate claim activity and financial amounts across insurance types.

### Trend Analysis

Monitor claim volume and claim amounts over time.

### Claim Status Analysis

Evaluate paid, pending, and denied claims and their distribution.

---

## Relationship to the Overall Project

The SQL analysis is one component of the project's end-to-end analytical workflow.

* **Business Requirements** define the business questions and analytical needs.
* **SQL** provides structured analysis of the healthcare claims data.
* **Python** supports data profiling and exploratory analysis.
* **Power BI** presents the results through interactive dashboards.
* **Business Insights** connect the analytical results to stakeholder needs.

---

## Portfolio Value

This SQL analysis demonstrates the ability to translate business requirements into structured queries and analytical outputs.

It demonstrates practical experience with:

* Healthcare data analysis
* SQL-based business analysis
* Data aggregation and segmentation
* KPI calculation
* Trend analysis
* Cost and utilization analysis
* Translating business questions into analytical queries
* Supporting business intelligence reporting
