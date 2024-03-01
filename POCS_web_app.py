# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:59:14 2024

@author: HP
"""

import numpy as np
import streamlit as st
import joblib
from PIL import Image



# Loading the saved model
loaded_model = joblib.load(open('POCS.sav', 'rb'))

# Creating a function for Prediction
def pcos_prediction(input_data):
    # Changing the input_data to a numpy array and converting to float
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)
    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    # Output the prediction
    if prediction[0] == 0:
        return 'The patient is not infected with PCOS'
    else:
        return 'The patient is infected with PCOS'
    

def main():
    st.title('PCOS Prediction Web App')
    image = Image.open('pocs image.png')
    st.image(image)

    # Text inputs to get user inputs
    age = st.text_input('Enter Age in years:')
    bmi = st.text_input('Enter BMI Value:')
    bloodgroup = st.text_input('Enter Blood Group Value:')
    pulserate = st.text_input('Enter Pulse rate in bpm:')
    hb = st.text_input('Enter Hb in g/dl:')
    cycle = st.text_input('Enter Cycle in R/I:')
    cyclelength = st.text_input('Enter Cycle length in days:')
    pregnant = st.text_input('Enter Pregnant value (0 or 1):')
    ibetahcg = st.text_input('Enter I Beta-HCG value:')
    fshlh = st.text_input('Enter FSH/LH value:')
    tsh = st.text_input('Enter TSH value:')
    amh = st.text_input('Enter AMH value:')
    weightgain = st.text_input('Enter Weight gain value (0 or 1):')
    hairloss = st.text_input('Enter Hair loss value (0 or 1):')
    regexercise = st.text_input('Enter Regular Exercise value (0 or 1):')
    follicleleft = st.text_input('Enter Follicle Left value:')
    follicleright = st.text_input('Enter Follicle Right value:')
    endometrium = st.text_input('Enter Endometrium value in mm:')
    iibetahcg = st.text_input('Enter II Beta-HCG value:')
    

    diagnosis = ''
    
    # Creating a button for prediction
    if st.button('PCOS Test Result'):
       diagnosis = pcos_prediction([age, bmi, bloodgroup, pulserate, hb, cycle, cyclelength, pregnant, ibetahcg, fshlh, tsh, amh, weightgain, hairloss, regexercise, follicleleft, follicleright, endometrium, iibetahcg])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()
