import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from hmmlearn import hmm
import streamlit as st

# load data
data = pd.read_csv('creditcard.csv')

# separate legitimate and fraudulent transactions
legit = data[data.Class == 0]
fraud = data[data.Class == 1]

# undersample legitimate transactions to balance the classes
legit_sample = legit.sample(n=len(fraud), random_state=2)
data = pd.concat([legit_sample, fraud], axis=0)

# split data into training and testing sets
X = data.drop(columns="Class", axis=1)
y = data["Class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=2)

# train Hidden Markov Model
model = hmm.GaussianHMM(n_components=2, random_state=42)
#model = hmm.GaussianHMM(n_components=2)  # You may need to tune n_components
model.fit(X_train)

# create Streamlit app
st.title("Credit Card Fraud Detection Systum Using HMM")
st.write("Enter the following features to check if the transaction is legitimate or fraudulent:")
st.write("Time, V1,V2,V3...28, Amount")



# create input fields for user to enter feature values
input_df = st.text_input('Input All features')

input_df_lst = input_df.split(',')
# create a button to submit input and get prediction
submit = st.button("Submit")

if submit:
    # get input feature values
    features = np.array(input_df_lst, dtype=np.float64)
    # make prediction
    prediction = model.predict(features.reshape(1,-1))
    # display result
    if prediction[0] == 0:
        st.write("Legitimate transaction")
    else:
        st.write("Fraudulent transaction")
