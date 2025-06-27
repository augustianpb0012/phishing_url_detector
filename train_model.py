import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from extract_features import extract_features

# Load dataset (replace with your actual dataset)
data = pd.read_csv("urls.csv")  # Columns: "url", "label" (0=legit, 1=phishing)

# Feature extraction
data['has_ip'] = data['url'].apply(lambda x: extract_features(x)[0])
data['has_at'] = data['url'].apply(lambda x: extract_features(x)[1])
data['url_len'] = data['url'].apply(lambda x: extract_features(x)[2])
data['has_https'] = data['url'].apply(lambda x: extract_features(x)[3])

X = data[['has_ip', 'has_at', 'url_len', 'has_https']]
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'model/phishing_model.pkl')

print("✅ Model trained and saved.")
