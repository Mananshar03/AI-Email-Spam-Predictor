import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# -------------------------------
# Train model (runs once)
# -------------------------------
@st.cache_resource
def train_model():
    data = {
        "text": [
            "Win money now",
            "Free prize claim now",
            "Limited offer click here",
            "Congratulations you won lottery",
            "Hello friend how are you",
            "Let's meet tomorrow",
            "Project meeting schedule",
            "Lunch at 2pm"
        ],
        "label": [1, 1, 1, 1, 0, 0, 0, 0]  # 1 = Spam, 0 = Not Spam
    }

    df = pd.DataFrame(data)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df["text"])
    y = df["label"]

    model = MultinomialNB()
    model.fit(X, y)

    return model, vectorizer


model, vectorizer = train_model()

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("📧 Email Spam Detector")

option = st.radio("Choose input method:", ["Type Email", "Upload CSV"])

# -------------------------------
# Option 1: Manual Input
# -------------------------------
if option == "Type Email":
    user_input = st.text_area("Enter your email text:")

    if st.button("Predict"):
        if user_input.strip() != "":
            transformed = vectorizer.transform([user_input])
            prediction = model.predict(transformed)[0]

            if prediction == 1:
                st.error("🚫 Spam Email")
            else:
                st.success("✅ Not Spam")
        else:
            st.warning("Please enter some text")

# -------------------------------
# Option 2: CSV Upload
# -------------------------------
else:
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("### Uploaded Data")
        st.write(df.head())

        if "text" not in df.columns:
            st.error("CSV must contain a 'text' column")
        else:
            if st.button("Predict CSV"):
                transformed = vectorizer.transform(df["text"])
                predictions = model.predict(transformed)

                df["Prediction"] = ["Spam" if p == 1 else "Not Spam" for p in predictions]

                st.write("### Results")
                st.write(df)

                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("Download Results", csv, "results.csv", "text/csv")