import numpy as np
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>Deployed to Heroku!!! Abhishek Yanamandra</h1>"


@app.route('/random', methods=['GET'])
def random():
    size = request.args.get('size')
    dims = [int(k) for k in size.split('x')]
    return jsonify(array=np.random.randn(*dims).tolist(), size=int(np.array(dims).prod()))
