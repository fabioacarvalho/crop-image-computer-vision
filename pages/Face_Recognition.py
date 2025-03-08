import streamlit as st
from streamlit_cropper import st_cropper

st.title("Face Recognition")
st.caption("Developed by Fábio A. Carvalho, 2025")

# Upload da imagem
img_file = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])
