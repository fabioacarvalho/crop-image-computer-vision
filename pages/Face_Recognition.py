import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image
import face_recognition
import PIL.Image
import PIL.ImageDraw

st.title("Face Recognition")
st.caption("Developed by Fábio A. Carvalho, 2025")

# Upload da imagem
img_file = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])

if img_file is not None:
    img = face_recognition.load_image_file(img_file)
    faces_found = face_recognition.face_locations(img)

    image_array = PIL.Image.fromarray(img)
    for face in faces_found:
        top, left, bottom, right = face
        draw = PIL.ImageDraw.Draw(image_array)
        draw.rectangle([left, top, right, bottom], outline="green", width=10)

    st.image(image_array)
    st.toast("Imagem carregada com sucesso!", icon=":material/thumb_up:")
