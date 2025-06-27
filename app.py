import streamlit as st
import joblib
from extract_features import extract_features

# Load trained model
model = joblib.load('model/phishing_model.pkl')

st.set_page_config(page_title="Phishing URL Detector", page_icon="🔐")
st.title("🔐 Phishing URL Detection System")

url = st.text_input("Enter the URL:")

if st.button("Check"):
    features = [extract_features(url)]
    result = model.predict(features)
    if result[0] == 1:
        st.error("⚠️ This is a phishing URL!")
    else:
        st.success("✅ This is a legitimate URL.")
