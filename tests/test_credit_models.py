import pytest
import pandas as pd
from inf8239_u01.credit_models import build_credit_svm

def _sample_data():
    df = pd.read_csv("data/raw/dataset.csv")
    X = df.drop(columns=["class"])
    y = df["class"]
    num_cols = X.select_dtypes(include="number").columns.tolist()
    cat_cols = X.select_dtypes(exclude="number").columns.tolist()
    return X, y, num_cols, cat_cols

def test_svm_returns_one_prediction_per_row():
    X, y, num_cols, cat_cols = _sample_data()
    model = build_credit_svm(num_cols, cat_cols)
    model.fit(X[:800], y[:800])
    assert len(model.predict(X[800:])) == len(X[800:])

def test_svm_rejects_non_positive_c():
    X, y, num_cols, cat_cols = _sample_data()
    with pytest.raises(ValueError):
        build_credit_svm(num_cols, cat_cols, C=0)

def test_pipeline_contains_prep_and_model():
    X, y, num_cols, cat_cols = _sample_data()
    pipeline = build_credit_svm(num_cols, cat_cols)
    assert list(pipeline.named_steps) == ["prep", "model"]