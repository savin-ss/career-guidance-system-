from flask import Flask, render_template, request
import pandas as pd
import sqlite3

app = Flask(__name__)

# Load data from SQLite database
def load_data():
    conn = sqlite3.connect('career_guidance.db')
    data = pd.read_sql_query("SELECT * FROM careers", conn)
    conn.close()
    return data

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        subject = request.form['subject']
        data = load_data()
        recommendations = data[data['subject'].str.lower() == subject.lower()]  # Ensure 'subject' matches your table column name
        return render_template('results.html', recommendations=recommendations)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

