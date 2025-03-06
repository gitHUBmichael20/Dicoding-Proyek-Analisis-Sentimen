from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Contoh data
data = [
    {"Text": "Aplikasi ini sangat bagus!", "Label": "positif"},
    {"Text": "Saya tidak suka aplikasi ini.", "Label": "negatif"},
    {"Text": "Lumayan, tapi bisa lebih baik.", "Label": "netral"},
]

# Bagi data
texts = [d["Text"] for d in data]
labels = [d["Label"] for d in data]

# Ekstraksi fitur
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Bagi data training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Latih model
model = SVC()
model.fit(X_train, y_train)

# Evaluasi model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Akurasi: {accuracy * 100:.2f}%")