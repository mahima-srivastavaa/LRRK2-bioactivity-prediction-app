# -*- coding: utf-8 -*-
"""app.ipy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h8NuUlwdILAuNnfGpoTY--RMh6ofT167
"""

import streamlit as st
import tensorflow as tf
import numpy as np
model = tf.keras.models.load_model('densenet.h5')

def preprocess_image(image):
    # Resize the image to the required input shape of the model
    image = image.resize((224, 224))

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Normalize the pixel values to the range of [0, 1]
    image_array = image_array / 255.0

    # Expand the dimensions to match the model's input shape
    image_array = np.expand_dims(image_array, axis=0)

    return image_array

def predict(image_path, model_path):
    # Load the image
    image = Image.open(image_path)

    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Load the DenseNet model
    model = tf.keras.models.load_model(model_path)

    # Perform prediction
    predictions = model.predict(preprocessed_image)

    # Get the predicted class labels
    predicted_labels = np.argmax(predictions, axis=1)

    return predicted_labels

def main():
    st.title("DenseNet Model Deployment")
    st.write("Upload an image and click the 'Predict' button")

    # Create an upload button
    uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform prediction on the uploaded image
        prediction = predict(image)

        # Display the prediction results
        st.write("Prediction Results:")
        # ...

if __name__ == '__main__':
    main()