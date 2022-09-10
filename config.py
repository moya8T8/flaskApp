#db연결 부분
import os

BASE_DIR = os.path.dirname(__file__)

#데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

#SQLAlchemy의 이벤트처리 옵션 -> 지금 현재 사용하지 않음 비활성화
SQLALCHEMY_TRACK_MODIFICATIONS = False

