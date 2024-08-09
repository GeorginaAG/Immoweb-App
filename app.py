import streamlit as st
import pandas as pd
import pickle
import numpy as np
        
# load the model
model = pickle.load(open('knn_model.sav', 'rb'))

st.image(r"e:\RSB_pic.jpg")

# Title and app definition
st.title('Estimate the price of a house in Belgium')
st.markdown("This app calculates the price of a property in Belgium in 2024")



#price per square meter per district
Price_Sqm = {'Tournai':1799, 'Brugge':3670, 'Veurne':3349, 'Mechelen':2620, 'Antwerp':2614, 
        'Ieper':2188, 'Mons':1536, 'Philippeville':1549, 'Brussels':3305, 'Soignies':1812, 
        'Charleroi':1507, 'Leuven':2906, 'Liège':1969, 'Aalst':2151, 'Sint-Niklaas':2342, 
        'Verviers':1917, 'Marche-en-Famenne':1816, 'Kortrijk':2204, 'Gent':2909, 'Eeklo':2197, 
        'Hasselt':2197, 'Nivelles':2716, 'Diksmuide':2100, 'Dendermonde':2267, 'Huy':1842, 
        'Tongeren':2142, 'Dinant':1835, 'Neufchâteau':1725, 'Halle-Vilvoorde':2735, 'Tielt':2188, 
        'Roeselare':2063, 'Namur':2136, 'Oostend':2661, 'Oudenaarde':2099, 'Thuin':1540, 
        'Arlon':2375, 'Turnhout':2200, 'Ath':1834, 'Maaseik':2163, 'Virton':1917, 
        'Bastogne':1814, 'Mouscron':1799, 'Waremme':1905}


selected_district = st.selectbox("Choose a District", list(Price_Sqm.keys()))
pricesqm = Price_Sqm[selected_district]


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


