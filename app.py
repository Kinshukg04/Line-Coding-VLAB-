from flask import Flask, render_template, url_for, request, redirect, flash
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import io


from random import randint


import random


app = Flask(__name__)
app.config['SECRET_KEY'] = "mysuperlaptop007"

def check(question,response):
    if(question==response):
        return "Correct. Well done!", "success"
    else:
        return "Incorrect. Please try again!", "danger"


@app.route('/')
def home():
    #clear_all_selections()
    return render_template('home.html')



@app.route('/unipolar', methods=['GET', 'POST'])
def unipolar():
    question = ""
    for i in range(6):
        question += str(randint(0, 1))

    msg = None
    if request.method=="GET":
        return render_template('unipolar.html', question=question, msg=msg)

    if request.method=="POST":
        g1 = request.form.get('g1', '', type=str)
        g2 = request.form.get('g2', '', type=str)
        g3 = request.form.get('g3', '', type=str)
        g4 = request.form.get('g4', '', type=str)
        g5 = request.form.get('g5', '', type=str)
        g6 = request.form.get('g6', '', type=str)

        response = ""+g1+g2+g3+g4+g5+g6

        msg, type = check(question,response)
        print(msg, type)
        flash(msg, type)
        return redirect(url_for('unipolar'))

    return render_template('unipolar.html', question=question, msg=msg)
@app.route('/ami')
def ami():
    #clear_all_selections()
    return render_template('ami.html')


@app.route('/pseudoternary')
def pseudoternary():
    #clear_all_selections()
    return render_template('pseudoternary.html')

@app.route('/bi_ans')
def bi_ans():
    #clear_all_selections()
    return render_template('bi_ans.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
