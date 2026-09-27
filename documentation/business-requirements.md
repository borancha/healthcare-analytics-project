# Healthcare Claims & Patient Analytics

## 1. Business Problem

The healthcare organization wants to better understand healthcare claim costs and utilization. Management needs visibility into patient demographics, medical conditions, provider activity, insurance types, claim status, and trends in healthcare spending.

## 2. Business Objective

The objective of this analysis is to identify patterns and trends in healthcare claims that can help stakeholders understand cost drivers, utilization patterns, and areas that may require further investigation.

## 3. Analytical Requirements

### Cost Analysis

- Calculate total claim amount.
- Calculate average claim amount.
- Identify diagnoses associated with higher claim costs.
- Analyze claim costs by healthcare provider.
- Analyze claim costs by insurance type.

### Utilization Analysis

- Calculate total number of claims.
- Calculate unique number of patients.
- Analyze claims by diagnosis.
- Analyze claims by state.
- Calculate average length of stay.

### Trend Analysis

- Analyze monthly claim volume.
- Analyze monthly claim amounts.
- Identify changes in healthcare utilization over time.

### Claim Status Analysis

- Analyze paid claims.
- Analyze pending claims.
- Analyze denied claims.
- Calculate the claim denial rate.

## 4. Key Performance Indicators

The dashboard should include:

- Total Patients
- Total Claims
- Total Claim Amount
- Average Claim Amount
- Average Length of Stay
- Claim Denial Rate

## 5. Key Business Questions

1. What is the total healthcare claim amount?
2. What is the average claim amount?
3. Which diagnoses have the highest claim costs?
4. Which providers have the highest claim amounts?
5. Which insurance types account for the largest claim amounts?
6. Which age groups have the highest utilization?
7. What are the monthly claim trends?
8. What percentage of claims are denied?
9. Which states have the highest claim volume?
10. Are there patterns between length of stay and claim amount?

## 6. Functional Requirements

The solution should allow users to:

- View overall healthcare claims and patient KPIs.
- Filter analysis by relevant patient, claim, provider, diagnosis, insurance, and geographic attributes.
- Analyze claim amounts across different categories.
- Compare claim volume and claim amounts over time.
- Review claim status distribution.
- Identify diagnoses and providers associated with higher claim amounts.
- Review patient utilization patterns.
- Interactively explore the data through Power BI visualizations.

## 7. Data Requirements

The analysis requires healthcare claims and patient-level information, including relevant fields such as:

- Patient information
- Patient demographics
- Diagnosis
- Provider
- Insurance type
- Claim amount
- Claim status
- Claim type
- State
- Hospital admission/discharge information
- Length of stay
- Claim date or relevant date fields

## 8. Assumptions

- The dataset is assumed to represent a sample healthcare claims population for analytical purposes.
- Claim amounts are assumed to be recorded consistently within the dataset.
- Patient identifiers are assumed to be unique where applicable.
- Missing or inconsistent data may affect certain calculations.
- The analysis identifies patterns in the available data and does not establish causation.
- Findings should be validated with appropriate business stakeholders before operational decisions are made.

## 9. Expected Deliverables

- Cleaned healthcare claims dataset
- SQL analysis
- Python exploratory analysis
- Power BI interactive dashboard
- Business insights
- Documentation of requirements and analysis

## 10. Stakeholders

Potential stakeholders include:

- Healthcare Operations Management
- Finance / Revenue Management
- Claims Management Team
- Provider Management Team
- Business Intelligence / Analytics Team

## 11. Acceptance Criteria

The project will meet the requirements when:

- Required healthcare data is available and suitable for analysis.
- Key KPIs can be calculated from the available data.
- Users can interact with the Power BI dashboard using relevant filters.
- Claim costs and utilization can be analyzed across relevant dimensions.
- Monthly trends can be reviewed.
- Claim status and denial metrics can be analyzed.
- The dashboard provides a clear view of the defined business questions.
- Python and SQL analysis support the overall analytical objectives.
- Project documentation clearly describes the requirements, analysis, and deliverables.

## 12. Success Criteria

The project will be considered successful when stakeholders can use the dashboard to quickly understand healthcare claim costs, utilization patterns, claim status, and major trends.

The completed solution should provide a structured analytical workflow from business requirements through data analysis and visualization.
