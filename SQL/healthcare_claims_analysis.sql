-- ============================================================
-- Healthcare Claims & Patient Analytics
-- SQL Analysis
-- ============================================================
-- Purpose:
-- Analyze healthcare claims data to understand:
-- - Claim volume and costs
-- - Patient utilization
-- - Providers and diagnoses
-- - Insurance types
-- - Claim status and denial patterns
-- - Geographic activity
-- - Monthly trends
-- - High-cost claims
--
-- Database: SQLite
-- Dataset: healthcare_claims.csv
-- ============================================================


-- ============================================================
-- 1. Total Number of Claims
-- Business Question:
-- How many healthcare claims are in the dataset?
-- ============================================================

SELECT
    COUNT(*) AS Total_Claims
FROM healthcare_claims;


-- ============================================================
-- 2. Total Number of Unique Patients
-- Business Question:
-- How many unique patients are represented?
-- ============================================================

SELECT
    COUNT(DISTINCT Patient_ID) AS Total_Patients
FROM healthcare_claims;


-- ============================================================
-- 3. Total Claim Amount
-- Business Question:
-- What is the total healthcare claim amount?
-- ============================================================

SELECT
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount
FROM healthcare_claims;


-- ============================================================
-- 4. Average Claim Amount
-- Business Question:
-- What is the average claim amount?
-- ============================================================

SELECT
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM healthcare_claims;


-- ============================================================
-- 5. Claims by Diagnosis
-- Business Question:
-- Which diagnoses are associated with higher claim costs?
-- ============================================================

SELECT
    Diagnosis,
    COUNT(*) AS Total_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount,
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Diagnosis
ORDER BY Total_Claim_Amount DESC;


-- ============================================================
-- 6. Claims by Provider
-- Business Question:
-- Which providers have the highest claim volumes and costs?
-- ============================================================

SELECT
    Provider,
    COUNT(*) AS Total_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount,
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Provider
ORDER BY Total_Claim_Amount DESC;


-- ============================================================
-- 7. Claims by Insurance Type
-- Business Question:
-- How do claim costs vary by insurance type?
-- ============================================================

SELECT
    Insurance_Type,
    COUNT(*) AS Total_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount,
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Insurance_Type
ORDER BY Total_Claim_Amount DESC;


-- ============================================================
-- 8. Claims by State
-- Business Question:
-- Which states have the highest claim activity?
-- ============================================================

SELECT
    State,
    COUNT(*) AS Total_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount,
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY State
ORDER BY Total_Claim_Amount DESC;


-- ============================================================
-- 9. Claims by Status
-- Business Question:
-- What is the distribution of paid, pending, and denied claims?
-- ============================================================

SELECT
    Claim_Status,
    COUNT(*) AS Total_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount,
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Claim_Status
ORDER BY Total_Claims DESC;


-- ============================================================
-- 10. Monthly Claim Trends
-- Business Question:
-- How do claim volume and costs change over time?
-- ============================================================

SELECT
    strftime('%Y-%m', Admission_Date) AS Claim_Month,
    COUNT(*) AS Total_Claims,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount,
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Claim_Month
ORDER BY Claim_Month;


-- ============================================================
-- 11. High-Cost Claims
-- Business Question:
-- Which individual claims represent high-cost cases?
-- ============================================================

SELECT
    Patient_ID,
    Diagnosis,
    Provider,
    Insurance_Type,
    Claim_Amount,
    Length_of_Stay,
    Claim_Status
FROM healthcare_claims
WHERE Claim_Amount > 50000
ORDER BY Claim_Amount DESC;


-- ============================================================
-- 12. Length of Stay Analysis
-- Business Question:
-- What patterns can be observed between length of stay,
-- diagnosis, and claim amount?
-- ============================================================

SELECT
    Diagnosis,
    COUNT(*) AS Total_Claims,
    ROUND(AVG(Length_of_Stay), 2) AS Average_Length_of_Stay,
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Diagnosis
ORDER BY Average_Length_of_Stay DESC;


