# 🩺 Health Insurance Cost Predictor

An **AI-powered Health Insurance Cost Prediction Web App** built using **Machine Learning** and **Streamlit**.  
The application predicts estimated insurance costs based on demographic, lifestyle, and medical factors, and provides a **clear cost breakdown visualization**.

🔗 **Live App:**  
👉 https://health-insurance-cost-predictor-nzv8hxcqbrusvw9zpw3sbi.streamlit.app/

---

## 📌 Features

- ✅ Accurate insurance cost prediction using trained ML models  
- 🌙 Dark Mode enabled by default  
- 📊 Cost breakdown visualization  
- 🧠 Intelligent medical risk scoring & normalization  
- ⚡ Loading spinner while predicting  
- 🎨 Clean, modern, responsive UI  
- 🧩 Separate models for different age groups  

---

## 🧠 Machine Learning Approach

- Two models are used:
  - **Young Age Model (≤ 25 years)**
  - **Adult Age Model (> 25 years)**
- Models trained using structured healthcare data  
- Feature scaling handled using **pre-trained scalers**  
- Medical history converted into a **normalized risk score**

---

## 📊 Input Parameters

- Age  
- Number of Dependants  
- Income (Lakhs)  
- Genetical Risk  
- Insurance Plan (Bronze / Silver / Gold)  
- Employment Status  
- Gender  
- Marital Status  
- BMI Category  
- Smoking Status  
- Region  
- Medical History  

---

## 🖥️ Tech Stack

- **Frontend:** Streamlit  
- **Backend / ML:** Python, Pandas, Scikit-learn  
- **Model Persistence:** Joblib  
- **Visualization:** Matplotlib  
- **Deployment:** Streamlit Cloud  

---

## 📁 Project Structure

```text
health-insurance-cost-predictor/
│
├── app.py
├── prediction_helper.py
├── artifacts/
│   ├── model_young.joblib
│   ├── model_rest.joblib
│   ├── scaler_young.joblib
│   └── scaler_rest.joblib
│
├── requirements.txt
└── README.md
```
Install dependencies
```bash
pip install -r requirements.txt
```
Run the application
``` bash
streamlit run app.py
```
📈 Cost Breakdown Explanation
```bash
The predicted insurance cost is divided into:
-Base Cost – Core coverage
-Medical Risk – Based on medical history
-Lifestyle Risk – Smoking, BMI, habits
-Plan Premium – Insurance plan selected
```

🚀 Live Deployment

The application is deployed on Streamlit Cloud:

👉 https://health-insurance-cost-predictor-nzv8hxcqbrusvw9zpw3sbi.streamlit.app/

🧑‍💻 Author
```bash
Krishna Gupta

Machine Learning & Data Science Enthusiast
```
⭐ Future Enhancements
```bash
-Explainable AI (SHAP values)
-Prediction confidence intervals
-Database integration
-Mobile-first UI optimization
```
