import streamlit as st
import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta

# ---------------- APP SETTINGS ---------------------------
st.set_page_config(
    page_title="Travel Journal",
    layout="centered",
    menu_items={
        'Get help': "https://www.tbdxxx.com/help",
        'Report a bug': "https://www.tbdxxx.com/bug",
        'About':  "Nothing yet"
        }
    )

def format_date_for_api(date):
    return date.strftime('%Y%m%d') + '0300', date.strftime('%Y%m%d') + '2100'

# ---------------- PAGE TITLE -----------------------------
st.title('«Travel Journal»')
st.image("assets/logo_travel.png", width=250)
st.write("")

tab1, tab2, tab3 = st.tabs(["Done That", "Bucket List", "Water Temperature"])

with tab1:

    # ---------------- TRAVEL MAP ----------------------------
    st.subheader("Travel Map", divider="red")
    st.write("Check out all our travels on a map!")

    travels = {
        'destination': ['Paris', 'Tokyo', 'New York', 'Cape Town', 'Sydney'],
        'date': ['2024-12-01', '2024-12-15', '2024-12-20', '2025-01-10', '2025-01-24'],
        'longitude': [2.3522, 139.6917, -74.0060, 18.4241, 151.2093],
        'latitude': [48.8566, 35.6895, 40.7128, -33.9249, -33.8688]
    }

    # Creating DataFrame
    df_travels = pd.DataFrame(travels)

    # Display travels on map
    st.map(df_travels)

    # Display the DataFrame
    st.write("List of our travels")
    st.dataframe(df_travels)

    # ---------------- UPLOAD/DOWNLOAD TRAVELS ----------------
    st.subheader("Edit Travels", divider="red")
    st.write("To edit your travels, simply download the current travel file, edit the file and upload the file.")

    if st.button("Download Travel File"):
        st.write("This is just a download dummy.")

    if st.button("Upload Travel File"):
        st.write("This is just an upload dummy.")

with tab2:
    st.subheader("Travel Bucket List", divider="red")
    st.write("One day, I will travel to these places.")

with tab3:
    st.subheader("Water Temperature", divider="red")
    st.write("Request water temperature via API from https://www.alplakes.eawag.ch/")

    # User input fields
    lake = st.selectbox('Choose Lake:', ['zurich', 'greifensee', 'stmoritz', 'hallwil', 'aegeri', 'geneva'])
    date = st.date_input('Choose Date:')

    if st.button('Get Temperature'):
        # Construct API parameters
        model = 'delft3d-flow'
        start_time, end_time = format_date_for_api(date)
        depth = 1

        # API request
        api_url = f"https://alplakes-api.eawag.ch/simulations/layer/average_temperature/{model}/{lake}/{start_time}/{end_time}/{depth}"
        response = requests.get(api_url)

        # Show the data or an error message
        if response.status_code == 200:
            data = response.json()
            temperatures = data['variable']['data']
            min_temp = round(min(temperatures), 1)
            max_temp = round(max(temperatures), 1)
            avg_temp = round((min_temp + max_temp)/2, 1)

            st.metric("Estimated Temperature", f"{avg_temp} °C")
            st.write(f"(between {min_temp} and {max_temp} °C.)")
        else:
            st.error("Failed to fetch data from API.")