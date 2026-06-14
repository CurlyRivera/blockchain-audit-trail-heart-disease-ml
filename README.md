# Designing a Blockchain-Inspired Audit Trail for Machine Learning Models Used in Heart Disease Risk Prediction

## Project Overview

This project develops a Python-based heart disease risk prediction workflow and pairs it with a blockchain-inspired audit trail to improve transparency, reproducibility, and accountability in health AI model development.

The project uses the UCI Heart Disease dataset to compare traditional machine learning models and a deep learning model while recording dataset versions, model versions, performance metrics, model settings, and tamper-evident model history.

The goal of this project is not to create a clinically deployable diagnostic tool. Instead, this project serves as a research-style prototype showing how predictive modeling, deep learning, reproducible code, and blockchain-inspired auditability can be combined to support more transparent health AI workflows.

## Key Terms

- **Machine learning model:** A computer model that learns patterns from data and uses those patterns to make predictions.
- **Deep learning model:** A type of machine learning model, often based on neural networks, that can learn complex patterns from data.
- **Heart disease risk prediction:** The use of clinical variables, such as age, cholesterol, blood pressure, chest pain type, and maximum heart rate, to estimate whether heart disease may be present.
- **Blockchain-inspired audit trail:** A record-keeping system inspired by blockchain principles that tracks important changes to datasets, models, and results in a way that is difficult to alter without detection.
- **Dataset version:** A specific version of the data used to train or evaluate a model.
- **Model version:** A specific version of a machine learning model, including the algorithm, settings, features, and performance results used during that run.
- **Dataset hash:** A unique digital fingerprint created from a dataset; if the dataset changes, the hash also changes.
- **Tamper-evident model history:** A model record system where changes to past data, results, or audit records can be detected.
- **Performance metrics:** Numerical measures used to evaluate how well a model performs, such as accuracy, precision, recall, F1 score, and ROC-AUC.
- **Reproducibility:** The ability to repeat the same workflow and obtain the same or similar results.
- **Health AI workflow:** The process of preparing health data, training a model, evaluating its performance, and tracking the model’s development for use in health-related research.

## Research Question

How can blockchain-inspired audit trails improve transparency, reproducibility, and accountability for machine learning and deep learning models used in heart disease risk prediction?

## Project Goals

- Build heart disease risk prediction models using structured clinical data.
- Compare traditional machine learning models with a neural network / deep learning baseline.
- Create a blockchain-inspired audit trail to track dataset versions, model versions, model settings, performance metrics, and model history.
- Demonstrate how tamper-evident records can improve trust, reproducibility, and accountability in health AI workflows.
- Organize the project into notebooks, reusable Python scripts, reproducible outputs, and a research-style paper.
- Connect concepts from finance, blockchain technology, medical studies, biomedical informatics, machine learning, and health AI governance.

## Dataset

This project uses the UCI Heart Disease dataset for machine learning model development and audit trail testing. The dataset includes clinical variables commonly used in heart disease prediction, such as age, sex, chest pain type, resting blood pressure, cholesterol, maximum heart rate, and heart disease diagnosis.

For this project, the target variable is treated as a binary classification outcome:

- `0` = no heart disease
- `1` = heart disease present

The dataset is used to train and evaluate heart disease risk prediction models. Each dataset version is also recorded in the blockchain-inspired audit trail using a dataset hash to support reproducibility, transparency, and tamper-evident model history.

Dataset source: UCI Machine Learning Repository - Heart Disease Dataset.

## Version 1: Baseline Model and Initial Audit Record

Version 1 trained a logistic regression model to predict heart disease presence using the UCI Heart Disease dataset. The model was evaluated using accuracy, precision, recall, F1 score, and ROC-AUC. A blockchain-inspired audit record was created for the model run, including the dataset hash, model version, features used, performance metrics, previous block hash, and current block hash.

### Version 1 Results

- Accuracy: 83.3%
- Precision: 84.6%
- Recall: 78.6%
- F1 Score: 81.5%
- ROC-AUC: 94.9%

## Version 2: Traditional Machine Learning Comparison and Audit Chain

Version 2 expanded the project by comparing multiple traditional machine learning models, creating a multi-block blockchain-inspired audit chain, testing tamper detection, and adding feature importance analysis for model explainability. This version compared Logistic Regression, Random Forest, and Gradient Boosting using the same cleaned UCI Heart Disease dataset and the same train-test split.

### Version 2 Model Comparison Results

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 83.3% | 84.6% | 78.6% | 81.5% | 94.9% |
| Random Forest | 85.0% | 88.0% | 78.6% | 83.0% | 94.1% |
| Gradient Boosting | 76.7% | 76.9% | 71.4% | 74.1% | 88.3% |

Random Forest achieved the highest accuracy and F1 score, while Logistic Regression achieved the highest ROC-AUC.

### Version 2 Audit Chain

Version 2 created a three-block audit chain:

- Block 1: Logistic Regression
- Block 2: Random Forest
- Block 3: Gradient Boosting

