import pickle
import pandas as pd
import numpy as np
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="💰",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Gradient Background */
.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/*  Glass Card Effect */
.card {
    background: rgba(255, 255, 255, 0.1);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
    opacity: 0.9;
}

/*  Input Labels */
label {
    font-weight: 500 !important;
}

/*  Button */
.stButton>button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #0072ff, #00c6ff);
}

/*  Result Box */
.result-box {
    background: rgba(0, 255, 150, 0.15);
    border: 1px solid rgba(0,255,150,0.4);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open('model_gb.pkl', 'rb'))

# ---------------- HEADER ----------------
st.markdown('<div class="title">💰 Insurance Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Premium Estimation System</div>', unsafe_allow_html=True)

# ---------------- CARD ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

# ---------------- INPUTS ----------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Age', 1, 100, 25)
    bmi = st.number_input('BMI', 10.0, 100.0, 30.0)
    children = st.number_input('Children', 0, 10, 2)

with col2:
    gender = st.selectbox('Gender', ('male', 'female'))
    smoker = st.selectbox('Smoker', ('yes', 'no'))
    region = st.selectbox('Region', ('southwest', 'southeast', 'northwest', 'northeast'))

# ---------------- ENCODING ----------------
Smoker = 1 if smoker == 'yes' else 0
sex_female = 1 if gender == 'female' else 0
sex_male = 1 if gender == 'male' else 0

region_dict = {'southwest': 0, 'southeast': 1, 'northwest': 2, 'northeast': 3}
Region = region_dict[region]

input_dict = {
    'age': age,
    'bmi': bmi,
    'children': children,
    'sex_male': sex_male,
    'sex_female': sex_female,
    'Smoker': Smoker,
    'Region': Region
}

input_features = pd.DataFrame([input_dict])
input_features = input_features[model.feature_names_in_]

# ---------------- PREDICTION ----------------
if st.button(' Predict Premium'):
    prediction = model.predict(input_features)
    output = round(np.exp(prediction[0]), 2)

    st.markdown(f"""
        <div class="result-box">
            💵 Estimated Cost: ${output}
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)