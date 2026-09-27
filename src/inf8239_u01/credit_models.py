from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC


def build_preprocessor(num_cols, cat_cols):
    num_pipe = Pipeline([("imputer", SimpleImputer(strategy="median")),
                          ("scale", StandardScaler())])
    cat_pipe = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                          ("onehot", OneHotEncoder(handle_unknown="ignore"))])
    return ColumnTransformer([("num", num_pipe, num_cols),
                               ("cat", cat_pipe, cat_cols)])


def build_credit_svm(num_cols, cat_cols, C=1.0, gamma="scale", class_weight=None):
    if C <= 0:
        raise ValueError("C debe ser positivo")
    preprocess = build_preprocessor(num_cols, cat_cols)
    return Pipeline([
        ("prep", preprocess),
        ("model", SVC(C=C, gamma=gamma, kernel="rbf",
                       class_weight=class_weight,
                       probability=True, random_state=42))
    ])