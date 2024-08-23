# app.py
from flask import Flask, request, redirect, url_for, render_template, flash
from database import create_db, add_record, get_all_records, get_record, update_record, delete_record

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use uma chave secreta para proteger sessões e mensagens flash

def initialize_database():
    create_db()

initialize_database()  # Chame a função de inicialização diretamente

@app.route('/')
def index():
    records = get_all_records()
    return render_template('index.html', records=records)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        imc = weight / (height ** 2)
        add_record(name, height, weight, imc)
        flash('Record added successfully!')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:record_id>', methods=['GET', 'POST'])
def edit(record_id):
    record = get_record(record_id)
    if not record:
        flash('Record not found!')
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name']
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        imc = weight / (height ** 2)
        update_record(record_id, name, height, weight, imc)
        flash('Record updated successfully!')
        return redirect(url_for('index'))

    return render_template('edit.html', record=record)

@app.route('/delete/<int:record_id>')
def delete(record_id):
    delete_record(record_id)
    flash('Record deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
