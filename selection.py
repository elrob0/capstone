import request

import json
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'craft beer!'
# named fJson b/c of other json imports
from flask import json as fJson
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['craftbeer.json']  
            