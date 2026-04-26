# 💰 Insurance Premium Prediction App

A Machine Learning web application that predicts medical insurance costs based on user details such as age, BMI, smoking habits, and region.

---

## 📌 Project Overview

This project uses a trained **Gradient Boosting Machine Learning model** to estimate insurance premiums.
The model has been trained on a standard insurance dataset and deployed using Streamlit for interactive predictions.

---

## 🚀 Features

* 🎯 Instant insurance premium prediction
* 🧠 Machine Learning model (Gradient Boosting Regressor)
* 🎨 Modern and interactive UI using Streamlit
* ⚡ Fast and lightweight application

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Frontend:** Streamlit
* **Libraries:**

  * pandas
  * numpy
  * scikit-learn
  * pickle

---

## 📂 Project Structure

```
Insurance-Premium-App/
│
├── app.py                # Streamlit application
├── model_gb.pkl         # Trained ML model
├── requirements.txt     # Dependencies
├── README.md            # Documentation

```

---

## 📊 Dataset Information

The dataset used for training is **not included in this repository**.

It contains the following features:

* age
* sex
* bmi
* children
* smoker
* region
* charges (target variable)

You can use any standard insurance dataset to retrain the model.

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Insurance-Premium-App.git
cd Insurance-Premium-App
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv myenv
```

---

### 3️⃣ Activate Environment

**Windows**

```bash
myenv\Scripts\activate
```

**Mac/Linux**

```bash
source myenv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📊 Input Parameters

* Age
* Gender
* BMI
* Smoking Status
* Number of Children
* Region

---

## 💡 Output

* Estimated Insurance Premium 💵

---

## 🧠 Model Information

* Algorithm: Gradient Boosting Regressor
* Preprocessing:

  * Encoding categorical variables
  * Feature alignment with training data
* Output transformed using exponential function (`exp`)

---

## 🔮 Future Improvements

* 📊 Add visualizations (charts)
* 🧠 Model explainability (SHAP values)
* 🌐 Deploy on Streamlit Cloud / AWS



## 👨‍💻 Author

Aishwarya Patil