Each block records the dataset hash, model version, training date, features used, hyperparameters, performance metrics, previous block hash, and current block hash. This creates a linked model history where each model record is connected to the previous model record.

### Version 2 Tamper Detection

Tamper-detection testing was performed by intentionally modifying audit records and checking whether the recalculated hash still matched the saved hash. The original audit chain was valid, while the tampered versions were detected as invalid.

Tamper tests included:

- Changing a model performance metric
- Changing a model name
- Changing the dataset hash
- Changing a previous block hash

### Version 2 Feature Importance

Feature importance analysis was added using Random Forest and Gradient Boosting. The most important variables included thalassemia-related information, chest pain type, number of major vessels, ST depression, age, cholesterol, and maximum heart rate.

### Version 2 Outputs

- `notebooks/heart_disease_model_comparison_v2.ipynb` - Version 2 notebook for model comparison, audit chain construction, tamper detection, and feature importance analysis.
- `results/model_comparison_v2.csv` - Model comparison results for Logistic Regression, Random Forest, and Gradient Boosting.
- `results/audit_chain_v2.json` - Multi-block blockchain-inspired audit chain.
- `results/tamper_detection_results_v2.json` - Tamper-detection test results.
- `results/feature_importance_v2.csv` - Feature importance results.
- `results/feature_importance_v2.png` - Feature importance chart.

## Version 3: Deep Learning and Reproducible Health AI Governance Extension

Version 3 expanded the project by adding a TensorFlow/Keras neural network model as a deep learning baseline. This version compared the neural network against the Version 2 traditional machine learning models, improved the project structure by adding reusable Python scripts, added reproducibility files, and upgraded the blockchain-inspired audit chain to include a deep learning model block.

The neural network was added to test whether a deep learning approach could improve prediction performance on the same cleaned heart disease dataset. It also allowed the audit trail to record deep learning-specific information, such as model architecture, number of layers, activation functions, optimizer, learning rate, epochs, batch size, and loss function.

### Version 3 Model Comparison Results

| Model | Type | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---|---:|---:|---:|---:|---:|
| Logistic Regression | Traditional ML baseline | 83.3% | 84.6% | 78.6% | 81.5% | 94.9% |
| Random Forest | Tree-based ML | 85.0% | 88.0% | 78.6% | 83.0% | 94.1% |
| Gradient Boosting | Boosted tree model | 76.7% | 76.9% | 71.4% | 74.1% | 88.3% |
| Neural Network / MLP | Deep learning baseline | 85.0% | 88.0% | 78.6% | 83.0% | 94.9% |

The neural network performed competitively with the traditional machine learning models. It matched the Random Forest model in accuracy and precision, produced a similar F1 score, and achieved a ROC-AUC close to Logistic Regression. However, it did not clearly outperform the traditional models. This suggests that deep learning can be added successfully to the workflow, but that traditional machine learning models may remain highly competitive for small structured clinical datasets.

### Version 3 Neural Network Architecture

The Version 3 neural network used a simple multilayer perceptron architecture:

- Input features: 13
- Hidden layer 1: Dense layer with 16 units and ReLU activation
- Hidden layer 2: Dense layer with 8 units and ReLU activation
- Output layer: Dense layer with 1 unit and sigmoid activation
- Optimizer: Adam
- Loss function: Binary cross-entropy
- Batch size: 16
- Epochs planned: 100
- Epochs trained: 27
- Trainable parameters: 369
- Early stopping: Used validation loss with patience of 10

The training history showed signs of possible overfitting. Training accuracy increased to approximately 87.8%, while validation accuracy peaked around 77.1% and later remained closer to 72.9%. This pattern suggests that the model was learning the training data more strongly than the validation data. Early stopping helped reduce the risk of continued overfitting.

### Version 3 Audit Chain

Version 3 expanded the audit chain to four blocks:

- Block 1: Logistic Regression
- Block 2: Random Forest
- Block 3: Gradient Boosting
- Block 4: Neural Network / MLP

The neural network audit block records additional deep learning-specific information, including:

- Architecture
- Number of layers
- Layer types
- Activation functions
- Optimizer
- Learning rate
- Epochs planned
- Epochs trained
- Batch size
- Loss function
- Early stopping settings

This makes the audit trail more complete because it records not only model performance, but also the deep learning configuration used to produce the model.

### Version 3 Reproducibility Improvements

Version 3 improved the project structure by adding reusable Python scripts in the `src/` folder:

- `src/data_processing.py` - Functions for loading the dataset, preparing features and target variables, splitting data, and scaling features.
- `src/model_training.py` - Functions for training traditional machine learning models and building/training the neural network.
- `src/evaluation.py` - Functions for evaluating scikit-learn and TensorFlow/Keras models.
- `src/audit_trail.py` - Functions for hashing files, hashing audit blocks, creating audit blocks, and saving audit chains.
- `src/tamper_detection.py` - Functions for recalculating block hashes and verifying audit chain validity.
- `src/feature_importance.py` - Functions for creating and saving feature importance outputs.

Version 3 also added reproducibility files:

