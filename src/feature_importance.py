import pandas as pd
import matplotlib.pyplot as plt


def create_feature_importance_table(random_forest_model, gradient_boosting_model, feature_names):
    """Create a feature importance table using Random Forest and Gradient Boosting."""
    feature_importance = pd.DataFrame({
        "Feature": feature_names,
        "Random Forest Importance": random_forest_model.feature_importances_,
        "Gradient Boosting Importance": gradient_boosting_model.feature_importances_
    })

    feature_importance["Average Importance"] = (
        feature_importance["Random Forest Importance"] +
        feature_importance["Gradient Boosting Importance"]
    ) / 2

    feature_importance = feature_importance.sort_values(
        by="Average Importance",
        ascending=False
    )

    return feature_importance


def save_feature_importance_plot(feature_importance, output_path):
    """Save a feature importance bar chart."""
    top_features = feature_importance.head(10)

    plt.figure(figsize=(10, 6))
    plt.barh(top_features["Feature"], top_features["Average Importance"])
    plt.xlabel("Average Feature Importance")
    plt.ylabel("Feature")
    plt.title("Top Feature Importance for Heart Disease Prediction")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
