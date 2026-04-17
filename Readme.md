## Patient Analytics Dashboard 

An AI-powered Healthcare Analytics Dashboard built to analyze Patient data, predict hospital readmissions, and enhance operational efficency in hospitals.

## Project Overview 

The patient Analytics Dashboard is an AI-powered healthcare-solution designed to analyze patient data and deliver actionable insights for improved clinical and operational decision-making. 
It leverageas machine learning techniques to Predict patient readmissions and Identify high-risk cases.

The project integrates SQL- based Data Management, Python-driven analysis, and interactive Visualizations to provide a comprehensive view of hospital performance and patient outcomes. It is inspired by real-world hospital workflow challenges.

## Business Challenge 

Healthare institutions generate large volumes of patient data, but often lack the stack to convert this data into actionable insights. This results in challenges such as identifying high-risk patients, reducing hospital readmissions, and efficiently managing resources.

Without data-driven systems, decission making remains reactive rather than proactive. This creates a need of intelligent solutions that can support better clinical and Operational outcomes.

## Objectives

- Analyze patient data to identify key trend and patterns
- Develop machine learning models to predict patient readmissions
- Identify high-risk patients for procative healthcare management
- Creative interactive Dashboards for data Visualizaton insights
- Support data driven decision-making in hospital operations

## Key Features

- Advanced analysis of patient data to uncover meaningful trends
- Machine-learning-driven prediction of patient readmissions
- Early identification of high risk patients for procative care
- KPI monitoring including average high length of stay and patient volume
- Department-level performance insights for opertional effciency
- Interactive Dashboard for intuitive data Visualization and decision making

  ## Tech stack

  - Python(Pandas, Numpy) for data cleaning, Preprocessing, and exploratory data analysis
  - SQL for structured data storage, quering, and Database Management
  - Power BI/Matplotlib for interactive data visualization and Dashboard development
  - Machine learning
      - Logistic Regression for predicting patient readmissions and analyzing risk factors

   This technology stack enables efficient data processing, predictive analytics, and data driven decision-making in healthcare.

  ## Machine learning $ Model Evaluation

  This project utilizes a logistic Regression model to predict patient readmissions based on historical healthcare data.
Data processing
- Data cleaning and preprocessing
- Handling missing values
- Encoding categorical variables using Label Encoding
- Feature selection for model training

Model Development 
- Implemented Logistic Regression for binary classification (readmitted vs not readmitted)
- Trained the model on patient data to identify patterns and risk factors

  Model Evaluation

  The performance of logistic Regression model was evaluated using standard classification metrics to ensure reliability and effectiveness.
   ### 📈 Model Accuracy

The Logistic Regression model achieved an accuracy of **53%**, indicating moderate overall prediction performance. While the model demonstrates reasonable capability in identifying readmitted patients, further optimization is required to improve overall accuracy and reduce misclassifications.

-  Precision: 54% refecting the model ability to correctly identify patients who are likely to be readmitted.
-  Recall: 53% , indicating the model's effectiveness in identifying actual readmitted patients, with stronger performance and high- risk cases.
-  F1-Score: 50%, repersenting a balance between precision and recall, with stronger performance in identifying readmitted patients.
- Confusion Matrix provided a detailed breakdown of true positives, true negatives, False positives and False negatives.helping to understand the model's prediction behavior.
### 📊 Confusion Matrix Interpretation

The confusion matrix provides a detailed breakdown of the model’s predictions:

* **True Negatives (29):** Correctly predicted non-readmitted patients
* **False Positives (72):** Patients incorrectly predicted as readmitted
* **False Negatives (23):** Readmitted patients incorrectly predicted as non-readmitted
* **True Positives (76):** Correctly predicted readmitted patients

This analysis shows that the model performs better in identifying readmitted patients but produces some false positives, indicating scope for improvement.
[[29 72]
 [23 76]]

 ### 📑 Classification Report

The classification report provides a detailed evaluation of the model’s performance across different metrics:

* For **non-readmitted patients (Class 0)**, the model achieved:

  * Precision: 0.56
  * Recall: 0.29
  * F1-score: 0.38

* For **readmitted patients (Class 1)**, the model achieved:

  * Precision: 0.51
  * Recall: 0.77
  * F1-score: 0.62

The results indicate that the model performs significantly better in identifying readmitted patients, with higher recall and F1-score for Class 1. This is particularly important in healthcare scenarios, where correctly identifying high-risk patients is critical.

However, the lower recall for non-readmitted patients suggests that the model may produce false positives, indicating opportunities for further optimization and improvement.

## 📸 Dashboard Preview

The dashboard provides an interactive visualization of patient data, enabling users to explore key metrics such as patient distribution, readmission trends, and department-wise performance.

It helps hospital administrators and healthcare professionals gain quick insights and make data-driven decisions efficiently.

## 💡 Real-World Impact

This project can help healthcare organizations:

* Identify high-risk patients for early intervention
* Reduce hospital readmission rates
* Improve resource allocation and operational efficiency
* Support data-driven decision-making

It is inspired by real-world hospital workflow challenges and aims to enhance patient care using data and AI.

## 🚀 Future Scope

* Improve model performance using advanced machine learning techniques
* Implement real-time patient monitoring and alerts
* Integrate with hospital appointment systems
* Develop a web-based application using Streamlit
* Apply clustering techniques for patient flow optimization

* [![Dashboard Preview](images/screenshot.png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)

* ## 🚀 Full Preview (Click Any Image)

[![Screenshot](Screenshot%20(186).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(189).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(190).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(191).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(192).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(194).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(195).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(201).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(202).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(209).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(213).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(217).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(224).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(226).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(228).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(229).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)
[![Screenshot](Screenshot%20(230).png)](https://Manshu-27.github.io/Patient-Analytics-Dashboard/)







  
   
  

  

  

  
        


  
 

- 
- 

- 

