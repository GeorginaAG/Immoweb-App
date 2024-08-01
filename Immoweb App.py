import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.metrics.pairwise import euclidean_distances

# load the model
model = pickle.load(open('knn_model.sav', 'rb'))

# Title and app definition
st.title('App for House Price Calculation')
st.markdown("This app calculates the price of a property in Belgium")

# add a lateral bar to give the characteristics desired
st.sidebar.header("user choices")

# Capture the data of the user
def user_report():
    # slider controls

    bathroom_count = st.sidebar.slider("Bathroom number", 0, 20, 1)
    bedroom_count = st.sidebar.slider("Bedroom number", 0, 20, 1)
    living_area = st.sidebar.slider("Living Area", 13, 1000, 1)
    number_of_facades = st.sidebar.slider("Number of Facades", 2, 4, 1)
    swimming_pool = st.sidebar.slider("Swimming Pool", 0, 1, 0)
    PEB_grade = st.sidebar.slider("PEB grade", 1, 9, 1)
    Building_state_grade = st.sidebar.slider("Building State", 1, 6, 1)
    kitchen_grade = st.sidebar.slider("Kitchen State", 0, 8, 0)
    price_sqm = st.sidebar.slider('Price per square meter, 100,5000,1')

  
    
    # Dictionary with the user's data
    user_report_data = {
        'bathroom_count': bathroom_count,
        'bedroom_count': bedroom_count,
        'living_area': living_area,
        'number_of_facades': number_of_facades,
        'swimming_pool': swimming_pool,
        'PEB_grade': PEB_grade,
        'Building_state_grade': Building_state_grade,
        'pricesqm': pricesqm,
        'kitchen_grade': kitchen_grade,
        'price_sqm' : price_sqm
    }

    # change the dictionaty to DF
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

# Get the data from the user
user_data = user_report()

st.header('House Data')
st.write(user_data)

# Predict the price
price = model.predict(user_data)

st.subheader('House Price')
st.subheader('Є' + str(np.round(price[0], 2)))

# show the user's data
#st.subheader("User Input Data")
#st.write(user_data)


