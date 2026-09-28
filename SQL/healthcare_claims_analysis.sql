-- ============================================================
-- Healthcare Claims & Patient Analytics
-- SQL Analysis
-- ============================================================
-- Purpose:
-- Analyze healthcare claims data to understand
-- patient utilization, claim costs, providers,
-- diagnoses, insurance types, and claim trends.
--
-- Dataset:
-- healthcare_claims.csv
-- ============================================================
-- ============================================================
-- 1. Total Number of Claims
-- ============================================================

SELECT COUNT(*) AS total_claims
FROM healthcare_claims;

-- ============================================================
-- 2. Total Number of Patients
-- ============================================================

SELECT COUNT(DISTINCT Patient_ID) AS Total_Patients
FROM healthcare_claims;


-- ============================================================
-- 3. Total Claim Amount
-- ============================================================

SELECT SUM(Claim_Amount) AS Total_Claim_Amount
FROM healthcare_claims;


-- ============================================================
-- 4. Average Claim Amount
-- ============================================================

SELECT AVG(Claim_Amount) AS Average_Claim_Amount
FROM healthcare_claims;

-- ============================================================
-- 5. Claims by Diagnosis
-- ============================================================

SELECT
    Diagnosis,
    COUNT(*) AS Total_Claims,
    SUM(Claim_Amount) AS Total_Claim_Amount,
    AVG(Claim_Amount) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Diagnosis
ORDER BY Total_Claim_Amount DESC;


-- ============================================================
-- 6. Claims by Provider
-- ============================================================

SELECT
    Provider,
    COUNT(*) AS Total_Claims,
    SUM(Claim_Amount) AS Total_Claim_Amount,
    AVG(Claim_Amount) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Provider
ORDER BY Total_Claim_Amount DESC;


-- ============================================================
-- 7. Claims by Insurance Type
-- ============================================================

SELECT
    Insurance_Type,
    COUNT(*) AS Total_Claims,
    SUM(Claim_Amount) AS Total_Claim_Amount,
    AVG(Claim_Amount) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Insurance_Type
ORDER BY Total_Claim_Amount DESC;


-- ============================================================
-- 8. Claims by State
-- ============================================================

SELECT
    State,
    COUNT(*) AS Total_Claims,
    SUM(Claim_Amount) AS Total_Claim_Amount,
    AVG(Claim_Amount) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY State
ORDER BY Total_Claim_Amount DESC;


-- ============================================================
-- 9. Claims by Status
-- ============================================================

SELECT
    Claim_Status,
    COUNT(*) AS Total_Claims,
    SUM(Claim_Amount) AS Total_Claim_Amount,
    AVG(Claim_Amount) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Claim_Status
ORDER BY Total_Claims DESC;

-- ============================================================
-- 10. Monthly Claim Trends
-- ============================================================

SELECT
    strftime('%Y-%m', Admission_Date) AS Claim_Month,
    COUNT(*) AS Total_Claims,
    SUM(Claim_Amount) AS Total_Claim_Amount,
    AVG(Claim_Amount) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Claim_Month
ORDER BY Claim_Month;

-- ============================================================
-- 11. High-Cost Claims
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
-- ============================================================

SELECT
    Diagnosis,
    COUNT(*) AS Total_Claims,
    AVG(Length_of_Stay) AS Average_Length_of_Stay,
    AVG(Claim_Amount) AS Average_Claim_Amount
FROM healthcare_claims
GROUP BY Diagnosis
ORDER BY Average_Length_of_Stay DESC;

-- ============================================================
-- 13. Claim Status Percentage
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
-- 14. Top 10 Most Expensive Claims
-- ============================================================

SELECT
    Patient_ID,
    Diagnosis,
    Provider,
    Claim_Amount,
    Length_of_Stay,
    Claim_Status
FROM healthcare_claims
ORDER BY Claim_Amount DESC
LIMIT 10;
