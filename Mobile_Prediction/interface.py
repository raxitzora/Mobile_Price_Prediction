import streamlit as st
import numpy as np
import joblib  # For loading the saved model

# Load the trained model
model = joblib.load('random_forest_model.pkl')  # Ensure the model file is in the same directory

# Streamlit App
def main():
    # App title
    st.title("Mobile Price Range Prediction")
    st.write("Predict the price range of a mobile phone based on its features.")

    # Sidebar inputs for the model
    st.sidebar.header("Input Features")
    
    battery_power = st.sidebar.slider("Battery Power (mAh)", min_value=500, max_value=2000, step=10)
    blue = st.sidebar.selectbox("Bluetooth Availability", [0, 1], format_func=lambda x: "Yes" if x else "No")
    clock_speed = st.sidebar.slider("Clock Speed (GHz)", min_value=0.5, max_value=3.0, step=0.1)
    dual_sim = st.sidebar.selectbox("Dual SIM Support", [0, 1], format_func=lambda x: "Yes" if x else "No")
    fc = st.sidebar.slider("Front Camera (MP)", min_value=0, max_value=20, step=1)
    four_g = st.sidebar.selectbox("4G Support", [0, 1], format_func=lambda x: "Yes" if x else "No")
    int_memory = st.sidebar.slider("Internal Memory (GB)", min_value=2, max_value=64, step=1)
    m_dep = st.sidebar.slider("Mobile Depth (cm)", min_value=0.1, max_value=1.0, step=0.1)
    mobile_wt = st.sidebar.slider("Mobile Weight (g)", min_value=80, max_value=250, step=5)
    n_cores = st.sidebar.slider("Number of Cores", min_value=1, max_value=8, step=1)
    pc = st.sidebar.slider("Primary Camera (MP)", min_value=0, max_value=20, step=1)
    px_height = st.sidebar.slider("Pixel Height", min_value=0, max_value=2000, step=50)
    px_width = st.sidebar.slider("Pixel Width", min_value=0, max_value=2000, step=50)
    ram = st.sidebar.slider("RAM (MB)", min_value=256, max_value=4096, step=256)
    sc_h = st.sidebar.slider("Screen Height (cm)", min_value=5, max_value=20, step=1)
    sc_w = st.sidebar.slider("Screen Width (cm)", min_value=0, max_value=20, step=1)
    talk_time = st.sidebar.slider("Talk Time (hours)", min_value=2, max_value=20, step=1)
    three_g = st.sidebar.selectbox("3G Support", [0, 1], format_func=lambda x: "Yes" if x else "No")
    touch_screen = st.sidebar.selectbox("Touch Screen", [0, 1], format_func=lambda x: "Yes" if x else "No")
    wifi = st.sidebar.selectbox("Wi-Fi Support", [0, 1], format_func=lambda x: "Yes" if x else "No")

    # Create a numpy array for prediction
    features = np.array([
        battery_power, blue, clock_speed, dual_sim, fc, four_g,
        int_memory, m_dep, mobile_wt, n_cores, pc, px_height,
        px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi
    ]).reshape(1, -1)

    # Prediction
    if st.sidebar.button("Predict"):
        prediction = model.predict(features)[0]
        
        # Map the prediction to a human-readable label
        price_range = {
            0: "Low Cost",
            1: "Medium Cost",
            2: "High Cost",
            3: "Very High Cost"
        }
        st.success(f"The predicted price range is: **{price_range[prediction]}**")

    # About section
    st.sidebar.header("About")
    st.sidebar.info("This app predicts the price range of a mobile phone using a trained Random Forest Classifier.")

if __name__ == '__main__':
    main()
