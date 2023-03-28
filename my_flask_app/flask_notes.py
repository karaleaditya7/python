python3 -V
sudo apt install python3-venv
mkdir my_flask_app
cd my_flask_app
python3 -m venv venv
source venv/bin/activate
pip install Flask
python -m flask --version

=================================

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

=================

export FLASK_APP=hello
export FLASK_ENV=development

flask run
flask run -p 5001

# when we create any website in flask, its an app 

ps -fA | grep python

kill -9 <port on which app running>

===========================
crete 2 folders in application folder==> static, templates

static folder is public
template folder is private

create index.html page in templates 

install sublime text 3

==============

https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

===================================

bootstrap templates

 <link href="css/styles.css" rel="stylesheet" /> ===> <link href="{{url_for('static', filename='css/styles.css') }}"rel="stylesheet" />


