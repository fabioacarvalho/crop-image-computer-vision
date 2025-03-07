import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image

st.title("Crop Image")
st.caption("Developed by Fábio A. Carvalho, 2025")

img_file = st.file_uploader("Select an image", type=["png", "jpg"])



with st.container():
    col1, col2, col3 = st.columns([3, 3, 3])

    with col1:
        realtime_update = st.checkbox("Update realtime", value=True)
    with col2:
        box_color = st.color_picker(label="Color box", value="#1461B9")
    with col3:
        aspect_choice = st.radio("Screen", options=["1:1", "16:9", "4:3"])

# On sidebar
# img_file = st.sidebar.file_uploader("Select an image", type=["png", "jpg"])
# realtime_update = st.sidebar.checkbox("Update realtime", value=True)
# box_color = st.sidebar.color_picker("Colors", "#1461B9")
# aspect_choice = st.sidebar.radio("Screen", options=["1:1", "16:9", "4:3"])

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
    st.toast("Imagem carregada com sucesso!", icon=":material/thumb_up:")

