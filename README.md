# 📩 Email Spam Detection using Machine Learning

A machine learning project to classify emails as **Spam** or **Ham (Not Spam)** using **Naive Bayes**, **Natural Language Processing**, and a clean **Streamlit UI** for real-time testing and spam probability prediction.

---


## 🧠 Features

- Classifies any email message as **Spam** or **Ham**
- Shows **Spam Probability** (confidence score)
- Built with **Scikit-learn**, **NLTK**, and **Streamlit**
- Supports batch predictions for multiple messages
- Clean, minimal UI design
- Model trained on real-world spam datasets

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Programming Language |
| Scikit-learn | ML Model (Naive Bayes) |
| NLTK | Text Preprocessing |
| Streamlit | Web UI |
| Joblib | Model Serialization |

---

## 📁 Project Structure

```
email-spam-detector/
├── email_spam_detection_model.pkl
├── vectorizer.pkl
├── app.py
├── requirements.txt
├── README.md
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/email-spam-detector.git
cd email-spam-detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🧪 Example Predictions

```plaintext
📩 Message: Your account has been suspended. Click here to verify.
🔍 Prediction: SPAM
📊 Spam Probability: 0.99

📩 Message: Hey, can we meet tomorrow for the assignment discussion?
🔍 Prediction: HAM
📊 Spam Probability: 0.01
```

---


## 📦 Requirements

```
scikit-learn
streamlit
nltk
joblib
```

---

## ✅ Future Improvements

- Use deep learning models (LSTM, BERT)
- Add user login and message history
- Visualize most common spam words
- Support multiple languages

---

## 🙌 Credits

- [NLTK Dataset](https://www.nltk.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Streamlit](https://streamlit.io/)
- Designed & built by [Your Name](https://github.com/your-username)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
