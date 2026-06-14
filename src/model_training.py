import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier


def train_logistic_regression(X_train, y_train):
    """Train a logistic regression model."""
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model


def train_random_forest(X_train, y_train, random_state=42):
    """Train a random forest model."""
    model = RandomForestClassifier(random_state=random_state)
    model.fit(X_train, y_train)
    return model


def train_gradient_boosting(X_train, y_train, random_state=42):
    """Train a gradient boosting model."""
    model = GradientBoostingClassifier(random_state=random_state)
    model.fit(X_train, y_train)
    return model


def build_mlp_model(input_dim):
    """Build a simple neural network / MLP model."""
    tf.keras.utils.set_random_seed(42)

    model = keras.Sequential([
        layers.Input(shape=(input_dim,)),
        layers.Dense(16, activation="relu"),
        layers.Dense(8, activation="relu"),
        layers.Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model


def train_mlp_model(model, X_train_scaled, y_train):
    """Train the neural network model with early stopping."""
    early_stopping = keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=10,
        restore_best_weights=True
    )

    history = model.fit(
        X_train_scaled,
        y_train,
        validation_split=0.2,
        epochs=100,
        batch_size=16,
        callbacks=[early_stopping],
        verbose=1
    )

    return model, history
