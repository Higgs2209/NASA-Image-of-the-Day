import streamlit as st
import pandas
from api import get_image, get_description, get_title
from send_email import SendMail
st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)
get_image()

with col2:
    title = get_title()
    st.title(title)
    st.image("image.jpg")
    st.write("\n")
    description = get_description()
    print(description)
    st.write(description)
    SendMail("image.jpg", description)





