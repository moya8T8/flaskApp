from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash # 비밀번호 해시화

# models.py는 데이터베이스 생성하고 데이터 관리 및 추가

db = SQLAlchemy() #데이터 베이스 저장

class User(db.Model) :
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), unique=True, nullable=False)
    userid = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

 # `   def check_password(self, password):
 #        return check_password_hash(self.password, password)`