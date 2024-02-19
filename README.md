# Credit Card Fraud Detection System Using HMM

## Overview
This is a simple Streamlit web application for credit card fraud detection using a Hidden Markov Model (HMM). The app reads a credit card dataset, undersamples legitimate transactions to balance the classes, and trains an HMM on the data. Users can input transaction features, and the app predicts whether the transaction is legitimate or fraudulent.

## Usage
1. Install the required dependencies using:
    ```bash
    pip install -r requirements.txt
    ```
   
2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

3. Enter the features in the provided text input and click "Submit" to get the prediction.

## Files
- `app.py`: Streamlit app code.
- `creditcard.csv`: Credit card dataset (replace with your dataset).

## Requirements
- Python 3.6+
- numpy
- pandas
- scikit-learn
- hmmlearn
- streamlit

## Notes
- Make sure to customize the dataset filename and path in the `app.py` file.
- Fine-tune the HMM model parameters based on your dataset and requirements.
