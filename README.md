# MNIST Digit Recognition App

This is a simple web application for recognizing handwritten digits from the MNIST dataset, built using **Streamlit** and **Keras**. It allows users to upload an image and returns the predicted digit based on a pre-trained model.

## 🛠️ Technologies Used
- **Streamlit:** For creating the interactive web interface
- **Keras & TensorFlow:** For loading and using the pre-trained MNIST model
- **NumPy:** For data manipulation and prediction processing
- **Matplotlib:** For displaying the uploaded image (optional)

## 📦 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/mnist-digit-recognition.git
    cd mnist-digit-recognition
    ```

2. Install the required dependencies:
    ```bash
    pip install streamlit numpy keras tensorflow matplotlib
    ```

3. Download or place the pre-trained MNIST model (`mnist.h5`) in the project directory.

## 🚀 Running the App

To run the Streamlit app, use the following command:
```bash
streamlit run app.py
```

## 🔍 How It Works
- The app allows users to upload an image in .jpg, .jpeg, or .png format.
- The image is preprocessed (converted to grayscale, resized to 28x28 pixels, and normalized).
- The preprocessed image is passed to a pre-trained MNIST model for prediction.
- The predicted digit is displayed on the app.

## 🖥️ Deployment
To deploy this app on a cloud platform, you can use:

- Frontend & Backend: Heroku or Streamlit Cloud
- Ensure your model file mnist.h5 is included and your environment variables are correctly set for production.
  
**Happy coding! 🚀**
