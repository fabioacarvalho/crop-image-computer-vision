import cv2
import streamlit as st
from PIL import Image
import numpy as np
from skimage import morphology, io, color, feature, filters

def image_brightness(image, result):
    image_brightness = cv2.convertScaleAbs(image, beta=result)
    return image_brightness

def image_blur(image, result):
    image_blur = cv2.GaussianBlur(image, (7,7), result)
    return image_blur

def image_improve(image):
    image_improvement = cv2.detailEnhance(image, sigma_s=35, sigma_r=0.50)
    return image_improvement

def image_grayscale(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return img_gray

def main():
    st.title("Handle with Images")
    st.subheader("Using OpenCV to handle with images")
    st.caption("Developed by Fábio A. Carvalho - 2025")

    with st.container():
        img_file = st.file_uploader("Select an image", type=["png", "jpg", "jpeg"])
        improvement = st.checkbox("Improve image details")

        st.html("<h3>Settings:</h3>")

        col1, col2 = st.columns([3, 3])

        with col1:
            blur = st.slider("Blur", min_value=0.2, max_value=3.5)
        with col2:
            brightness = st.slider("Brightness", min_value=-50, max_value=50, value=0)
        
        st.html("<h3>Filters:</h3>")

        cola, colb, colc, cold = st.columns([3, 3, 3, 3])
        with cola:
            image_gray = st.checkbox("Convert image to gray")
        with colb:
            image_erosion = st.checkbox("Apply erosion filter")
        with colc:
            image_dilation = st.checkbox("Apply dilation filter")
        with cold:
            image_edge = st.checkbox("Apply edge filter")

        if not img_file:
            return None
        
        original_img = Image.open(img_file)
        original_img = np.array(original_img)

        processed_img = image_brightness(original_img, brightness)
        processed_img = image_blur(processed_img, blur)

        if improvement:
            processed_img = image_improve(processed_img)
        
        if image_gray:
            processed_img = image_grayscale(processed_img)
        
        if image_erosion:
            processed_img = morphology.erosion(processed_img)
        if image_dilation:
            processed_img = morphology.dilation(processed_img)
        if image_edge:
            processed_img = filters.sobel(processed_img)

        col_original, col_processed = st.columns([3, 3])
        with col_original:
            st.text("Original Image")
            st.image(original_img)
        with col_processed:
            st.text("Processed image")
            st.image(processed_img)


if __name__ == '__main__':
    main()