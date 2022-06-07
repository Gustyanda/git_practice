from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid, base64
app=Flask(__name__)
db=SQLAlchemy(app)

app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Kehidupan6@localhost:5432/db_course?sslmode=disable'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# study=db.Table('study',
#     db.Column('category_id', db.Integer, db.ForeignKey('category.id'), nullable=False),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
#     db.Column('instructor_id', db.Integer, db.ForeignKey('instructor.id'), nullable=False))




class Category(db.Model):
    id=db.Column(db.Integer, primary_key=True, index=True)
    public_id=db.Column(db.String, nullable=False)
    tag=db.Column(db.String, nullable=False)
    course=db.relationship('Course', backref='categories')

class Course(db.Model):
    id=db.Column(db.Integer, primary_key=True, index=True)
    public_id=db.Column(db.String, nullable=False)
    lesson=db.Column(db.String, nullable=False)
    categories_id=db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    # study_course1=db.relationship('Instructor', backref='course_1', secondary='study')
    # study_course2=db.relationship('User', backref='course_2', secondary='study')

class Instructor(db.Model):
    id=db.Column(db.Integer, primary_key=True, index=True)
    public_id=db.Column(db.String, nullable=False)
    coach=db.Column(db.String, nullable=False)
    status=db.Column(db.String)
    # study_instructor1=db.relationship('Course', backref='instructor_1', secondary='study')
    # study_instructor2=db.relationship('User', backref='instructor_2', secondary='study')    

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True, index=True)
    public_id=db.Column(db.String, nullable=False)
    name=db.Column(db.String, nullable=False)
    username=db.Column(db.String, nullable=False, unique=True)
    password=db.Column(db.String, nullable=False, unique=True)
    # course=db.relationship('Course', backref='user_1', secondary='study')
    # study_user2=db.relationship('Instructor', backref='user_2', secondary='study')  

class Study(db.Model):
    id=db.Column(db.Integer, primary_key=True, index=True)
    public_id=db.Column(db.String, nullable=False)
    course_id=db.Column(db.Integer, db.ForeignKey('course.id'))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    instructor_id=db.Column(db.Integer, db.ForeignKey('instructor.id'))

# # create table default
# db.create_all()
# db.session.commit()




@app.route('/', methods=['GET'])
def home():
    return {
        'message': 'WELCOME TO COURSE ONLINE'
    }





def auth_user(auth):
    encode = base64.b64decode(auth[6:])
    str_encode = encode.decode('ascii')
    






@app.route('/category', methods=['GET'])
def get_category():
    return jsonify ([
        { 
            'tag':category.tag
        } for category in Category.query.all()
    ])

@app.route('/category', methods=['POST'])
def create_category():
    data = request.get_json()
    if len(data['tag']) == 0:
        return {
            'message': 'must fill tag detail !'
        }, 400
    
    c = Category(
        public_id=str(uuid.uuid4()),
        tag=data['tag']
    )

    db.session.add(c)
    db.session.commit()
    return {
        'message': 'tag successfully create'
    }, 201




@app.route('/course', methods=['GET'])
def get_course():
    return jsonify ([
        {
            'lesson':course.lesson,
            'categories':{
                'tag': course.categories.tag
            } 
        } for course in Course.query.all()
    ])

@app.route('/course', methods=['POST'])
def create_course():
    data = request.get_json()
    if len(data['lesson']) == 0:
        return {
            'message': 'must fill lesson detail!'
        }, 400

    category = Category.query.filter_by(tag=data['tag']).first()
    if not category:
        return {
            'message': 'tag needs for search !'
        }, 400

    c = Course(
        public_id=str(uuid.uuid4()),
        lesson=data['lesson'],
        categories_id=category.id
    )
    db.session.add(c)
    db.session.commit()
    return {
        'message': 'lesson successfully create !'
    }, 201




@app.route('/instructor', methods=['GET'])
def get_instructor():
    return jsonify([
        {
            'coach':instructor.coach, 'status':instructor.status
        } for instructor in Instructor.query.all()
    ])

@app.route('/instructor', methods=['POST'])
def create_instructor():
    data = request.get_json()
    if len(data['coach']) == 0:
        return {
            'message': 'name instructor required !'
        }, 400

    i = Instructor(
        public_id=str(uuid.uuid4()),
        coach=data['coach'],
        status=data['status']
    )
    db.session.add(i)
    db.session.commit()
    return {
        'message': 'instructor successfully add !'
    }, 201

@app.route('/instructor/<id>', methods=['PUT'])
def update_instructor(id):
    data = request.get_json()
    instructor = Instructor.query.filter_by(public_id=id).first_or_404()
    instructor.status = data['status']
    db.session.commit()
    return jsonify({
        'coach':instructor.coach, 'status':instructor.status
    })




@app.route('/user', methods=['GET'])
def get_user():
    return jsonify ([
        {
            'name':user.name, 'username':user.username
        } for user in User.query.all()
    ])

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    if len(data['name']) == 0:
        return {
            'message': 'name requirement for applicant student !'
        }, 400

    if len(data['username']) > 15 and len(data['password']) > 15:
        return {
            'message': 'username/password is too long !'
        }, 400

    u = User(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        username=data['username'],
        password=data['password']
    )
    db.session.add(u)
    db.session.commit()
    return {
        'message': 'user successfully create !'
    }, 201

@app.route('/user/<id>', methods=['GET'])
def get_user_id(id):
    user = User.query.filter_by(public_id=id).first_or_404()
    return jsonify ({
        'name':user.name, 'username':user.username, 'password':user.password
    })

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.filter_by(public_id=id).first_or_404()
    user.username = data['username']
    user.password = data['password']
    db.session.commit()
    return {
        'message': 'data has been update !'
    }






    