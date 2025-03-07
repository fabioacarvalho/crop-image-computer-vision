import streamlit as st
from streamlit_cropper import st_cropper
from pixellib.torchbackend.instance import instanceSegmentation


st.title("Image Segmentation")
st.caption("Developed by Fábio A. Carvalho, 2025")

img_file = st.file_uploader("Select an image", type=["png", "jpg"])

if img_file is not None:

    inst = instanceSegmentation()
    inst.load_model("model/pointrend_resnet50.pkl")
    out = inst.segmentImage(
        img_file,
        show_bboxes=True,
        output_image_name="img/image1_seg.jpg"
    )

    st.image(out)
    st.toast("Imagem carregada com sucesso!", icon=":material/thumb_up:")
