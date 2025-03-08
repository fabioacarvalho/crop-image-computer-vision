import streamlit as st
from streamlit_cropper import st_cropper


st.title("Image Segmentation")
st.caption("Developed by Fábio A. Carvalho, 2025")

img_file = st.file_uploader("Select an image", type=["png", "jpg"])

st.info("In progress, wait...")