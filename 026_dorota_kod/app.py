from flask import Flask, render_template, redirect, url_for

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)

app.secret_key = ':)'

@app.route('/')
def index():
    text = open('dane/xd.txt', encoding = 'utf-8').read()
    return render_template("index.html", text=text)

# Forms

@app.route('/form_a', methods=["GET", "POST"])
def form_a():

    form = X()
    if form.validate_on_submit():
        
        github = form.github.data
        my_github_state = form.my_github_state.data
        follow_me = form.follow_me.data

        string = '{}\n{}\n{}\n\n'.format(github, my_github_state, follow_me)
        save_data(string)

        return redirect(url_for('form_result'))

    return render_template("form_a.html", form=form)

@app.route('/form_b', methods=["GET", "POST"])
def form_b():

    form = B()
    if form.validate_on_submit():

        name = form.name.data
        python = form.python.data
        level = form.level.data
        checkbox = form.checkbox.data
        string = '{}\n{}\n{}\n{}\n\n'.format(name, python, level, checkbox)
        save_data_b(string)
        
        return redirect(url_for('form_result'))

    return render_template("form_b.html", form=form)

@app.route('/form_result')
def form_result():
    return render_template("form_result.html")


# Helpers

def save_data(string):
    with open('dane/data.txt', "a") as f:
        f.write(string)

def save_data_b(string):
    with open('dane/data_b.txt', "a") as f:
        f.write(string)

# Form

class X(FlaskForm):
    x_options = [
            ('a','a'),
            ('a','b'),
            ('c','c'),
            ('d','d'),
    ]

    github = StringField('Twoj github:', validators=[DataRequired()])
    my_github_state = SelectField('Ogarniam githuba na:', choices=x_options)
    follow_me = BooleanField('Followuj mnie na gitubie :)')

    button = SubmitField('kk')

class B(FlaskForm):
    how_long_python_options = [
        ('week', 'od tygodnia'),
        ('month', 'od miesiąca'),
        ('year', 'od roku'),
        ('what', 'co to Python?'),
    ]

    level_options = [
        ('beginner', 'jestem totalnie na początku (serio)'),
        ('beginner_plus', 'coś tam kumam, ale niewiele'),
        ('intermediate', 'trzaskam projekty'),
        ('master', 'wymiatam!'),
        ('whatever', 'wciąż nie wiem, co to Python?'),
    ]
    name = StringField('Jak masz na imię?', validators=[DataRequired()])
    python = SelectField('Od jak dawna uczysz się Pythona?', choices=how_long_python_options)
    level = SelectField('Na jakim poziomie nauki jesteś?', choices=level_options)
    checkbox = BooleanField('Zaznacz, jeżeli chcesz się razem pouczyć :)')
    button = SubmitField('Jest ok! Wysyłam!')

if __name__=="__main__":
    app.run()
