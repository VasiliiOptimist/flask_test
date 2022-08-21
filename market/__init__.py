from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '607713711a66ac0fbb888629'
db = SQLAlchemy(app)  # writing 'app' is important

from market import routes