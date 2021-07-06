import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

######################
# Page Title
######################

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))

st.write("""
# Data visualize App
This app show your csv data on table or graph.
***
""")

st.write("""
# Show your data on Table
""")

uploaded_file = st.file_uploader("Choose an your csv file...", type = 'csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(pd.DataFrame(data))


st.write("""
***
""")

st.write("""
# Show your data on graph
""")
if st.checkbox('Show DataFrame by chart'):
    if uploaded_file is not None:
        chart_df = pd.DataFrame(data)
        st.line_chart(chart_df)
if st.checkbox('Show DataFrame by histgram'):
    if uploaded_file is not None:
        st.altair_chart(data)