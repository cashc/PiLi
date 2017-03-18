from flask import Flask
from flask import render_template
# import os
# from flask import send_from_directory
app = Flask(__name__)

@app.route('/')
@app.route('/<red>,<green>,<blue>,<power>')
def index(red=255, green=255, blue=255, power=1):
    return render_template('index.html', r=red, g=green, b=blue, p=power)

