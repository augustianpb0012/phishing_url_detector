# 🔐 Phishing URL Detector

A machine learning-based web application that detects whether a given URL is **phishing** or **legitimate**. Built using Python, Scikit-learn, and Streamlit, this tool helps demonstrate how basic feature extraction and classification models can be applied in cybersecurity.

---

## 🚀 Features

- 🧠 Predicts if a URL is **phishing** or **safe**
- ⚙️ Uses a trained **Random Forest Classifier**
- 🔍 Extracts features such as:
  - Presence of IP address in URL
  - Use of `@` symbol
  - Length of the URL
  - Use of HTTPS
- 🖥️ Streamlit-powered web interface

---

## 🛠️ Tech Stack

- Python 3
- Scikit-learn
- Pandas
- Joblib
- Streamlit

---


---

## 📦 Installation

1. Clone the repository:
'''bash
git clone https://github.com/yourusername/phishing_url_detector.git
cd phishing_url_detector

2. Create a virtual environment (optional but recommended):
'''bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
'''bash
pip install -r requirements.txt

## How to Use
1. Prepare the Dataset
Make sure urls.csv contains:
*url — the actual URL
*label — 1 for phishing, 0 for legitimate

2. Train the Model
'''bash
python train_model.py

3. Launch the Web App
'''bash
streamlit run app.py

4. Enter a URL in the Streamlit interface to see if it's safe or phishing
           URL	                     Prediction
http://192.168.0.1/login    	    ⚠️ Phishing
https://www.google.com	          ✅ Legitimate
http://login.example.com@scam.io	⚠️ Phishing


Output:

![image](https://github.com/user-attachments/assets/f69abb6b-7004-49bf-b21f-f32324d197d6)
![image](https://github.com/user-attachments/assets/61aa651c-694b-4b10-a158-ea93ac7c5f10)

