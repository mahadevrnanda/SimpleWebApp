# Server side code
import numpy as np
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
@app.route('/random',methods=['GET'])
def random():
    size = request.args.get('size')
    dims = [int(k) for k in size.split('x')]
    return jsonify(array=np.random.randn(*dims).tolist(), size=int(np.array(dims).prod()))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8090,debug=True)