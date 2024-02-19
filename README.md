# Credit Card Fraud Detection System Using HMM

## Overview
The Credit Card Fraud Detection System is a robust application built on the principles of Hidden Markov Models (HMM) to identify potentially fraudulent credit card transactions. Leveraging advanced machine learning techniques, this system aims to enhance security measures in financial transactions by accurately distinguishing between legitimate and fraudulent activities.

## Key Features
- **Hidden Markov Model:** Utilizes a Gaussian Hidden Markov Model for sequential data analysis, enabling the detection of subtle patterns indicative of fraudulent behavior.

- **Balanced Dataset:** Implements undersampling to balance the dataset, ensuring the model is trained on a representative distribution of legitimate and fraudulent transactions.
  
- **Streamlit Web Application:** The user-friendly Streamlit web interface allows users to input transaction features, providing instant predictions on the legitimacy of a transaction.
  
- **Customizable:** Easily adaptable to different datasets and scenarios, with potential for fine-tuning model parameters for optimal performance.

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
- Ensure to customize the dataset filename and path in the `app.py` file.
- Fine-tune the HMM model parameters based on your dataset and specific requirements.

