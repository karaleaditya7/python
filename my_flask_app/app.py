from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/adityadb'
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno  = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120), nullable=False)
    Phone_Num = db.Column(db.Integer(12), nullable=False)
    Message = db.Column(db.String(120), nullable=False)
    Date = db.Column(db.String(12), nullable=False)
    Email = db.Column(db.String(120), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods = ['GET','POST'])
def contact():
    if(request.method=='POST'):
        '''add entry to the database'''
        name = request.form.get('Name')
        email = request.form.get('Email')
        phone = request.form.get('Phone_No')
        message = request.form.get('Meassage')

        entry = Contacts(Name=name,Phone_No=phone,Message=message,Email=email)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')


app.run(debug=True)

