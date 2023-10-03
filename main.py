import streamlit as st
import pandas
from api import get_image, get_description

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)
get_image()

with col2:
    st.image("image.jpg")
    st.write("\n")
    description = get_description()
    print(description)
    st.write(description)






