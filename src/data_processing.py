import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_dataset(url):
    """
    Load the cleaned heart disease dataset from a CSV URL.

    Parameters:
        url (str): URL or file path to the CSV dataset.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    df = pd.read_csv(url)
    return df


def prepare_features_and_target(df):
    """
    Separate the dataset into features and target variable.

    This project uses heart_disease_present as the binary target variable.
    The original num column is removed from the feature set.

    Parameters:
        df (pandas.DataFrame): Cleaned heart disease dataset.

    Returns:
        X (pandas.DataFrame): Feature variables.
        y (pandas.Series): Target variable.
    """
    X = df.drop(columns=["num", "heart_disease_present"])
    y = df["heart_disease_present"]
    return X, y


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.

    Stratification is used to preserve the class distribution of the target variable.

    Parameters:
        X (pandas.DataFrame): Feature variables.
        y (pandas.Series): Target variable.
        test_size (float): Proportion of data used for testing.
        random_state (int): Random seed for reproducibility.

    Returns:
        X_train, X_test, y_train, y_test
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


def scale_features(X_train, X_test):
    """
    Scale features for neural network training.

    Scaling is especially important for neural network models because features
    with different ranges can affect model training.

    Parameters:
        X_train (pandas.DataFrame): Training features.
        X_test (pandas.DataFrame): Testing features.

    Returns:
        X_train_scaled: Scaled training features.
        X_test_scaled: Scaled testing features.
        scaler: Fitted StandardScaler object.
    """
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler
