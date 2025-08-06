import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load("email_spam_detection_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit UI
st.set_page_config(page_title="Spam Email Detector", page_icon="📩")
st.title("📩 Spam Email Detector")
st.write("Enter an email message below and click **Predict** to know if it's SPAM or HAM.")

# Text input from user
user_input = st.text_area("✉️ Enter Email Message", height=200)

# Predict button
if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message to predict.")
    else:
        # Transform input & predict
        vectorized_input = vectorizer.transform([user_input])
        prediction = model.predict(vectorized_input)[0]
        prob = model.predict_proba(vectorized_input)[0][1]  # Probability of spam

        if prediction == 1:
            st.error("🔴 **SPAM**")
        else:
            st.success("🟢 **HAM (Not Spam)**")
        
        st.info(f"📊 Spam Probability: **{round(prob, 2)}**")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
