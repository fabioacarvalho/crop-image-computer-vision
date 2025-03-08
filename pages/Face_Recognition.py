import face_recognition
import PIL.Image
import PIL.ImageDraw
import numpy as np
import streamlit as st
import io  # Adicionado para manipular a imagem corretamente

st.title("Face Recognition")
st.caption("Developed by Fábio A. Carvalho, 2025")

def image_process(img_file):
    # Abrir a imagem e exibi-la
    img_open = PIL.Image.open(img_file).convert("RGB")

    # Converter a imagem para um formato que face_recognition aceite
    img_bytes = io.BytesIO()
    img_open.save(img_bytes, format="JPEG")  # Salva como um buffer de bytes
    img_bytes.seek(0)  # Retorna ao início do buffer

    # Carregar a imagem no face_recognition
    img = face_recognition.load_image_file(img_bytes)

    # Detectar rostos
    found_faces = face_recognition.face_locations(img)

    # Desenhar os bounding boxes
    image_array = PIL.Image.fromarray(img)
    draw = PIL.ImageDraw.Draw(image_array)

    for face in found_faces:
        top, right, bottom, left = face  # Corrigido a ordem dos valores
        draw.rectangle([left, top, right, bottom], outline="green", width=5)
    
    return image_array

def main():
    img_file = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])

    if img_file:
        result = image_process(img_file)
        # Exibir imagem com bounding boxes
        st.image(result, caption="Detected Faces", width=500)

if __name__ == "__main__":
    main()