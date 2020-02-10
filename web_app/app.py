import os
from flask import Flask, render_template, request
from flask import redirect, url_for, session

# get the base directory of __file__ --> app.py
basedir = os.path.abspath(os.path.dirname(__file__))
# create Flask application
app = Flask(__name__)
# this is for security
app.config['SECRET_KEY'] = 'princejudecarlo'

############################
### VIEW FUNCTIONS W FORMS #
############################

# below are the backend of each html
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
