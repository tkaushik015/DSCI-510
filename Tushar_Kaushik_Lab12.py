#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd

# Load data
@st.cache
def load_data():
    data = pd.read_csv('car_data.csv')
    return data

df = load_data()

# Sidebar filters
st.sidebar.header('Filters')
car_name = st.sidebar.text_input('Car Name')
transmission = st.sidebar.multiselect('Transmission', options=['Manual', 'Automatic'], default=['Manual', 'Automatic'])
selling_price_range = st.sidebar.slider('Selling Price Range', 0, 20, (0, 20))
year_range = st.sidebar.slider('Year Range', 2000, 2024, (2000, 2024))

if st.sidebar.button('Submit'):
    filtered_data = df

    if car_name:
        filtered_data = filtered_data[filtered_data['car_name'].str.contains(car_name, case=False)]

    if transmission:
        filtered_data = filtered_data[filtered_data['transmission'].isin(transmission)]

    filtered_data = filtered_data[(filtered_data['selling_price'] >= selling_price_range[0]) & 
                                  (filtered_data['selling_price'] <= selling_price_range[1])]

    filtered_data = filtered_data[(filtered_data['year'] >= year_range[0]) & 
                                  (filtered_data['year'] <= year_range[1])]

    st.write(filtered_data)
else:
    st.write(df)


# In[ ]:


`

