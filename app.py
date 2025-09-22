import streamlit as st
import numpy as np
import pickle

st.title('Car Price Prediction')
model=pickle.load(open('model.pkl', 'rb'))

col1, col2=st.columns(2)
with col1:
    year=st.text_input("Year of Purchase")
with col2:
    present_price=st.text_input('Present Price (in lakhs)')

col3, col4=st.columns(2)
with col3:
    kms_driven=st.text_input('KMs Driven (in thousands)')
with col4:
    fuel_type=st.selectbox('Fuel Type', ('Petrol', 'Diesel', 'CNG'))

col5, col6=st.columns(2)
with col5:
    seller_type=st.selectbox('Seller Type', ('Dealer', 'Individual'))
with col6:
    transmission=st.selectbox('Transmission Type', ('Manual', 'Automatic'))

owner=st.selectbox('Number of Previous Owners', ('0', '1'))


if st.button('Predict Price'):
    if year=='' or present_price=='' or kms_driven=='':
        st.error('Please fill all the fields')
    else:
        year=int(year)
        present_price=float(present_price)
        kms_driven=int(kms_driven)

        fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
        seller_map = {'Dealer': 0, 'Individual': 1}
        transmission_map = {'Manual': 0, 'Automatic': 1}
        
        fuel_type = fuel_map[fuel_type]
        seller_type = seller_map[seller_type]
        transmission = transmission_map[transmission]

        owner=int(owner)

        prediction=model.predict([[present_price, kms_driven, owner, year, fuel_type, seller_type, transmission]])
        output=round(prediction[0], 2)
        if output<0:
            st.error("Sorry you cannot sell this car")
        else:
            st.success(f"You can sell the car at {output} lakhs")