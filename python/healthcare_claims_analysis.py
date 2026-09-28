#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os

os.getcwd()


# In[5]:


import pandas as pd

file_path = r"E:\Srikanth\Data_Analytics_Portfolio\healthcare-analytics-project\data\healthcare_claims.csv"

df = pd.read_csv(file_path)

df.head()


# In[6]:


df.shape


# In[7]:


df.columns.tolist()


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# In[10]:


df.duplicated().sum()


# In[11]:


df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'])

df.info()


# In[12]:


df[['Admission_Date', 'Discharge_Date']].head()


# In[13]:


summary = {
    "Total Claims": len(df),
    "Total Claim Amount": df["Claim_Amount"].sum(),
    "Average Claim Amount": df["Claim_Amount"].mean(),
    "Average Length of Stay": df["Length_of_Stay"].mean(),
    "Average Patient Age": df["Age"].mean()
}

summary


# In[14]:


print(f"Total Claims: {len(df):,}")
print(f"Total Claim Amount: ${df['Claim_Amount'].sum():,.2f}")
print(f"Average Claim Amount: ${df['Claim_Amount'].mean():,.2f}")
print(f"Average Length of Stay: {df['Length_of_Stay'].mean():.1f} days")
print(f"Average Patient Age: {df['Age'].mean():.1f} years")


# In[15]:


claim_status = df['Claim_Status'].value_counts()

claim_status


# In[16]:


claim_status_pct = df['Claim_Status'].value_counts(normalize=True) * 100

claim_status_pct.round(2)


# In[17]:


df.groupby('Claim_Status')['Claim_Amount'].agg(
    ['count', 'sum', 'mean']
).round(2)


# In[18]:


diagnosis_counts = df['Diagnosis'].value_counts()

diagnosis_counts


# In[19]:


diagnosis_analysis = df.groupby('Diagnosis')['Claim_Amount'].agg(
    ['count', 'sum', 'mean']
).sort_values('sum', ascending=False)

diagnosis_analysis.round(2)


# In[20]:


diagnosis_status = pd.crosstab(
    df['Diagnosis'],
    df['Claim_Status']
)

diagnosis_status


# In[21]:


diagnosis_status_pct = pd.crosstab(
    df['Diagnosis'],
    df['Claim_Status'],
    normalize='index'
) * 100

diagnosis_status_pct.round(2)


# In[22]:


df['Insurance_Type'].value_counts()
insurance_analysis = df.groupby('Insurance_Type')['Claim_Amount'].agg(
    ['count', 'sum', 'mean']
).sort_values('sum', ascending=False)

insurance_analysis.round(2)
insurance_status = pd.crosstab(
    df['Insurance_Type'],
    df['Claim_Status'],
    normalize='index'
) * 100

insurance_status.round(2)


# In[23]:


df['Insurance_Type'].value_counts()


# In[24]:


insurance_analysis = df.groupby('Insurance_Type')['Claim_Amount'].agg(
    ['count', 'sum', 'mean']
).sort_values('sum', ascending=False)

insurance_analysis.round(2)


# In[25]:


df['Provider'].nunique()


# In[26]:


df['Provider'].value_counts()


# In[27]:


provider_analysis = df.groupby('Provider')['Claim_Amount'].agg(
    ['count', 'sum', 'mean']
).sort_values('sum', ascending=False)

provider_analysis.round(2)


# In[28]:


provider_status = pd.crosstab(
    df['Provider'],
    df['Claim_Status'],
    normalize='index'
) * 100

provider_status.round(2)


# In[29]:


df['State'].nunique()


# In[30]:


df['State'].value_counts()


# In[31]:


state_analysis = df.groupby('State')['Claim_Amount'].agg(
    ['count', 'sum', 'mean']
).sort_values('sum', ascending=False)

state_analysis.round(2)


# In[32]:


state_status = pd.crosstab(
    df['State'],
    df['Claim_Status'],
    normalize='index'
) * 100

state_status.round(2)


# In[33]:


df['Age'].describe()


# In[34]:


df['Gender'].value_counts()


# In[35]:


gender_analysis = df.groupby('Gender')['Claim_Amount'].agg(
    ['count', 'sum', 'mean']
).sort_values('sum', ascending=False)

gender_analysis.round(2)


# In[36]:


bins = [0, 18, 35, 50, 65, 100]
labels = ['0-18', '19-35', '36-50', '51-65', '66+']

df['Age_Group'] = pd.cut(
    df['Age'],
    bins=bins,
    labels=labels
)

df['Age_Group'].value_counts().sort_index()


# In[41]:


df['Length_of_Stay'].describe()


# In[42]:


