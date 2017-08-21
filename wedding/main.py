#Main file for wedding app

from flask import Flask, render_template, request
from flask sqlalchemy import SQLAlchemy



app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://feng:password123@localhost/wedding' # need to edit
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/wedding'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email 

def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
@app.route('/land')
def land():
    return "Hello, Landing!"
@app.route('/index')
def index():
    return "Hello, World!"


# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def regemail():
    email = None
    if request.method == 'POST':
    	email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return print('success')
    return print ('no post')

if __name__ == "__main__":
	app.run()
