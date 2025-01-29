 
Mobile Price Range Prediction

This repository contains a Streamlit web application that predicts the price range of a mobile phone based on its features using a trained Random Forest Classifier.

Features

Predicts mobile price range as Low Cost, Medium Cost, High Cost, or Very High Cost.

User-friendly interface built with Streamlit.

Allows users to input mobile phone specifications through sliders and dropdowns.

Uses a trained Random Forest model (random_forest_model.pkl) for prediction.

Installation

To run this application locally, follow these steps:

Prerequisites

Ensure you have Python installed (preferably 3.7+). You also need to install the required dependencies:

pip install streamlit numpy joblib

Running the App

After installing the dependencies, navigate to the project directory and run:

streamlit run app.py
If that don't work --> python -m streamlit run interface.py

Replace app.py with the actual filename if different.

Input Features

The app takes the following input features:

Battery Power (mAh)

Bluetooth Availability

Clock Speed (GHz)

Dual SIM Support

Front Camera (MP)

4G Support

Internal Memory (GB)

Mobile Depth (cm)

Mobile Weight (g)

Number of Cores

Primary Camera (MP)

Pixel Height & Width

RAM (MB)

Screen Height & Width (cm)

Talk Time (hours)

3G Support

Touch Screen

Wi-Fi Support

Model Information

The prediction model is a Random Forest Classifier.

The trained model is stored as random_forest_model.pkl.

Screenshots

Add screenshots of your app here.

License

This project is open-source and available under the MIT License.

Author

m@dh@v@rt

