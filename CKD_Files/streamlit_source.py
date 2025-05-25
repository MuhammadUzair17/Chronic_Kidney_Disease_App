import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(page_title="CKD Prediction", layout="centered", page_icon="💻")

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("CKD_Files/ckd.pkl")

model = load_model()

# Sidebar with project information
with st.sidebar:
    st.title("About this Application")
    st.markdown("""
    This application uses a trained machine learning model to estimate the likelihood of Chronic Kidney Disease (CKD).

    **Model Input Features:**
    - Hemoglobin  
    - Specific Gravity  
    - Albumin  
    - Serum Creatinine  
    - Hypertension  
    - Diabetes Mellitus

    **Disclaimer:** This tool is intended for educational purposes only and should not be used as a substitute for professional medical diagnosis.
    """)

# Main Title
st.title("Chronic Kidney Disease (CKD) Prediction")
st.markdown("Please fill in the following medical details to receive a CKD risk prediction.")

# Input form
with st.form("ckd_form"):
    col1, col2 = st.columns(2)

    with col1:
        hemoglobin = st.slider("Hemoglobin (g/dl)", 3.0, 18.0, 13.5, step=0.1)
        specific_gravity = st.selectbox("Specific Gravity", options=[1.005, 1.010, 1.015, 1.020, 1.025])
        albumin = st.slider("Albumin (g/dl)", 0, 5, 1)

    with col2:
        serum_creatinine = st.slider("Serum Creatinine (mg/dl)", 0.1, 15.0, 1.2, step=0.1)
        hypertension = st.radio("Hypertension Diagnosis", ['Yes', 'No'])
        diabetes_mellitus = st.radio("Diabetes Mellitus Diagnosis", ['Yes', 'No'])

    submitted = st.form_submit_button("Predict CKD")

# Prediction
if submitted:
    # Ensure categorical inputs match training format (lowercase)
    hypertension = hypertension.lower()
    diabetes_mellitus = diabetes_mellitus.lower()

    input_data = pd.DataFrame([{
        "hemoglobin": hemoglobin,
        "specific_gravity": specific_gravity,
        "albumin": albumin,
        "serum_creatinine": serum_creatinine,
        "hypertension": hypertension,
        "diabetes_mellitus": diabetes_mellitus
    }])

    try:
        prediction = model.predict(input_data)[0]

        if prediction == "ckd":
            st.error("Prediction: CKD Detected")
            st.markdown("""
            **Recommendations:**
            - Consult a nephrologist for a detailed examination.
            - Follow a kidney-friendly diet.
            - Monitor blood pressure and blood sugar levels.
            - Stay hydrated as per medical advice.
            - Avoid over-the-counter medications without approval.
            """)
        else:
            st.success("Prediction: No CKD Detected")
            st.markdown("""
            **General Health Tips:**
            - Maintain a balanced diet.
            - Drink adequate water throughout the day.
            - Exercise regularly and manage stress.
            - Attend routine health checkups.
            - Avoid smoking and excessive alcohol use.
            """)

    except Exception as e:
        st.error("An error occurred during prediction.")
        st.text(f"Details: {str(e)}")

# Footer
st.markdown("---")
st.caption("Developed for academic use. No personal data is stored or shared.")
