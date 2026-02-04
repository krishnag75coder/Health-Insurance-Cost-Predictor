import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
from prediction_helper import predict

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    page_icon="🩺",
    layout="wide"
)

# ===================== DARK MODE (DEFAULT ON) =====================
dark_mode = st.toggle("🌙 Dark Mode", value=True)

# ===================== DARK MODE CSS ONLY =====================
if dark_mode:
    st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #c9d1d9;
    }

    .sub-title {
        text-align: center;
        font-size: 18px;
        margin-bottom: 50px;
        color: #c9d1d9;
    }

    .card {
        background: #161b22;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.35);
        width: 95%;
        margin: auto;
    }

    label {
        font-weight: 600;
        color: #c9d1d9;
    }

    /* 🔽 REDUCED & CENTERED BUTTON */
    .stButton > button {
        width: 260px;
        padding: 10px;
        border-radius: 12px;
        font-size: 17px;
        font-weight: 600;
        background: linear-gradient(90deg, #58a6ff, #4facfe);
        color: white;
        border: none;
        margin: 20px auto 0;
        display: block;
    }

    .stButton > button:hover {
        transform: scale(1.03);
    }

    footer {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

# ===================== HEADER =====================
st.markdown(
    "<h1 style='text-align:center;'>🩺 Health Insurance Cost Predictor</h1>",
    unsafe_allow_html=True
)


# ===================== OPTIONS =====================
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure',
        'Diabetes & High blood pressure', 'Thyroid',
        'Heart disease', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# ===================== FORM CARD =====================
st.markdown("<div class='card'>", unsafe_allow_html=True)

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input("👤 Age", 18, 100)
with row1[1]:
    dependants = st.number_input("👨‍👩‍👧 Dependants", 0, 20)
with row1[2]:
    income = st.number_input("💰 Income (Lakhs)", 0, 200)

with row2[0]:
    genetic = st.number_input("🧬 Genetical Risk", 0, 5)
with row2[1]:
    plan = st.selectbox("📜 Insurance Plan", categorical_options['Insurance Plan'])
with row2[2]:
    job = st.selectbox("💼 Employment Status", categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox("⚧ Gender", categorical_options['Gender'])
with row3[1]:
    marital = st.selectbox("💍 Marital Status", categorical_options['Marital Status'])
with row3[2]:
    bmi = st.selectbox("⚖ BMI Category", categorical_options['BMI Category'])

with row4[0]:
    smoking = st.selectbox("🚬 Smoking Status", categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox("🌍 Region", categorical_options['Region'])
with row4[2]:
    history = st.selectbox("🏥 Medical History", categorical_options['Medical History'])

# ===================== INPUT DICT =====================
input_dict = {
    'Age': age,
    'Number of Dependants': dependants,
    'Income in Lakhs': income,
    'Genetical Risk': genetic,
    'Insurance Plan': plan,
    'Employment Status': job,
    'Gender': gender,
    'Marital Status': marital,
    'BMI Category': bmi,
    'Smoking Status': smoking,
    'Region': region,
    'Medical History': history
}

# ===================== PREDICTION =====================
if st.button("🔮 Predict Insurance Cost"):

    with st.spinner("🔍 Calculating insurance cost..."):
        time.sleep(1.2)
        prediction = predict(input_dict)

    st.success(f"💵 Estimated Insurance Cost: ₹ {prediction:,.2f}")

    # ===================== COST BREAKDOWN =====================
    breakdown = {
        "Base Cost": prediction * 0.55,
        "Medical Risk": prediction * 0.20,
        "Lifestyle Risk": prediction * 0.15,
        "Plan Premium": prediction * 0.10
    }

    df_breakdown = pd.DataFrame({
        "Component": breakdown.keys(),
        "Cost": breakdown.values()
    })

    st.subheader("📊 Cost Breakdown")

    fig, ax = plt.subplots(figsize=(3.5, 3.5))
    ax.pie(
        df_breakdown["Cost"],
        labels=df_breakdown["Component"],
        autopct="%1.1f%%",
        startangle=90,
        textprops={'fontsize': 11}
    )
    ax.axis("equal")

    st.pyplot(fig, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)
