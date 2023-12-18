from flask import Flask
from flask_migrate import Migrate
from hello import db

app = Flask(__name__)

# 配置数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/users'

db.init_app(app)
migrate = Migrate(app, db)