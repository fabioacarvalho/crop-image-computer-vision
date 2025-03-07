import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image
import cv2
from skimage import io, color
from IPython.display import Image
import os

st.title("Face Recognition")
st.caption("Developed by Fábio A. Carvalho, 2025")

# Upload da imagem
img_file = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])

if img_file is not None:
    st.toast("Image loaded with success.", icon=":material/thumb_up:")
    img = io.imread(img_file)
    st.caption(img.shape)


