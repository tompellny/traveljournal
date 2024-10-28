import streamlit as st
import pandas as pd
import numpy as np

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

# ---------------- PAGE TITLE -----------------------------
st.title('«Travel Journal»')
st.image("assets/logo_travel.png", width=250)
st.write("")

tab1, tab2 = st.tabs(["Done That", "Bucket List"])

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
