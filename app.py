from flask import Flask, render_template, url_for, request, redirect, flash
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from random import randint


app = Flask(__name__)
app.config['SECRET_KEY'] = "mysuperlaptop007"

unipolar_questions = []
ps_questions=[]
ami_questions = []

def check(question,response):
    if(question==response):
        return "Correct. Well done!", "success"
    else:
        return "Incorrect. Please try again!", "danger"

def check_AMI(question,response):
    response_int = []
    last_pos = 0
    ans = []
    for i in range(6):
        if (response[i]=='+'):
            response_int.append(1)
        if(response[i]=='-'):
            response_int.append(-1)
        if(response[i]=='0'):
            response_int.append(0)
        if(question[i]=='0'):
            ans.append(0)
        if(question[i]=='1' and last_pos==0):
            ans.append(response_int[i])
            last_pos = response_int[i]
        elif(question[i]=='1' and last_pos==1):
            ans.append(-1)
            last_pos = -1
        elif(question[i]=='1' and last_pos==-1):
            ans.append(1)
            last_pos = 1
    if(ans==response_int):
        return "Correct. Well done!", "success"
    else:
        return "Incorrect. Please try again!", "danger"

def check_psedo(question,response):
    print(question, response)
    response_int = []
    last_pos = 0
    ans = []
    for i in range(6):
        if (response[i]=='+'):
            response_int.append(1)
        if(response[i]=='-'):
            response_int.append(-1)
        if(response[i]=='0'):
            response_int.append(0)
        if(question[i]=='1'):
            ans.append(0)
        if(question[i]=='0' and last_pos==0):
            ans.append(response_int[i])
            last_pos = response_int[i]
        elif(question[i]=='0' and last_pos==1):
            ans.append(-1)
            last_pos = -1
        elif(question[i]=='0' and last_pos==-1):
            ans.append(1)
            last_pos = 1
    if(ans==response_int):
        return "Correct. Well done!", "success"
    else:
        return "Incorrect. Please try again!", "danger"


@app.route('/')
def home():
    #clear_all_selections()
    return render_template('home.html')



@app.route('/unipolar', methods=['GET', 'POST'])
def unipolar():
    if request.method=="GET":
        question = ""
        for i in range(6):
            question += str(randint(0, 1))

        unipolar_questions.append(question)
        return render_template('unipolar.html', question=question)

    if request.method=="POST":
        g1 = request.form.get('g1', '', type=str)
        g2 = request.form.get('g2', '', type=str)
        g3 = request.form.get('g3', '', type=str)
        g4 = request.form.get('g4', '', type=str)
        g5 = request.form.get('g5', '', type=str)
        g6 = request.form.get('g6', '', type=str)

        response = ""+g1+g2+g3+g4+g5+g6

        msg, type = check(unipolar_questions[-1],response)

        flash(msg, type)
        return redirect(url_for('unipolar'))

    return render_template('unipolar.html', question=question)

@app.route('/ami', methods=['GET', 'POST'])
def ami():
    if request.method=="GET":
        question = ""
        for i in range(6):
            question += str(randint(0, 1))

        ami_questions.append(question)
        return render_template('ami.html', question=question)

    if request.method=="POST":
        g1 = request.form.get('g1', '', type=str)
        g2 = request.form.get('g2', '', type=str)
        g3 = request.form.get('g3', '', type=str)
        g4 = request.form.get('g4', '', type=str)
        g5 = request.form.get('g5', '', type=str)
        g6 = request.form.get('g6', '', type=str)

        response = ""+g1+g2+g3+g4+g5+g6

        msg, type = check_AMI(ami_questions[-1],response)

        flash(msg, type)
        return redirect(url_for('ami'))

    return render_template('ami.html', question=question)

@app.route('/pseudoternary', methods=['GET', 'POST'])
def pseudoternary():
    if request.method=="GET":
        question = ""
        for i in range(6):
            question += str(randint(0, 1))

        ps_questions.append(question)
        return render_template('pseudoternary.html', question=question)

    if request.method=="POST":
        g1 = request.form.get('g1', '', type=str)
        g2 = request.form.get('g2', '', type=str)
        g3 = request.form.get('g3', '', type=str)
        g4 = request.form.get('g4', '', type=str)
        g5 = request.form.get('g5', '', type=str)
        g6 = request.form.get('g6', '', type=str)

        response = ""+g1+g2+g3+g4+g5+g6

        msg, type = check_psedo(ps_questions[-1],response)

        flash(msg, type)
        return redirect(url_for('pseudoternary'))

    return render_template('pseudoternary.html', question=question)
    #clear_all_selections()
    #return render_template('pseudoternary.html')

@app.route('/bi_ans')
def bi_ans():
    #clear_all_selections()
    return render_template('bi_ans.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
