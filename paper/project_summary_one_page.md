One-Page Project Summary
Project Title

Designing a Blockchain-Inspired Audit Trail for Machine Learning Models Used in Heart Disease Risk Prediction

Project Overview

This project is an independent health AI and biomedical informatics research prototype that combines heart disease risk prediction, machine learning, deep learning, reproducibility, and blockchain-inspired model governance. The project uses the UCI Heart Disease dataset to train and compare multiple prediction models while creating a tamper-evident audit trail that records dataset versions, model versions, hyperparameters, performance metrics, and linked model history.

The goal is not to create a clinically deployable diagnostic tool. Instead, the goal is to demonstrate how health AI workflows can be made more transparent, reproducible, and accountable through structured documentation and auditability.

Research Question

How can blockchain-inspired audit trails improve transparency, reproducibility, and accountability for machine learning and deep learning models used in heart disease risk prediction?

Methods

The project uses a cleaned version of the UCI Heart Disease dataset with a binary target variable:

0 = no heart disease
1 = heart disease present

Three traditional machine learning models were compared in Version 2:

Logistic Regression
Random Forest
Gradient Boosting

Version 3 added a TensorFlow/Keras neural network model as a deep learning baseline. The neural network used a multilayer perceptron architecture with 13 input features, two hidden dense layers, ReLU activation, a sigmoid output layer, Adam optimization, binary cross-entropy loss, and early stopping.

The project also includes reusable Python scripts for data processing, model training, evaluation, audit trail construction, tamper detection, and feature importance analysis.

Model Comparison Results
Model	Type	Accuracy	Precision	Recall	F1 Score	ROC-AUC
Logistic Regression	Traditional ML baseline	83.3%	84.6%	78.6%	81.5%	94.9%
Random Forest	Tree-based ML	85.0%	88.0%	78.6%	83.0%	94.1%
Gradient Boosting	Boosted tree model	76.7%	76.9%	71.4%	74.1%	88.3%
Neural Network / MLP	Deep learning baseline	85.0%	88.0%	78.6%	83.0%	94.9%

The neural network performed competitively with the traditional machine learning models, but it did not clearly outperform them. This suggests that deep learning can be added successfully to the workflow, but traditional machine learning models may remain highly competitive for small structured clinical datasets.

Audit Trail Design

The blockchain-inspired audit trail records each model run as a linked audit block. Each block includes:

Dataset name and dataset version
Dataset hash
Model name and model version
Model type
Training date
Features used
Hyperparameters
Performance metrics
Previous block hash
Current block hash

Version 3 expanded the audit chain to four blocks:

Block 1: Logistic Regression
Block 2: Random Forest
Block 3: Gradient Boosting
Block 4: Neural Network / MLP

The neural network block also records deep learning-specific details, including model architecture, number of layers, activation functions, optimizer, learning rate, epochs planned, epochs trained, batch size, loss function, and early stopping settings.

Interpretation

The neural network was added to evaluate whether a deep learning model could improve prediction performance and to demonstrate how deep learning model details can be included in a health AI audit trail. The neural network performed well, but signs of possible overfitting appeared during training. Training accuracy increased to approximately 87.8%, while validation accuracy peaked around 77.1% and later remained closer to 72.9%.

This result is important because it shows that deep learning is not automatically superior in every biomedical prediction task. For small structured datasets, traditional machine learning models may offer similar performance with less complexity and greater interpretability.

Health AI Governance Relevance

This project focuses on model governance rather than only model performance. In health AI, predictive models should be documented, reproducible, interpretable, and auditable. This project supports those goals by combining:

Machine learning and deep learning model comparison
Feature importance analysis
Reusable Python code
Reproducibility files
Hash-based audit records
Tamper-evident model history
A research-style paper draft
Current Repository Outputs

Key project files include:

README.md
notebooks/heart_disease_model_comparison_v2.ipynb
notebooks/heart_disease_deep_learning_v3.ipynb
results/model_comparison_v2.csv
results/model_comparison_v3.csv
results/audit_chain_v2.json
results/audit_chain_v3.json
results/tamper_detection_results_v2.json
results/feature_importance_v2.csv
results/feature_importance_v2.png
src/data_processing.py
src/model_training.py
src/evaluation.py
src/audit_trail.py
src/tamper_detection.py
src/feature_importance.py
paper/blockchain_audit_trail_heart_disease_research_paper_draft.md
requirements.txt
.gitignore
Future Work

Future versions may include additional datasets, fairness and bias testing, improved neural network regularization, deep learning interpretability methods such as SHAP or LIME, improved tamper-detection reporting, and more complete blockchain or distributed ledger implementation.

Disclaimer

This project is for educational and research portfolio purposes only. It is not intended for clinical diagnosis, treatment decisions, or direct medical recommendations. The models have not been clinically validated and should not be used as medical decision-making tools.
