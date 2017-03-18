from flask import Flask
from flask import render_template
import os
from flask import send_from_directory
app = Flask(__name__)

@app.route('/')
@app.route('/<red>.<green>.<blue>.<power>')
def index(red=0, green=0, blue=0, power=0):
    return render_template('index.html', r=red, g=green, b=blue, p=power)

@app.route('/favicon.png')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png')
