#!/usr/bin/env python3
"""Minimal training stub to create a scikit-learn Pipeline model.

This script is only a template. Adjust the TARGET column to what you actually want to predict.
It builds a Pipeline that handles preprocessing so you don't need a separate label_encoder.pkl.

Usage:
  python train_stub.py

It will write:
  - ocd_model.pkl  (a sklearn Pipeline that accepts raw columns)
"""
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

CSV_PATH = 'OCD_Patient.csv'
TARGET = 'Anxiety Diagnosis'  # <-- CHANGE if needed (e.g., 'Depression Diagnosis')

def main():
    df = pd.read_csv(CSV_PATH)
    df = df.dropna(subset=[TARGET])
    y = df[TARGET].astype(str)

    X = df.drop(columns=[TARGET])

    # Split columns by type
    cat_cols = [c for c in X.columns if X[c].dtype == 'object']
    num_cols = [c for c in X.columns if c not in cat_cols]

    pre = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
        ('num', 'passthrough', num_cols),
    ])

    pipe = Pipeline([
        ('pre', pre),
        ('clf', RandomForestClassifier(n_estimators=200, random_state=42))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    print(classification_report(y_test, preds))

    joblib.dump(pipe, 'ocd_model.pkl')
    print('Saved trained pipeline to ocd_model.pkl')

if __name__ == '__main__':
    main()
