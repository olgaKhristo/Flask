from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cuvmrsqn:yZoe4SqQcbyUqrOVv0RU6KgPhdTZErlw@trumpet.db.elephantsql.com/cuvmrsqn'
db = SQLAlchemy(app)

from application import routes