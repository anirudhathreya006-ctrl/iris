# Iris Flower Prediction — Streamlit

A simple Streamlit app that predicts the Iris flower species from four measurements.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Files

- `app.py` — Streamlit user interface and prediction
- `train.py` — trains the Random Forest model and saves `iris_model.pkl`
- `iris_model.pkl` — trained model used by the app
- `iris.csv` — Iris dataset in CSV format
- `requirements.txt` — Python dependencies

## Deploy on Streamlit Community Cloud

1. Upload all files in this folder to a GitHub repository.
2. In Streamlit Community Cloud, choose **Create app**.
3. Select your repository, branch, and `app.py` as the main file.
4. Deploy.
