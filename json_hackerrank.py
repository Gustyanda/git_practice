# ----- 01. (convert hackerrank into call into postman)

from importlib.util import resolve_name
from urllib import response
from flask import Flask, jsonify, request, request_started
import requests
app = Flask(__name__)

def data(n,m,s):
    if (m + s - 1) % n == 0:
        return {'chair':(n)}
        # return jsonify(n)
        # return n
    else:
        return {'chair':(m + s - 1) % n}
        # return jsonify((m + s - 1) % n)
        # return (m + s - 1) % n

@app.route('/save-the-prisoners2', methods=['GET','POST']) # (other queries API)
def handler():
    req = request.get_json()
    n = req['prisoners']
    m = req['sweets']
    s = req['chairs']
    return jsonify(data(n,m,s))

@app.route('/save-the-prisoners', methods=['POST']) # (body, multi list)
def handler_multi():
    lst = []
    req = request.get_json()['test_cases']
    for x in req:
        n = x['prisoners']
        m = x['sweets']
        s = x['chairs']
        lst.append(data(n,m,s))
    # return jsonify(lst)
    return {'chairs':lst}

@app.route('/save-the-prisoners3/prisoners/<int:prisoners>/candy/<int:candy>', methods=['POST'])
def handler_path(prisoners,candy):
    # p = int(prisoners)
    # c = int(candy)
    if request.args.get('start') != None:
        start = int(request.args.get('start'))
    else:
        start = 1
    return (data(prisoners,candy,start))
