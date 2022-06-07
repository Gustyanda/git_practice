from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
db=SQLAlchemy(app)

app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Kehidupan6@localhost:5432/db_course?sslmode=disable'


study=db.Table('study',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('instructor_id', db.Integer, db.ForeignKey('instructor.id'), nullable=False))

class Category(db.Model):
    id=db.Column(db.Integer, primary_key=True, index=True)
    tag=db.Column(db.String, nullable=False)
    public_id=db.Column(db.String, nullable=False)

class Course(db.Model):
    id=db.Column(db.Integer, primary_key=True, index=True)
    lesson=db.Column(db.String, nullable=False)
    public_id=db.Column(db.String, nullable=False)
    categories_id=db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    study_course1=db.relationship('Instructor', backref='course_1', secondary='study')
    study_course2=db.relationship('User', backref='course_2', secondary='study')

class Instructor(db.Model):
    id=db.Column(db.Integer, primary_key=True, index=True)
    coach=db.Column(db.String, nullable=False)
    public_id=db.Column(db.String, nullable=False)
    study_instructor1=db.relationship('Course', backref='instructor_1', secondary='study')
    study_instructor2=db.relationship('User', backref='instructor_2', secondary='study')    

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True, index=True)
    name=db.Column(db.String, nullable=False)
    public_id=db.Column(db.String, nullable=False)
    study_user1=db.relationship('Course', backref='user_1', secondary='study')
    study_user2=db.relationship('Instructor', backref='user_2', secondary='study')  


# # create table default
# db.create_all()
# db.session.commit()

@app.route('/home', methods=['GET'])
def home():
    