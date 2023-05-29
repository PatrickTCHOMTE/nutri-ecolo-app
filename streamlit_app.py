import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.experimental_connection('s3', type=FilesConnection)
df = conn.read("nutri-ecolo-app-data/open_food_data_final_cleaned.csv", input_format="csv")

# Display a dataframe as an interactive table
st.dataframe(df, use_container_width=True)

