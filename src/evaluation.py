import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score


def evaluate_sklearn_model(model, X_test, y_test, model_name, model_type):
    """Evaluate a scikit-learn binary classification model."""
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    return {
        "Model": model_name,
        "Type": model_type,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1 Score": f1_score(y_test, y_pred),
        "ROC-AUC": roc_auc_score(y_test, y_prob)
    }


def evaluate_keras_model(model, X_test_scaled, y_test, model_name="Neural Network / MLP"):
    """Evaluate a TensorFlow/Keras binary classification model."""
    y_prob = model.predict(X_test_scaled).ravel()
    y_pred = (y_prob >= 0.5).astype(int)

    return {
        "Model": model_name,
        "Type": "Deep learning baseline",
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1 Score": f1_score(y_test, y_pred),
        "ROC-AUC": roc_auc_score(y_test, y_prob)
    }


def create_results_table(results_list):
    """Create a model comparison table from model results."""
    return pd.DataFrame(results_list)
