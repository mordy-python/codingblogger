from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'dkjfdkajhfljkdsahflksdjhlafjkdshfkj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:python@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False

class User(db.Model):
    def __init__(self, name, date_created, email):
        pass

@app.route('/')
def index():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)
