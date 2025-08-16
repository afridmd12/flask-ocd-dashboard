# OCD Analytics (Upgraded)

A small Flask app to explore an OCD patient dataset, generate visual dashboards, and demo a (non-diagnostic) predictor.

## What's new
- Safer uploads, better error handling.
- Auto EDA: summary table, missingness, multiple plots (gender, age, ethnicity, obsession/compulsion types, Y-BOCS, duration, yearly trend, correlations).
- Cleaned CSV download.
- `/predict` page (demo): shows a Y-BOCS-based severity proxy if model isn't loaded.
- JSON API: `/api/summary/<filename>` returns dataset summary.
- `requirements.txt` added.
- Optional `train_stub.py` to train an example sklearn Pipeline model and save `ocd_model.pkl`.

## How to run
```bash
pip install -r requirements.txt
python app.py
# visit http://localhost:2001
```

## Using the predictor
- If `ocd_model.pkl` is a scikit-learn Pipeline that accepts raw columns, the app will use it directly.
- If your model relies on separate encoders, put them into `label_encoder.pkl` as a dict `{column_name: fitted_encoder}`.
- If no model loads, the predictor falls back to a simple Y-BOCS severity proxy (for education only).

## Training a quick demo model
```
python train_stub.py
```
This writes `ocd_model.pkl`. By default, it trains a classifier for **Anxiety Diagnosis** from the features in `OCD_Patient.csv`. Change the `TARGET` variable in `train_stub.py` to fit your goal.

## Disclaimer
This project is for education and exploration only. It is **not** a medical device and does **not** provide medical diagnosis. Always consult a licensed professional for clinical decisions.
