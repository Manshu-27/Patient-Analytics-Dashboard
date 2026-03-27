
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import os 

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("App started...")

print("Hospital Smart dashboard")


df = pd.read_csv("hospital_data.csv")
print("csv loaded successfully")
print("Columns:", df.columns.tolist())
print("Number of rows:", len(df))

df['patient_ID'] = range(1, len(df) +1)

departments = ['cardiology', 'Neurology', 'Orthopedic', 'General']
df['Department'] = np.random.choice(departments, size=len(df))

admission_status = ['Emergency', 'Routine']
df['Admission'] = np.random.choice(admission_status, size=len(df))

df.to_csv("hospital_updated.csv", index=False)
print("999 updated with new columns")

print("Hospital Data preview:")
print(df.head())

total_patients = len(df)
print("\nTotal patients:", total_patients)

print(df.columns)

dept_counts = df['Department'].value_counts()

print("\nPatients per department:")
print(dept_counts)

print("Average Age:", df['age'].mean())

print(df.columns)

df['cost'] = df['num_procedures'] * 5000 + df['days_in_hospital']
print("Total Revenue:", df['cost'].sum())

print(df.columns)

print(df['gender'].value_counts())

plt.figure(figsize=(8,5))
dept_counts.plot(kind='bar')

plt.title("Patients per Department")
plt.xlabel("Departments")
plt.ylabel("Number of patients")

plt.show()

admission_counts = df['Admission'].value_counts()

plt.figure(figsize=(6,6))
admission_counts.plot(kind='pie', autopct='%1.1f%%')

plt.title("Admission Type Distribution")
plt.show()

plt.hist(df['age'])
plt.title("Age Distribution")
plt.show()

df.groupby('Department')['cost'].sum().plot(kind='bar')
plt.title("Revenue per Department")
plt.show()

le = LabelEncoder()

df['gender'] = le.fit_transform(df['gender'])
df['Department'] = le.fit_transform(df['Department'])
df['Admission'] = le.fit_transform(df['Admission'])

X = df[['age', 'num_procedures', 'days_in_hospital', 'comorbidity_score']]
y = df['Admission']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

print("\nClassification Report:\n", classification_report(y_test, y_pred))



























