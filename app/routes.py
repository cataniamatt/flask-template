from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import TestForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    title = 'Provision'
    form = TestForm()
    if form.validate_on_submit():
        
        # Capturing form input
        name = form.name.data
        surname = form.surname.data
        gender = form.gender.data
        sport = form.sport.data

        flash(f"Name: {name} {surname}\n Gender: {gender}\n Favourite sport: {sport}", 'success')
        return redirect(url_for('form'))

    return render_template('form.html', title=title, form=form)
