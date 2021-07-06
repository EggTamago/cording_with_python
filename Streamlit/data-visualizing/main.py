import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

######################
# Page Title
######################

image = Image.open('photo.jpg')

st.image(image, use_column_width=True)

st.write("""
# Data visualize App
This app show your csv data on table or graph.
***
""")

uploaded_file = st.file_uploader("Choose an your csv file...", type = 'csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(pd.DataFrame(data))