# Email Spam Detector

A simple yet powerful app built with **Streamlit** that helps you detect whether an email is spam or not.  
It uses a **Naive Bayes classifier** trained on sample data and provides both manual input and CSV upload options for batch predictions.

---

## Project Overview
This project is designed to make **spam detection** easy and interactive.  
You can type in an email or upload a CSV file, and the app instantly classifies each entry as **Spam** or **Not Spam**.

- Provides **real-time predictions** for typed emails.  
- Supports **bulk classification** via CSV upload.  
- Displays results clearly with options to **download predictions**.  
- Built for learning, experimenting, and quick spam filtering demonstrations.  

---

## Features
- **Manual Input** – Type or paste an email and get instant classification.  
- **CSV Upload** – Upload a dataset of emails for batch predictions.  
- **Fast Predictions** – Uses a trained **Multinomial Naive Bayes** model.  
- **Download Results** – Export predictions as a CSV file.  
- **Interactive UI** – Clean and simple interface powered by Streamlit.  

---

## Technologies / Tools Used
- **Python** – Core programming language.  
- **Streamlit** – Interactive web app framework.  
- **Pandas** – Data handling and CSV operations.  
- **Scikit-learn** – Machine learning (CountVectorizer + MultinomialNB).  

---

## Setup & Usage

Open your **Terminal (Mac/Linux)** or **Command Prompt/PowerShell (Windows)** and run the following commands:

```bash
# 1. Install required libraries
pip install streamlit pandas scikit-learn

# 2. To Run the Application
streamlit run email_class.py
## Follow these steps to test the AI Image Classifier and Editor:

1. Open the App  
   Launch the application in your web browser.
2. Write an email or upload a csv file
3. Click option of pridiction
4. model will tell you the email is spam or not


