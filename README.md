# Designing a Blockchain-Inspired Audit Trail for Machine Learning Models Used in Heart Disease Risk Prediction

## Project Overview

This project develops a Python-based heart disease risk prediction model and pairs it with a blockchain-inspired audit trail that records dataset versions, model versions, performance metrics, and tamper-evident model history to improve transparency, reproducibility, and accountability in health AI workflows.

## Research Question

How can blockchain-inspired audit trails improve transparency, reproducibility, and accountability for machine learning models used in heart disease risk prediction?

## Project Goals

- Build a machine learning model for heart disease risk prediction.
- Create a blockchain-inspired audit trail to track dataset versions, model versions, model performance, and model history.
- Demonstrate how tamper-evident records can improve trust and reproducibility in health AI workflows.
- Connect concepts from finance, blockchain technology, medical studies, and biomedical informatics.

## Dataset

This project uses a public heart disease dataset for machine learning model development and audit trail testing. The dataset will include clinical variables commonly used in heart disease risk prediction, such as age, sex, chest pain type, resting blood pressure, cholesterol, maximum heart rate, and heart disease diagnosis.

For this project, the target variable will be treated as a binary classification outcome:
- `0` = no heart disease
- `1` = heart disease present

The dataset will be used to train and evaluate heart disease risk prediction models. Each dataset version will also be recorded in the blockchain-inspired audit trail using a dataset hash to support reproducibility, transparency, and tamper-evident model history.

Dataset source: UCI Machine Learning Repository - Heart Disease Dataset.

## Version 1

Version 1 trains a logistic regression model to predict heart disease presence using the UCI Heart Disease dataset. The model is evaluated using accuracy, precision, recall, F1 score, and ROC-AUC. A blockchain-inspired audit record is created for the model run, including the dataset hash, model version, features used, performance metrics, previous block hash, and current block hash.

### Version 1 Results

- Accuracy: 83.3%
- Precision: 84.6%
- Recall: 78.6%
- F1 Score: 81.5%
- ROC-AUC: 94.9%

## Audit Trail Features

Each model run will record:

- Dataset name
- Dataset version
- Dataset hash
- Model name
- Model version
- Training date
- Features used
- Performance metrics
- Previous block hash
- Current block hash

## Tools Used / Planned

- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- hashlib
- GitHub

## Project Status

This project is currently in early development. Version 1 has been completed using a logistic regression model and a blockchain-inspired audit trail record. Future versions will expand the audit trail, compare additional machine learning models, and include tamper-detection testing.

## Repository Structure

- `data/` - Dataset files or notes about the dataset source.
- `notebooks/` - Jupyter notebooks for data exploration, model building, and evaluation.
- `src/` - Python scripts for reusable functions and audit trail logic.
- `results/` - Model performance metrics, charts, and output files.
- `paper/` - Research-style write-up for the project.
- `poster/` - Future one-page research poster.
- `references/` - Notes, articles, and citations related to heart disease prediction, health AI, and blockchain-inspired audit trails.
