# ----- 01. (convert hackerrank into call into postman)

# from importlib.util import resolve_name
# from urllib import response
# from flask import Flask, jsonify, request, request_started
# import requests
# app = Flask(__name__)

# def data(n,m,s):
#     if (m + s - 1) % n == 0:
#         return {'chair':(n)}
#         # return jsonify(n)
#         # return n
#     else:
#         return {'chair':(m + s - 1) % n}
#         # return jsonify((m + s - 1) % n)
#         # return (m + s - 1) % n

# @app.route('/save-the-prisoners2', methods=['GET','POST']) # (other queries API)
# def handler():
#     req = request.get_json()
#     n = req['prisoners']
#     m = req['sweets']
#     s = req['chairs']
#     return jsonify(data(n,m,s))

# @app.route('/save-the-prisoners', methods=['POST']) # (body, multi list)
# def handler_multi():
#     lst = []
#     req = request.get_json()['test_cases']
#     for x in req:
#         n = x['prisoners']
#         m = x['sweets']
#         s = x['chairs']
#         lst.append(data(n,m,s))
#     # return jsonify(lst)
#     return {'chairs':lst}

# @app.route('/save-the-prisoners3/prisoners/<int:prisoners>/candy/<int:candy>', methods=['POST'])
# def handler_path(prisoners,candy):
#     # p = int(prisoners)
#     # c = int(candy)
#     if request.args.get('start') != None:
#         start = int(request.args.get('start'))
#     else:
#         start = 1
#     return (data(prisoners,candy,start))



# ----- 02. task hackerrank
# from flask import Flask, request
# app = Flask(__name__)

# def data(a,k,queries):
#     for x in range(len(queries)):
#         queries[x] = a[(queries[x]-int(k))%len(a)]
#     return {'result':(queries)}
# # print(data([3,4,5],2,[1,2]))
# # print(data([1,2,3],2,[0,1,2]))


# @app.route('/circular-array', methods=['GET'])
# def handler():
#     k = request.headers.get('rotation-count')
#     req = request.get_json()
#     a = req['data']
#     queries = req['query']
#     return data(a,k,queries)




# ----- 03. task hackerrank
# url (http://127.0.0.1:5000/find-digits)
# (version 1.3)

# from itertools import count
# from flask import Flask,request
# app = Flask(__name__)

# def data(n):
#     count = 0
#     lst = str(n)
#     for x in lst:
#         if int(x) != 0 and n % int(x) == 0:
#             count += 1
#     return count


# # @app.route('/find-digits', methods=['POST'])
# # def handler():
# #     lst = []
# #     req = request.get_json()['check']
# #     for x in range(len(req)):
# #         lst.append(str(data(req[x])))
# #     return {'result': lst} 

# # http://127.0.0.1:5000/find-digits

# @app.route('/find-digits-next', methods=['POST'])
# def handler():
#     req = request.get_json()['check']
#     for x in range(len(req)):
#         var_output = { 
#             'input':req[x],
#             'output':str(data(req[x]))
#         }
#     return {
#         'result':(var_output)
#     }
