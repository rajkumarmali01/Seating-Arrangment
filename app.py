from flask import Flask, render_template, request, redirect, session, url_for, flash
import pandas as pd
from openpyxl import load_workbook
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

EXCEL_FILE = 'seating_data.xlsx'

# Hardcoded admin credentials for 9 buildings
ADMIN_CREDENTIALS = {
    "Building1": "Building1@123",
    "Building2": "Building2@123",
    "Building3": "Building3@123",
    "Building4": "Building4@123",
    "Building5": "Building5@123",
    "Building6": "Building6@123",
    "Building7": "Building7@123",
    "Building8": "Building8@123",
    "Building9": "Building9@123"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in ADMIN_CREDENTIALS and ADMIN_CREDENTIALS[username] == password:
            session['admin'] = username
            return redirect('/dashboard')
        else:
            flash("Invalid credentials")
            return redirect('/')

    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'admin' not in session:
        return redirect('/')

    df = pd.read_excel(EXCEL_FILE)
    building = session['admin']
    building_df = df[df['Building Name'] == building].reset_index(drop=True)

    if request.method == 'POST':
        row_index = int(request.form['row_index'])
        column = request.form['column']
        new_value = request.form['new_value']

        full_df = pd.read_excel(EXCEL_FILE)
        target_indices = full_df[full_df['Building Name'] == building].index

        if row_index < len(target_indices):
            actual_index = target_indices[row_index]
            full_df.at[actual_index, column] = new_value
            full_df.to_excel(EXCEL_FILE, index=False)
            flash('Data updated successfully!')
        return redirect('/dashboard')

    return render_template('dashboard.html', data=building_df.to_dict(orient='records'), columns=building_df.columns)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
