import streamlit as st
import numpy as np
import joblib
import pandas as pd

model = joblib.load('fraud_detection_pipeline.pkl',mmap_mode = None)
st.title('fraud detection preiction app')

st.markdown('please enter thr transaction details and use the predict button')
st.divider()

transaction_type = st.selectbox('transacetion type',('PAYMENT','TRANSFER','CASH_OUT','DEPOSIT'))
amount = st.number_input('Amount',min_value = 0.0,value = 1000.0)
oldbalanceOrg = st.number_input('old balance(sender)',min_value =0.0,value =10000.0)
newbalanceOrig = st.number_input('new balance(sender)',min_value =0.0,value =9000.0)
oldbalanceDest = st.number_input('old balance(receiver)',min_value =0.0,value =0.0)
newbalanceDest = st.number_input('new balance(receiver)',min_value =0.0,value =0.0)

if st.button('Predict'):
    input_data = pd.DataFrame([
        {
            "type":transaction_type,
            "amount":amount,
            "oldbalanceOrg" :oldbalanceOrg,
            "newbalanceOrig":newbalanceOrig,
            "oldbalanceDest":oldbalanceDest,
            "newbalanceDest":newbalanceDest,


        }
    ])
    prediction = model.predict(input_data)
    st.subheader(f'Prediction: {int(prediction[0])}')



    if prediction == 1:
        st.error('this transaction can be fraud')
    else:
        st.success('this transaction does not look like fraud')    
