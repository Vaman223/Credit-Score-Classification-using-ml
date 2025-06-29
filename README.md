# 💸 Financial Health Predictor

A machine learning-based web app that predicts a user's financial risk score based on various banking and income-related parameters.

## 🚀 Features

- Predicts based on user attributes such as income, credit history, and debt.
- Uses **K-Nearest Neighbors (KNN)** algorithm for prediction.
- Applied **Data Preprocessing**, **Feature Engineering**, and **EDA** to refine model performance.
- Fetches live credit-related visualizations or statistics via APIs (if available).
- Designed for **static datasets** (no live training).
- Album covers or visualizations are dynamically fetched via APIs like Spotify (for illustrative add-ons), but audio playback is restricted as per API limitations.

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

## 📂 Folder Structure

