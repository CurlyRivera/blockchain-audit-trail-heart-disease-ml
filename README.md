# Designing a Blockchain-Inspired Audit Trail for Machine Learning Models Used in Heart Disease Risk Prediction

## Project Overview

This project develops a Python-based heart disease risk prediction model and pairs it with a blockchain-inspired audit trail that records dataset versions, model versions, performance metrics, and tamper-evident model history to improve transparency, reproducibility, and accountability in health AI workflows.

## Key Terms

- **Machine learning model:** A computer model that learns patterns from data and uses those patterns to make predictions.
- **Heart disease risk prediction:** The use of clinical variables, such as age, cholesterol, blood pressure, chest pain type, and maximum heart rate, to estimate whether heart disease may be present.
- **Blockchain-inspired audit trail:** A record-keeping system inspired by blockchain principles that tracks important changes to datasets, models, and results in a way that is difficult to alter without detection.
- **Dataset version:** A specific version of the data used to train or evaluate a model.
- **Model version:** A specific version of a machine learning model, including the algorithm, settings, features, and performance results used during that run.
- **Dataset hash:** A unique digital fingerprint created from a dataset; if the dataset changes, the hash also changes.
- **Tamper-evident model history:** A model record system where changes to past data, results, or audit records can be detected.
- **Performance metrics:** Numerical measures used to evaluate how well a model performs, such as accuracy, precision, recall, F1 score, and ROC-AUC.
- **Reproducibility:** The ability to repeat the same workflow and obtain the same or similar results.
- **Health AI workflow:** The process of preparing health data, training a model, evaluating its performance, and tracking the model’s development for use in health-related decision-making.

## Research Question

How can blockchain-inspired audit trails improve transparency, reproducibility, and accountability for machine learning models used in heart disease risk prediction?

## Project Goals

- Build a machine learning model for heart disease risk prediction.
- Create a blockchain-inspired audit trail to track dataset versions, model versions, model performance, and model history.
- Demonstrate how tamper-evident records can improve trust and reproducibility in health AI workflows.
- Connect concepts from finance, blockchain technology, medical studies, and biomedical informatics.

## Dataset

This project uses a public heart disease dataset for machine learning model development and audit trail testing. The dataset includes clinical variables commonly used in heart disease risk prediction, such as age, sex, chest pain type, resting blood pressure, cholesterol, maximum heart rate, and heart disease diagnosis.

For this project, the target variable is treated as a binary classification outcome:
- `0` = no heart disease
- `1` = heart disease present

The dataset is used to train and evaluate heart disease risk prediction models. Each dataset version is also recorded in the blockchain-inspired audit trail using a dataset hash to support reproducibility, transparency, and tamper-evident model history.

Dataset source: UCI Machine Learning Repository - Heart Disease Dataset.

## Version 1

Version 1 trains a logistic regression model to predict heart disease presence using the UCI Heart Disease dataset. The model is evaluated using accuracy, precision, recall, F1 score, and ROC-AUC. A blockchain-inspired audit record is created for the model run, including the dataset hash, model version, features used, performance metrics, previous block hash, and current block hash.

### Version 1 Results

- Accuracy: 83.3%
- Precision: 84.6%
- Recall: 78.6%
- F1 Score: 81.5%
- ROC-AUC: 94.9%

## Version 2

Version 2 expands the project by comparing multiple machine learning models, creating a multi-block blockchain-inspired audit chain, testing tamper detection, and adding feature importance analysis for model explainability. This version compares Logistic Regression, Random Forest, and Gradient Boosting using the same cleaned UCI Heart Disease dataset and the same train-test split.

### Version 2 Model Comparison Results

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 83.3% | 84.6% | 78.6% | 81.5% | 94.9% |
| Random Forest | 85.0% | 88.0% | 78.6% | 83.0% | 94.1% |
| Gradient Boosting | 76.7% | 76.9% | 71.4% | 74.1% | 88.3% |

Random Forest achieved the highest accuracy and F1 score, while Logistic Regression achieved the highest ROC-AUC.

## Version 2 Audit Chain

Version 2 creates a three-block audit chain:

- Block 1: Logistic Regression
- Block 2: Random Forest
- Block 3: Gradient Boosting

Each block records the dataset hash, model version, training date, features used, hyperparameters, performance metrics, previous block hash, and current block hash. This creates a linked model history where each model record is connected to the previous model record.

## Version 2 Tamper Detection

Tamper-detection testing was performed by intentionally modifying audit records and checking whether the recalculated hash still matched the saved hash. The original audit chain was valid, while the tampered versions were detected as invalid.

Tamper tests included:

- Changing a model performance metric
- Changing a model name
- Changing the dataset hash
- Changing a previous block hash

## Version 2 Feature Importance

Feature importance analysis was added using Random Forest and Gradient Boosting. The most important variables included thalassemia-related information, chest pain type, number of major vessels, ST depression, age, cholesterol, and maximum heart rate.

### Version 2 Outputs

- `notebooks/heart_disease_model_comparison_v2.ipynb` - Version 2 notebook for model comparison, audit chain construction, tamper detection, and feature importance analysis.
- `results/model_comparison_v2.csv` - Model comparison results for Logistic Regression, Random Forest, and Gradient Boosting.
- `results/audit_chain_v2.json` - Multi-block blockchain-inspired audit chain.
- `results/tamper_detection_results_v2.json` - Tamper-detection test results.
- `results/feature_importance_v2.csv` - Feature importance results.
- `results/feature_importance_v2.png` - Feature importance chart.

## Audit Trail Features

Each model run records:

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

## Tools Used

- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- hashlib
- GitHub

## Project Status

This project is currently in early development. Version 1 established a baseline logistic regression model and created an initial blockchain-inspired audit record. Version 2 expanded the project by comparing multiple machine learning models, creating a multi-block audit chain, testing tamper detection, and adding feature importance analysis for model explainability. Future versions may include additional datasets, more advanced machine learning models, fairness and bias testing, and more complete blockchain or distributed ledger implementation.

## How to Reproduce This Project

1. Open `notebooks/heart_disease_model_comparison_v2.ipynb`.
2. Run all notebook cells from top to bottom.
3. The notebook will generate model comparison results, audit chain records, tamper-detection results, and feature importance outputs in the `results/` folder.

## Repository Structure

- data/ - Dataset files or notes about the dataset source.
- notebooks/ - Jupyter notebooks for data exploration, model building, model comparison, audit trail construction, tamper detection, and feature importance analysis.
- src/ - Python scripts for reusable functions and audit trail logic.
- results/ - Model performance metrics, audit trail records, tamper-detection results, feature importance tables, and charts.
- paper/ - Research-style write-up for the project.
- poster/ - Future one-page research poster.
- references/ - Notes, articles, and citations related to heart disease prediction, health AI, and blockchain-inspired audit trails.
