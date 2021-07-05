import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('My 1st App! ppppp')

st.write('DataFrame')
st.write(
    pd.DataFrame({
        '1st column': [1, 2, 3, 4],
        '2st column': [10, 22, 33, 45]
    })
)

"""
# My first app.
## This is magic command
Markdown対応
"""

if st.checkbox('Show DataFrame'):
    chart_df = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )

    st.line_chart(chart_df)

st.title('顔認識アプリ')

uploaded_file = st.file_uploader("Choose an image...", type = 'jpg')
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)