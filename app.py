from flask import Flask, render_template, url_for, request, redirect
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
from random import randint
import ipywidgets as wg
from IPython.display import display
import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
import random


def check(question,response):
    if(question==response):
        return "success"
    else:
        return "danger"


@app.route('/')
def home():
    #clear_all_selections()
    return render_template('home.html')



@app.route('/unipolar', methods=['GET', 'POST'])
def graphs():
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

        msg = check(question,response)

        return render_template('unipolar.html', question=question, msg=msg)

    return render_template('unipolar.html', question=question, msg=msg)
@app.route('/bipolar')
def bipolar():
    #clear_all_selections()
    return render_template('Bipolar.html')


@app.route('/uni_ans')
def uni_ans():
    #clear_all_selections()
    return render_template('uni_ans.html')

@app.route('/bi_ans')
def bi_ans():
    #clear_all_selections()
    return render_template('bi_ans.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
