#!/miniconda3/envs/env/bin/python

from flask import jsonify,Flask,render_template, send_from_directory, send_file, request
from flask_cors import *

app = Flask(__name__, static_url_path='/static',static_folder='static')
CORS(app)


@app.route('/')
def icao_position_app():
    return render_template('/index.html')


@app.route('/data/<path:path>')
def send_data(path):
   return send_from_directory('static/',path)


@app.route('/get_max_min')
def max_min():
   #get the api request and calculate the max and min
   return


if __name__ == "__main__":
   app.run(host='0.0.0.0',port=5400,debug=True)
