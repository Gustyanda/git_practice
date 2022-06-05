@app.route('/login', methods=['GET', 'POST'])
def auth():
    auth_header = request.headers.get('Authorization')
    encode_var = base64.b64decode(auth_header[6:])
    string_var = encode_var.decode('ascii')
    lst = string_var.split(':')
    users = lst[0]
    passes = lst[1]
    usernames = User.query.filter_by(username=users).first()
    passwords = User.query.filter_by(password=passes).first()
    if (usernames != None) and (passwords != None):
        return 'True' # expected output in end point
    else:
        return 'False'
