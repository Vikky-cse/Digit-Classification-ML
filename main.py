import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import tensorflow as tf

model = load_model('./mnist.h5')

def preprocess_image(image):
    gray = tf.image.rgb_to_grayscale(image)
    resized = tf.image.resize(gray, [28, 28])
    reshaped = tf.reshape(resized, (1, 28, 28, 1))
    normalized = reshaped / 255.0
    return normalized


st.title("MNIST Digit Recognition")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
   
    st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)

   
    image = tf.image.decode_image(uploaded_image.read(), channels=3)
    processed_image = preprocess_image(image)

   
    prediction = model.predict(processed_image)
    digit = np.argmax(prediction)

    st.write("Predicted Digit:", digit)

   
