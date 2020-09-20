import streamlit as st
import pandas as pd
import numpy as np
import time

st.title ('Uber pickups in NYC  🚗🗽')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

rows = st.number_input('Rows to import:',min_value=0,max_value=100000,value=1000,step=1000)


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data



data = load_data(rows)

with st.spinner('Loading data...'):
    time.sleep(0.5)
    
#st.text('Loading data...')
#st.write('Importing ', rows,' rows')

# creating a progress bar 
#bar= st.progress(0)

#for percent_complete in range(100):
    #time.sleep(0.0001)
    #bar.progress(percent_complete + 1)


# Add a placeholder
#latest_iteration = st.empty()
#bar = st.progress(0)
# Create a text element and let the reader know the data is loading.

#with st.spinner('Loading data...'):
     #time.sleep(0.5)
     #st.success('Done!')
     

##for i in range(rows):
  # Update the progress bar with each iteration.
  #latest_iteration.text(f'Iteration {i+1}')
  #bar.progress(i+1)
  #time.sleep(0.001)

# Load data into the dataframe.


# Notify the reader that the data was successfully loaded.

if len(data)>0:
    st.success("Done! (using cache)")

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)



if len(data) > 0 :
    st.subheader('Number of pickups by hour')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

    st.bar_chart(hist_values)

    hour_to_filter = st.slider('Hour:',0,24,10)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
    st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    st.map(filtered_data)


    if st.checkbox('We are done'):
        st.balloons()

# for advanced maps check   st.deckgl_chart.