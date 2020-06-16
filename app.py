from flask import Flask, render_template, url_for, request, redirect, flash
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysuperlaptop007"

unipolar_questions = []
ps_questions=[]
ami_questions = []
unipolar_score = 0
unipolar_total = 0
ami_score = 0
ami_total = 0
pseudo_score = 0
pseudo_total = 0

def check(question,response):
    if(question==response):
        return "Correct. Well done!", "success"
    else:
        return "Incorrect. Better luck next time!", "danger"

def check_AMI(question,response):
    response_int = []
    last_pos = 0
    ans = []
    flag = 0
    for i in range(6):
        if (response[i]=='+'):
            response_int.append(1)
        if(response[i]=='-'):
            response_int.append(-1)
        if(response[i]=='0'):
            response_int.append(0)
        if(question[i]=='0'):
            ans.append(0)
        if(question[i]=='1' and last_pos==0 and flag==0):
            if(response_int[i]!=0):
                ans.append(response_int[i])
                last_pos = response_int[i]
                flag = 1
            else:
                return "Incorrect. Better luck next time!", "danger"
        elif(question[i]=='1' and last_pos==0 and flag==1):
            ans.append(-1)
            last_pos = -1
        elif(question[i]=='1' and last_pos==1):
            ans.append(-1)
            last_pos = -1
        elif(question[i]=='1' and last_pos==-1):
            ans.append(1)
            last_pos = 1
    if(ans==response_int):
        return "Correct. Well done!", "success"
    else:
        return "Incorrect. Better luck next time!", "danger"

def check_psedo(question,response):
    print(question, response)
    response_int = []
    last_pos = 0
    ans = []
    flag = 0
    for i in range(6):
        if (response[i]=='+'):
            response_int.append(1)
        if(response[i]=='-'):
            response_int.append(-1)
        if(response[i]=='0'):
            response_int.append(0)
        if(question[i]=='1'):
            ans.append(0)
        if(question[i]=='0' and last_pos==0 and flag==0):
            if(response_int[i]!=0):
                ans.append(response_int[i])
                last_pos = response_int[i]
                flag = 1
            else:
                return "Incorrect. Better luck next time!", "danger"
        elif(question[i]=='0' and last_pos==0 and flag==1):
            ans.append(-1)
            last_pos = -1
            flag = 1
        elif(question[i]=='0' and last_pos==1):
            ans.append(-1)
            last_pos = -1
        elif(question[i]=='0' and last_pos==-1):
            ans.append(1)
            last_pos = 1
    if(ans==response_int):
        return "Correct. Well done!", "success"
    else:
        return "Incorrect. Better luck next time!", "danger"

def get_uni_score():
    return unipolar_score
def update_uni_score(inc):
    global unipolar_score
    unipolar_score += inc
def get_ami_score():
    return ami_score
def update_ami_score(inc):
    global ami_score
    ami_score += inc
def get_pseudo_score():
    return pseudo_score
def update_pseudo_score(inc):
    global pseudo_score
    pseudo_score += inc

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/unipolar', methods=['GET', 'POST'])
def unipolar():
    global unipolar_total

    if request.method=="GET":
        question = ""
        for i in range(6):
            question += str(randint(0, 1))

        unipolar_questions.append(question)
        return render_template('unipolar.html', question=question, score=get_uni_score(), total=unipolar_total)

    if request.method=="POST":
        g1 = request.form.get('g1', '', type=str)
        g2 = request.form.get('g2', '', type=str)
        g3 = request.form.get('g3', '', type=str)
        g4 = request.form.get('g4', '', type=str)
        g5 = request.form.get('g5', '', type=str)
        g6 = request.form.get('g6', '', type=str)

        response = ""+g1+g2+g3+g4+g5+g6

        msg, type = check(unipolar_questions[-1],response)

        if (type=="success"):
            update_uni_score(1)
        unipolar_total+=1

        flash(msg, type)
        return redirect(url_for('unipolar'))

    return render_template('unipolar.html', question=question, score=get_uni_score(), total=unipolar_total)

@app.route('/ami', methods=['GET', 'POST'])
def ami():
    global ami_total
    if request.method=="GET":
        question = ""
        for i in range(6):
            question += str(randint(0, 1))

        ami_questions.append(question)
        return render_template('ami.html', question=question, score=get_ami_score(), total=ami_total)

    if request.method=="POST":
        g1 = request.form.get('g1', '', type=str)
        g2 = request.form.get('g2', '', type=str)
        g3 = request.form.get('g3', '', type=str)
        g4 = request.form.get('g4', '', type=str)
        g5 = request.form.get('g5', '', type=str)
        g6 = request.form.get('g6', '', type=str)

        response = ""+g1+g2+g3+g4+g5+g6

        msg, type = check_AMI(ami_questions[-1],response)

        if (type=="success"):
            update_ami_score(1)
        ami_total+=1

        flash(msg, type)
        return redirect(url_for('ami'))

    return render_template('ami.html', question=question, score=get_ami_score(), total=ami_total)

@app.route('/pseudoternary', methods=['GET', 'POST'])
def pseudoternary():
    global pseudo_total
    if request.method=="GET":
        question = ""
        for i in range(6):
            question += str(randint(0, 1))

        ps_questions.append(question)
        return render_template('pseudoternary.html', question=question, score=get_pseudo_score(), total=pseudo_total)

    if request.method=="POST":
        g1 = request.form.get('g1', '', type=str)
        g2 = request.form.get('g2', '', type=str)
        g3 = request.form.get('g3', '', type=str)
        g4 = request.form.get('g4', '', type=str)
        g5 = request.form.get('g5', '', type=str)
        g6 = request.form.get('g6', '', type=str)

        response = ""+g1+g2+g3+g4+g5+g6

        msg, type = check_psedo(ps_questions[-1],response)

        if (type=="success"):
            update_pseudo_score(1)
        pseudo_total += 1

        flash(msg, type)
        return redirect(url_for('pseudoternary'))

    return render_template('pseudoternary.html', question=question, score=get_pseudo_score(), total=pseudo_total)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
