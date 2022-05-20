from flask import Flask, request
app = Flask(__name__)

def data(a,k,queries):
    for x in range(len(queries)):
        queries[x] = a[(queries[x]-int(k))%len(a)]
    return {'result':(queries)}
# print(data([3,4,5],2,[1,2]))
# print(data([1,2,3],2,[0,1,2]))


@app.route('/circular-array', methods=['GET'])
def handler():
    k = request.headers.get('rotation-count')
    req = request.get_json()
    a = req['data']
    queries = req['query']
    return data(a,k,queries)
