import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image

st.title("Crop Image")

# st.file_uploader("Send an image", type=["png", "jpg"])

img_file = st.sidebar.file_uploader("Send an image", type=["png", "jpg"])
realtime_update = st.sidebar.checkbox("Update realtime", value=True)
box_color = st.sidebar.color_picker("Colors", "#1461B9")
aspect_choice = st.sidebar.radio("Screen", options=["1:1", "16:9", "4:3"])

aspect_dict = {
    "1:1": (1,1),
    "16:9": (16,9),
    "4:3": (4,3),
}
aspect_ratio = aspect_dict[aspect_choice]

if img_file:
    img = Image.open(img_file)

    if not realtime_update:
        st.write("Double click to crop image.")
    
    img_cropped = st_cropper(
        img,
        realtime_update=realtime_update,
        box_color=box_color,
        aspect_ratio=aspect_ratio
    )
    
    st.write("Rresult")
    
    crop = img_cropped.thumbnail((350,350))
    st.image(img_cropped)