los_analysis = df.groupby('Length_of_Stay')['Claim_Amount'].agg(
    ['count', 'sum', 'mean']
).sort_index()

los_analysis.round(2)


# In[43]:


df[['Length_of_Stay', 'Claim_Amount']].corr()


# In[44]:


import matplotlib.pyplot as plt

claim_status = df['Claim_Status'].value_counts()

claim_status.plot(kind='bar')

plt.title('Healthcare Claims by Claim Status')
plt.xlabel('Claim Status')
plt.ylabel('Number of Claims')
plt.xticks(rotation=0)
plt.show()


# In[45]:


diagnosis_cost = df.groupby('Diagnosis')['Claim_Amount'].sum().sort_values(ascending=False)

diagnosis_cost.plot(kind='bar')

plt.title('Total Claim Amount by Diagnosis')
plt.xlabel('Diagnosis')
plt.ylabel('Total Claim Amount ($)')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[46]:


diagnosis_avg = df.groupby('Diagnosis')['Claim_Amount'].mean().sort_values(ascending=False)

diagnosis_avg.plot(kind='bar')

plt.title('Average Claim Amount by Diagnosis')
plt.xlabel('Diagnosis')
plt.ylabel('Average Claim Amount ($)')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[47]:


insurance_cost = df.groupby('Insurance_Type')['Claim_Amount'].sum().sort_values(ascending=False)

insurance_cost.plot(kind='bar')

plt.title('Total Claim Amount by Insurance Type')
plt.xlabel('Insurance Type')
plt.ylabel('Total Claim Amount ($)')
plt.xticks(rotation=0)
plt.show()


# In[48]:


insurance_count = df['Insurance_Type'].value_counts()

insurance_count.plot(kind='bar')

plt.title('Number of Claims by Insurance Type')
plt.xlabel('Insurance Type')
plt.ylabel('Number of Claims')
plt.xticks(rotation=0)
plt.show()


# In[49]:


provider_cost = df.groupby('Provider')['Claim_Amount'].sum().sort_values(ascending=False)

provider_cost.plot(kind='bar')

plt.title('Total Claim Amount by Provider')
plt.xlabel('Provider')
plt.ylabel('Total Claim Amount ($)')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[50]:


state_cost = df.groupby('State')['Claim_Amount'].sum().sort_values(ascending=False)

state_cost.plot(kind='bar')

plt.title('Total Claim Amount by State')
plt.xlabel('State')
plt.ylabel('Total Claim Amount ($)')
plt.xticks(rotation=0)
plt.show()


# In[51]:


plt.scatter(df['Length_of_Stay'], df['Claim_Amount'])

plt.title('Length of Stay vs Claim Amount')
plt.xlabel('Length of Stay (Days)')
plt.ylabel('Claim Amount ($)')
plt.show()


# In[52]:


age_group_count = df['Age_Group'].value_counts().sort_index()

age_group_count.plot(kind='bar')

plt.title('Number of Claims by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Claims')
plt.xticks(rotation=0)
plt.show()


# In[53]:


gender_cost = df.groupby('Gender')['Claim_Amount'].mean()

gender_cost.plot(kind='bar')

plt.title('Average Claim Amount by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Claim Amount ($)')
plt.xticks(rotation=0)
plt.show()


# In[54]:


df['Admission_Month'] = df['Admission_Date'].dt.to_period('M')


# In[55]:


monthly_claims = df.groupby('Admission_Month').size()

monthly_claims.plot(kind='line', marker='o')

plt.title('Monthly Healthcare Claim Volume')
plt.xlabel('Month')
plt.ylabel('Number of Claims')
plt.xticks(rotation=45)
plt.show()


# In[56]:


monthly_cost = df.groupby('Admission_Month')['Claim_Amount'].sum()

monthly_cost.plot(kind='line', marker='o')

plt.title('Monthly Healthcare Claim Amount')
plt.xlabel('Month')
plt.ylabel('Total Claim Amount ($)')
plt.xticks(rotation=45)
plt.show()


# In[57]:


diagnosis_status = pd.crosstab(
    df['Diagnosis'],
    df['Claim_Status']
)

diagnosis_status.plot(kind='bar', stacked=True)

plt.title('Claim Status Distribution by Diagnosis')
plt.xlabel('Diagnosis')
plt.ylabel('Number of Claims')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Claim Status')
plt.show()


# In[58]:


output_file = r"E:\Srikanth\Data_Analytics_Portfolio\healthcare-analytics-project\data\healthcare_claims_cleaned.csv"

df.to_csv(output_file, index=False)

print("Cleaned dataset saved successfully!")


# In[ ]:




