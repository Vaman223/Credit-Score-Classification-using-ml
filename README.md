# 💸 Credit Score classification

A machine learning-based web app that predicts a user's financial risk score based on various banking and income-related parameters.

## 🚀 Features

- Predicts based on user attributes such as income, credit history, and debt.
- Uses **K-Nearest Neighbors (KNN)** algorithm for prediction.
- Applied **Data Preprocessing**, **Feature Engineering**, and **EDA** to refine model performance.
- Designed for **static datasets** (no live training).

---

## 📊 Input Features

| Feature                    | Description                         |
|---------------------------|-------------------------------------|
| Annual Income             | Yearly earnings (in ₹ or $)         |
| Monthly Salary            | Income received per month           |
| Number of Bank Accounts   | Total accounts user has             |
| Number of Credit Cards    | Total credit cards owned            |
| Interest Rate             | Average loan interest rate (%)      |
| Number of Delayed Payments| Count of past payment delays        |
| Outstanding Debt          | Total unpaid debts                  |
| Credit History            | Duration of credit history (years)  |
| Age                       | User's age                          |
| Monthly Balance           | Remaining balance at month's end    |

---

## 🧠 Model

- Algorithm: **K-Nearest Neighbors (KNN)**
- Data: Static CSV dataset
- Preprocessing: Null removal, outlier handling, normalization
- Feature Engineering: Correlation checks, scaling
- Model trained on preprocessed data, not updated in real-time

---

## 🖼️ Visual Output

- Displays prediction along with user-specific indicators
- Graphs generated with Matplotlib/Seaborn
- API is used (like Spotify or others) to pull relevant visual assets dynamically (no music playback)

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Flask / Streamlit (for UI)
- Matplotlib / Plotly for visualization

---
Create a folder and then put index.html inside and then open app.py in vs code or any other word editor
Run in termninal "Flask run" Voila your web page will be hosted locally.

---
#Preview of page
![image alt](https://github.com/Vaman223/Credit-Score-Classification-using-ml/blob/main/Screenshot%202025-06-29%20163950.png?raw=true)
![image alt](https://github.com/Vaman223/Credit-Score-Classification-using-ml/blob/main/Screenshot%202025-06-29%20163956.png?raw=true)

