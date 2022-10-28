from pathlib import Path
from typing import Tuple

import bentoml
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def process_data(path) -> pd.DataFrame:
    df = pd.read_csv(path / "smoke_detection_iot.csv", index_col=0)
    df.columns = (
        df.columns.str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("[", "_", regex=False)
        .str.replace("]", "_", regex=False)
        .str.replace("%", "pct", regex=False)
        .str.replace(".", "_", regex=False)
    )
    df.drop(columns=["utc"], inplace=True)
    return df


def process_features_target(df) -> Tuple[pd.DataFrame, pd.Series]:
    target = "fire_alarm"
    X = df.drop(columns=target)
    y = df[target]

    return X, y


def train(X_train, y_train):
    model = make_pipeline(
        StandardScaler(),
        RandomForestClassifier(n_estimators=25, max_depth=10, random_state=42),
    )
    # Fit model to training data
    model.fit(X_train, y_train)
    return model


def save_model(model):
    bentoml.sklearn.save_model("smoke_detection", model)


def predict(model, X):
    y_pred = model.predict(X)
    return y_pred


def validate_generalize(model, X, X_test, X_val, y, y_test, y_val):
    accuracy_test_score = accuracy_score(y_test, model.predict(X_test))
    accuracy_validation_score = accuracy_score(y_val, model.predict(X_val))
    auc_score = roc_auc_score(y_val, model.predict(X_val))
    print(f"Accuracy test score: {accuracy_test_score:.3f}")
    print(f"Accuracy validation score: {accuracy_validation_score:.3f}")
    print(f"AUC score for validation data: {auc_score:.3f}")

    # cross validate
    cv_result = cross_validate(model, X, y, cv=5)
    scores = cv_result["test_score"]
    print(
        "The mean cross-validation accuracy for cv=5 is: "
        f"{scores.mean():.3f} +/- {scores.std():.3f}"
    )


def main(path):
    df = process_data(path)
    X, y = process_features_target(df)
    # Data split (set test validation data)
    X_train_full, X_test, y_train_full, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_full, y_train_full, test_size=0.25, random_state=42
    )
    # train model
    model = train(X_train, y_train)
    # validate and generalize model
    validate_generalize(model, X, X_test, X_val, y, y_test, y_val)
    # validation predictions
    y_pred_val = list(predict(model, X_val))[:10]
    print(f"First ten model predictions of validation data: {y_pred_val}")
    # save model
    save_model(model)


if __name__ == "__main__":
    data_path = Path("./dataset/")
    main(data_path)
