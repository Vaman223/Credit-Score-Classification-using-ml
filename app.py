from flask import Flask, render_template, request, redirect, flash, url_for
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'

model = joblib.load('model.joblib')

score_map = {
    0: ("Poor", "score-poor", "Your credit score is low. Focus on reducing debt and making timely payments."),
    1: ("Standard", "score-standard", "You're doing okay. Improve your score by paying bills on time and reducing debt."),
    2: ("Good", "score-good", "Excellent score! Keep managing your finances wisely.")
}

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            features = [
             float(request.form['annual_income']),
             float(request.form['monthly_salary']),
             float(request.form['num_bank_accounts']),
             float(request.form['num_credit_cards']),
             float(request.form['interest_rate']),
             float(request.form['num_loans']),
             float(request.form['avg_days_delayed']),
             float(request.form['num_delayed_payments']),
             float(request.form['changed_credit_limit']),
             float(request.form['num_credit_inquiries']),
             float(request.form['outstanding_debt']),
             float(request.form['credit_utilization_ratio']),
             float(request.form['credit_history_age']),
             float(request.form['total_emi']),
             float(request.form['amount_invested']),
             float(request.form['monthly_balance'])
]
            input_array = np.array([features])
            prediction = model.predict(input_array)[0]
            label, score_class, score_description = score_map.get(prediction, ("Unknown", "", "No description available"))
            return render_template('index.html', prediction=label, score_class=score_class, score_description=score_description)
        except Exception as e:
            flash(f"Error during prediction: {str(e)}", "error")
            return redirect(url_for('predict'))
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
