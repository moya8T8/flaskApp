from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__) # flask를 생성하고 app 변수에 flask 초기화 하여 실행

db = SQLAlchemy()
migrate = Migrate()


# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(config)
#
#     #ORM 디비 관련
#     db.init_app(app)
#     migrate.init_app(app, db)
#
#
#     return app

@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'


if __name__ == '__main__':
    app.debug = True
    app.run()