-- ============================================================
-- 13. Claim Status Percentage
-- Business Question:
-- What percentage of claims fall into each claim status?
-- ============================================================

SELECT
    Claim_Status,
    COUNT(*) AS Total_Claims,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM healthcare_claims),
        2
    ) AS Claim_Percentage
FROM healthcare_claims
GROUP BY Claim_Status
ORDER BY Claim_Percentage DESC;


-- ============================================================
-- 14. Claim Denial Rate
-- Business Question:
-- What percentage of claims are denied?
-- ============================================================

SELECT
    COUNT(*) AS Total_Claims,
    SUM(
        CASE
            WHEN Claim_Status = 'Denied' THEN 1
            ELSE 0
        END
    ) AS Denied_Claims,
    ROUND(
        SUM(
            CASE
                WHEN Claim_Status = 'Denied' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS Claim_Denial_Rate
FROM healthcare_claims;


-- ============================================================
-- 15. Age Group Analysis
-- Business Question:
-- Which patient age groups have the highest utilization?
-- ============================================================

SELECT
    CASE
        WHEN Age < 18 THEN 'Under 18'
        WHEN Age BETWEEN 18 AND 34 THEN '18-34'
        WHEN Age BETWEEN 35 AND 49 THEN '35-49'
        WHEN Age BETWEEN 50 AND 64 THEN '50-64'
        ELSE '65+'
    END AS Age_Group,
    COUNT(*) AS Total_Claims,
    COUNT(DISTINCT Patient_ID) AS Unique_Patients,
    ROUND(SUM(Claim_Amount), 2) AS Total_Claim_Amount,
    ROUND(AVG(Claim_Amount), 2) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Age_Group
ORDER BY Total_Claims DESC;


-- ============================================================
-- 16. Top 10 Most Expensive Claims
-- Business Question:
-- Which individual claims have the highest claim amounts?
-- ============================================================

SELECT
    Patient_ID,
    Diagnosis,
    Provider,
    Insurance_Type,
    Claim_Amount,
    Length_of_Stay,
    Claim_Status
FROM healthcare_claims
ORDER BY Claim_Amount DESC
LIMIT 10;


-- ============================================================
-- 17. Data Quality Check - Missing Values
-- Purpose:
-- Identify missing values in important analytical fields.
-- ============================================================

SELECT
    SUM(CASE WHEN Patient_ID IS NULL THEN 1 ELSE 0 END) AS Missing_Patient_ID,
    SUM(CASE WHEN Age IS NULL THEN 1 ELSE 0 END) AS Missing_Age,
    SUM(CASE WHEN Gender IS NULL THEN 1 ELSE 0 END) AS Missing_Gender,
    SUM(CASE WHEN State IS NULL THEN 1 ELSE 0 END) AS Missing_State,
    SUM(CASE WHEN Diagnosis IS NULL THEN 1 ELSE 0 END) AS Missing_Diagnosis,
    SUM(CASE WHEN Provider IS NULL THEN 1 ELSE 0 END) AS Missing_Provider,
    SUM(CASE WHEN Insurance_Type IS NULL THEN 1 ELSE 0 END) AS Missing_Insurance_Type,
    SUM(CASE WHEN Claim_Amount IS NULL THEN 1 ELSE 0 END) AS Missing_Claim_Amount,
    SUM(CASE WHEN Claim_Status IS NULL THEN 1 ELSE 0 END) AS Missing_Claim_Status
FROM healthcare_claims;


-- ============================================================
-- 18. Data Quality Check - Duplicate Patient/Claim Records
-- Purpose:
-- Identify potential duplicate combinations of key fields.
-- ============================================================

SELECT
    Patient_ID,
    Admission_Date,
    Claim_Amount,
    COUNT(*) AS Duplicate_Count
FROM healthcare_claims
GROUP BY
    Patient_ID,
    Admission_Date,
    Claim_Amount
HAVING COUNT(*) > 1
ORDER BY Duplicate_Count DESC;


-- ============================================================
-- End of SQL Analysis
-- ============================================================
