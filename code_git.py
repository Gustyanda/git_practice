# url (http://127.0.0.1:5000/find-digits)
# (version 1.3)

from itertools import count
from flask import Flask,request
app = Flask(__name__)

def data(n):
    count = 0
    lst = str(n)
    for x in lst:
        if int(x) != 0 and n % int(x) == 0:
            count += 1
    return count


# @app.route('/find-digits', methods=['POST'])
# def handler():
#     lst = []
#     req = request.get_json()['check']
#     for x in range(len(req)):
#         lst.append(str(data(req[x])))
#     return {'result': lst} 

# http://127.0.0.1:5000/find-digits

@app.route('/find-digits-next', methods=['POST'])
def handler():
    req = request.get_json()['check']
    for x in range(len(req)):
        var_output = { 
            'input':req[x],
            'output':str(data(req[x]))
        }
    return {
        'result':(var_output)
    }