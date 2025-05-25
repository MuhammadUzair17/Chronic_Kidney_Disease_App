# Chronic Kidney Disease (CKD) Prediction Project

This repository contains a machine learning project aimed at predicting the likelihood of Chronic Kidney Disease (CKD) using clinical and laboratory data. The project includes data preprocessing, model training, and a Streamlit web application for interactive prediction.

---

## Project Overview

Chronic Kidney Disease is a serious health condition characterized by gradual loss of kidney function over time. Early detection is critical to prevent progression to kidney failure requiring dialysis or transplantation. This project leverages machine learning techniques to provide an early diagnosis tool based on patient medical data.

---

## Dataset

- The dataset used is sourced from the UCI Machine Learning Repository CKD dataset.
- It contains 400 patient records with 24 clinical features and one target variable indicating CKD presence.
- Key features include:
  - Hemoglobin
  - Specific Gravity
  - Albumin
  - Serum Creatinine
  - Hypertension status
  - Diabetes Mellitus status
- The dataset has been preprocessed to handle missing values and normalize feature scales.

---

## Technologies and Libraries

- Python 3
- Libraries:
  - pandas, numpy for data manipulation
  - matplotlib, seaborn for visualization
  - scikit-learn for machine learning (feature selection, model training, evaluation)
  - joblib for model serialization
  - Streamlit for web app deployment
  - collections for counting classes

---

## Model Development

- Multiple classification algorithms were explored including Logistic Regression, Support Vector Machine (SVM), and K-Nearest Neighbors (KNN).
- Feature selection was performed using SelectKBest with ANOVA F-value.
- Data preprocessing pipeline includes imputation of missing values and scaling.
- Stratified K-Fold cross-validation and GridSearchCV were used for hyperparameter tuning.
- The final model is saved as `ckd.pkl`.

---

## Streamlit Web Application

- The app allows users to input medical parameters and receive a CKD risk prediction.
- Input features:
  - Hemoglobin (g/dl)
  - Specific Gravity
  - Albumin (g/dl)
  - Serum Creatinine (mg/dl)
  - Hypertension (Yes/No)
  - Diabetes Mellitus (Yes/No)
- Upon submission, the app displays the prediction result:
  - **CKD Detected** with recommendations to consult a nephrologist and follow medical advice.
  - **No CKD Detected** with general health tips.


