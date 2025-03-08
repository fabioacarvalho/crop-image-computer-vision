import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

st.title("Face Detection")
st.caption("Developed by Fábio A. Carvalho, 2025")

def detect_face(image):
    # Caminho absoluto do classificador
    face_param = os.path.join(os.getcwd(), "models", "haarcascade_frontalface_alt.xml")
    classificador_cascade = cv2.CascadeClassifier(face_param)

    # Verificar se o classificador carregou corretamente
    if classificador_cascade.empty():
        st.error("Erro ao carregar o classificador Haarcascade. Verifique o caminho do arquivo.")
        return image

    # Converter RGB para BGR (porque OpenCV usa BGR)
    img_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Converter para escala de cinza
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Detectar faces
    faces = classificador_cascade.detectMultiScale(img_gray, scaleFactor=1.2, minNeighbors=10)

    # Se encontrou rostos, desenhar os bounding boxes
    if len(faces) > 0:
        for (x, y, width, height) in faces:
            cv2.rectangle(img_bgr, (x, y), (x + width, y + height), (0, 255, 0), 3)

    # Converter de volta para RGB para exibição no Streamlit
    img_result = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    
    return img_result

def main():
    img_file = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])
    st.info("In progress, for while, use Face Recognition.")

    if img_file:
        process_image = st.checkbox("Detect faces")

        if process_image:
            # Abrir imagem e converter para array editável
            img = Image.open(img_file).convert("RGB")
            img_array = np.array(img, dtype=np.uint8).copy()  # Garante que a imagem seja editável

            result = detect_face(img_array)

            if result is not None:
                st.image(result, caption="Detected Faces")

if __name__ == "__main__":
    main()