- `requirements.txt` - Lists the main Python packages needed to run the project.
- `.gitignore` - Prevents unnecessary cache, environment, system, and temporary files from being tracked.

### Version 3 Outputs

- `notebooks/heart_disease_deep_learning_v3.ipynb` - Version 3 notebook for adding and evaluating the TensorFlow/Keras neural network.
- `results/model_comparison_v3.csv` - Version 3 model comparison results including the neural network.
- `results/audit_chain_v3.json` - Version 3 audit chain with four model blocks, including the neural network block.
- `src/data_processing.py` - Reusable data processing functions.
- `src/model_training.py` - Reusable model training functions.
- `src/evaluation.py` - Reusable evaluation functions.
- `src/audit_trail.py` - Reusable audit trail functions.
- `src/tamper_detection.py` - Reusable tamper-detection functions.
- `src/feature_importance.py` - Reusable feature importance functions.
- `requirements.txt` - Reproducibility file listing required packages.
- `.gitignore` - File for excluding unnecessary files from version control.
- `paper/blockchain_audit_trail_heart_disease_research_paper_draft.md` - Research-style paper draft describing Versions 1, 2, and 3.

## Deep Learning Interpretation

The neural network was added to evaluate whether a deep learning model could improve heart disease prediction performance compared with traditional machine learning models. It also strengthened the project by showing how deep learning model details can be recorded in a blockchain-inspired audit trail.

The neural network performed competitively, but it did not clearly outperform the traditional models. This is an important result because deep learning is not automatically superior in every biomedical prediction task. For small structured clinical datasets, traditional machine learning models such as Logistic Regression and Random Forest may remain highly competitive and may offer advantages in simplicity, interpretability, and reproducibility.

The neural network also showed signs of possible overfitting. Training accuracy continued to improve while validation performance stopped improving and validation loss increased after the best validation point. This reinforces the need for careful validation, early stopping, and cautious interpretation when applying deep learning to small health datasets.

Interpretability and auditability are especially important in health AI. A health-related model should not only produce predictions; it should also be documented, traceable, and reproducible. This project addresses interpretability through feature importance analysis and addresses auditability through hash-based audit records that track datasets, model versions, hyperparameters, performance metrics, and linked model history.

## Audit Trail Features

Each model run records:

- Dataset name
- Dataset version
- Dataset hash
- Model name
- Model version
- Model type
- Training date
- Features used
- Hyperparameters
- Performance metrics
- Previous block hash
- Current block hash

For the Version 3 neural network model, the audit trail also records:

- Architecture
- Number of layers
- Activation functions
- Optimizer
- Learning rate
- Epochs planned
- Epochs trained
- Batch size
- Loss function
- Early stopping settings

## Tools Used

- Python
- pandas
- NumPy
- scikit-learn
- TensorFlow/Keras
- matplotlib
- hashlib
- JSON
- GitHub
- Google Colab

## Project Status

This project is currently in active development. Version 1 established a baseline logistic regression model and created an initial blockchain-inspired audit record. Version 2 expanded the project by comparing multiple traditional machine learning models, creating a multi-block audit chain, testing tamper detection, and adding feature importance analysis for explainability. Version 3 added a TensorFlow/Keras neural network model, compared it against traditional models, added reusable Python scripts, added reproducibility files, upgraded the audit chain to include a deep learning block, and created a research-style paper draft.

Future versions may include additional datasets, fairness and bias testing, improved neural network regularization, deep learning interpretability methods such as SHAP or LIME, improved tamper-detection reporting, and more complete blockchain or distributed ledger implementation.

## How to Reproduce This Project

1. Clone or download this GitHub repository.
2. Install the required packages listed in `requirements.txt`.
3. Open `notebooks/heart_disease_model_comparison_v2.ipynb` to reproduce the Version 2 traditional machine learning comparison, audit chain, tamper detection, and feature importance analysis.
4. Open `notebooks/heart_disease_deep_learning_v3.ipynb` to reproduce the Version 3 neural network model and deep learning comparison.
5. Run all notebook cells from top to bottom.
6. Review generated outputs in the `results/` folder.

## Repository Structure

- `data/` - Dataset files or notes about the dataset source.
- `notebooks/` - Jupyter notebooks for data exploration, model building, model comparison, audit trail construction, tamper detection, feature importance analysis, and deep learning.
- `src/` - Reusable Python scripts for data processing, model training, evaluation, audit trail logic, tamper detection, and feature importance.
- `results/` - Model performance metrics, audit trail records, tamper-detection results, feature importance tables, and charts.
- `paper/` - Research-style write-up for the project.
- `poster/` - Future one-page research poster.
- `references/` - Notes, articles, and citations related to heart disease prediction, health AI, biomedical informatics, model governance, and blockchain-inspired audit trails.
- `requirements.txt` - Python package requirements for reproducing the project.
- `.gitignore` - Files and folders excluded from version control.

## Disclaimer

This project is for educational and research portfolio purposes only. It is not intended for clinical diagnosis, treatment decisions, or direct medical recommendations. The models have not been clinically validated and should not be used as medical decision-making tools.
