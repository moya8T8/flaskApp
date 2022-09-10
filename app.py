import os #디렉토리 절대 경로
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import User

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/resgister', methods=['GET', 'POST'])
def resigter():
    if request.method == 'GET':
        return render_template('register.html') #경로 난리치지마  진짜 가만안둔다
    else:
        userid = request.form.get('userid')
        print(userid)

    return redirect('/')



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)