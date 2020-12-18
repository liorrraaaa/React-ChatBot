#Set virtual environment:
#   python3 -m venv venv
#   . venv/bin/activate

#Run servers:
#   run flask
#   npm start

import time
from flask import Flask

app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}