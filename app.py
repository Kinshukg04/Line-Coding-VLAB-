from flask import Flask, render_template, url_for, request, redirect
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

import ipywidgets as wg
from IPython.display import display
import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
import random


def check(ans,response):
    if(ans==response):
        print("Correct")
    else:
        print('Incorrect')
def myPlot(y):
    #fig = Figure()
    n = len(y)
    y.append(y[n-1])
    x = [0,1,2,3,4,5,6]
    plt.step(x,y,'r-',where='post')
    plt.ylabel('V')
    plt.xlabel('T')
    plt.ylim([-2,2])
    plt.xlim([0,6])


  #plt.savefig('/static/images/new_plot.png')
  #plt.show()
# c_slide = wg.IntSlider(value=1,min=-1,max=1,step=1)
#wg.interact(myPlot, c=c_slide)

@app.route('/')
def home():
    #clear_all_selections()
    return render_template('home.html')

@app.route('/unipolar')
def unipolar():
    #clear_all_selections()
    arr = [1,0,1,1,0,1]
    inp = arr
    graph = myPlot(inp)
    #pngImage = io.BytesIO()
    #FigureCanvas(graph).print_png(pngImage)

    # Encode PNG image to base64 string
    #pngImageB64String = "data:image/png;base64,"
    #pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return render_template('Unipolar.html'  )

@app.route('/graphs', methods=['GET', 'POST'])
def graphs():
    num = range(0, 1)
    ans = random.sample(num, 6)
    if request.method=="POST":
        g1 = request.form.get('g1', '', type=int)
        g2 = request.form.get('g2', '', type=int)
        g3 = request.form.get('g3', '', type=int)
        g4 = request.form.get('g4', '', type=int)
        g5 = request.form.get('g5', '', type=int)
        g6 = request.form.get('g6', '', type=int)

        print(g1,g2,g3,g4,g5,g6)
    response = []
    response.append(g1)
    response.append(g2)
    response.append(g3)
    response.append(g4)
    response.append(g5)
    response.append(g6)

    check(ans,response)


    return render_template('graphs.html')
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
