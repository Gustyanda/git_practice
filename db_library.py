from email.policy import default
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid, base64, requests
app = Flask(__name__)
db = SQLAlchemy(app)

# # config
app.config['SECRET KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Kehidupan6@localhost:5432/db_alchemy_book2?sslmode=disable'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True




author_book = db.Table('author_book',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), nullable=False),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), nullable=False))

# # class
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    tag = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    public_id = db.Column(db.String, nullable=False)
    books = db.relationship('Book', backref='kategori', lazy='dynamic')

    def __repr__(self):
        return f'Category <{self.tag}>'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(30), nullable=False)
    release = db.Column(db.Date, nullable=False)
    public_id = db.Column(db.String, nullable=False)
    categories_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    categories = db.relationship('Category', backref='buku')
    auth_book = db.relationship('Author', secondary='author_book', backref='buku')

    def __repr__(self):
        return f'Book <{self.title}>'

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(30), nullable=False)
    bod = db.Column(db.Date, nullable=False)
    public_id = db.Column(db.String, nullable=False)
    auth_author = db.relationship('Book', secondary='author_book', backref='penulis')

    def __repr__(self):
        return f'Author <{self.name}>'

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True, index=True)
#     name = db.Column(db.String(30), nullable=False)
#     username = db.Column(db.String(10), nullable=False, unique=True)
#     password = db.Column(db.String(10), nullable=False,unique=True)
#     public_id = db.Column(db.String, nullable=False)
#     is_admin = db.Column(db.Boolean, default=False)
#     rents = db.relationship('User', backref='pinjam', lazy='dynamic')

#     def __repr__(self):
#         return f'User <{self.username}>'

# class Rent(db.Model):
#     id = db.Column(db.Integer, primary_key=True, index=True)
#     date_rent = db.Column(db.Date, nullable=False)
#     date_return = db.Column(db.Date, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     admin_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
#     books = db.relationship('Rent', backref='buku', lazy='dynamic')
 
#     def __repr__(self):
#         return f'Rent <{self.date_rent}>'





# # path home
@app.route('/')
def home():
    return {
        'message':'WELCOME TO OUR BOOK STORE'
    }



# # path author_book
@app.route('/author_books' , methods=['POST'])
def create_author_book():
    data = request.get_json()
    book = Book.query.filter_by(id=data['book_id']).first_or_404()
    author = Author.query.filter_by(id=data['author_id']).first_or_404()
    book.auth_book.append(author)
    db.session.add(book)
    db.session.commit()

    return {
        "message" : "success"
    },201


# # path Category
@app.route('/categories')
def get_categories():
    return jsonify([
        {
            'id': category.public_id, 'tag': category.tag, 'description': category.description
            } for category in Category.query.all()
    ])

@app.route('/categories/<id>/')
def get_category(id):
    print(id)
    category = Category.query.filter_by(public_id=id).first_or_404()
    return {
        'id': category.public_id, 'tag': category.tag, 'description': category.description
    }

# path query for insert,update,delete for category
@app.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    if not 'tag' in data or not 'description' in data:
        return jsonify ({
            'error': 'Bad Request',
            'message': 'There is no input'
        }), 400

    if len(data['tag']) == 0 or len(data['description']) == 0:
        return jsonify({
            'error': 'Bad Request',
            'message': 'tag and description must fill'
        }), 400
    
    c = Category(
        tag = data['tag'],
        description = data['description'],
        public_id = str(uuid.uuid4())
    )

    db.session.add(c)
    db.session.commit()
    return {
        'id': c.public_id, 'tag': c.tag, 'description': c.description
    }, 201

@app.route('/categories/<id>/', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    if 'tag' not in data:
        return {
            'error': 'Bad Request',
            'message': 'Tag needs'
        }, 400

    category = Category.query.filter_by(public_id=id).first_or_404()
    category.tag = data['tag']
    category.description = data['description']
    db.session.commit()
    return jsonify ({
        'id': category.public_id, 'tag': category.tag, 'description':category.description
    })

@app.route('/categories/<id>/', methods=['DELETE'])
def delete_category(id):
    category = Category.query.filter_by(public_id=id).first_or_404()
    db.session.delete(category)
    db.session.commit()
    return {
        'success': 'Data successfully delete'
    }




# # path Book
@app.route('/books')
def get_books():
    return jsonify([
        {
            'id': book.public_id, 'title': book.title, 'release': book.release, 
            'ketegori' : {
                'tag': book.kategori.tag,
                'description': book.kategori.description
            }
        } for book in Book.query.all()
    ])

@app.route('/books/<id>/')
def get_book(id):
    book = Book.query.filter_by(public_id=id).first_or_404()
    return jsonify ({
        'id': book.public_id, 'title': book.title, 'release': book.release, 
        'ketegori' : {
            'tag': book.kategori.tag,
            'description': book.kategori.description
        }        
    })

@app.route('/books/author') # get author_book data
def get_author_book():
    return jsonify([
        { 
            'id': book.public_id, 'title': book.title,
            'category': {
                'tag': book.categories.tag,
            },
            'author' : [
                x.name
                for x in book.penulis
            ]
        } for book in Book.query.all()
    ])



# path query for insert,update,delete for book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not 'title' in data or not 'release' in data:
        return jsonify({
            'error': 'Bad Request',
            'message': 'There is no input' 
        }), 400

    if len(data['title']) == 0 or len(data['release']) == 0:
        return jsonify({
            'error': 'Bad Request',
            'message': 'title and release must fill'
        }), 400

    category = Category.query.filter_by(tag=data['tag']).first()
    if not category:
        return {
            'error': 'Bad Request',
            'message': 'Invalid Tag' 
        }
    book = Book(
        title = data['title'],
        release = data['release'],
        categories_id = category.id,
        public_id = str(uuid.uuid4())
    )
    db.session.add(book)
    db.session.commit()
    return {
        'id': book.public_id, 'title': book.title, 'release': book.release,
        'kategori':{
            'tag': book.kategori.tag,
            'description': book.kategori.description            
        }
    }, 201

@app.route('/books/tag', methods=['POST']) # get data tag
def get_romance():
    data = request.get_json()
    categories = Category.query.filter_by(tag=data['tag']).first_or_404()
    b = []
    for x in categories.buku:
        b.append(x.title)
    return {
        'tag': categories.tag, 'books': b
    }

@app.route('/books/<id>/', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    print(data)
    print('title' in data)
    if not 'title' in data:
        return {
            'error': 'Bad Request',
            'message': 'Title needs'
        }, 400
    book = Book.query.filter_by(public_id=id).first_or_404()
    book.title = data.get('title', book.title)
    if 'title' in data or 'release' in data:
        book.title = data['title'],
        book.release = data['release']
    db.session.commit()
    return {
        'id': book.public_id, 'title': book.title, 'release': book.release,
        'kategori':{
            'tag': book.kategori.tag,
            'description': book.kategori.description            
        }
    }, 201

@app.route('/books/<id>/', methods=['DELETE'])
def delete_book(id):
    book = Book.query.filter_by(public_id=id).first_or_404()
    db.session.delete(book)
    db.session.commit()
    return {
        'success': 'Data successfully delete'
    }



# # path Author
@app.route('/authors')
def get_author():
    return jsonify ([
        {
            'id': author.public_id, 'name': author.name, 'bod': author.bod
        } for author in Author.query.all()
    ])

@app.route('/authors/<id>/')
def get_authors(id):
    author = Author.query.filter_by(public_id=id).first_or_404()
    return {
            'id': author.public_id, 'name': author.name, 'bod': author.bod        
    }

# path query for insert,update,delete for author
@app.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    if not 'name' in data or not 'bod' in data:
        return jsonify({
            'error': 'Bad Request',
            'message': 'There is no input'
        }), 400

    if len(data['name']) == 0 or len(data['bod']) == 0:
        return jsonify ({
            'error': 'Bad Request',
            'message': 'name and bod must fill'
        }), 400

    a = Author(
        name = data['name'],
        bod = data['bod'],
        public_id = str(uuid.uuid4())
    )

    db.session.add(a)
    db.session.commit()
    return {
            'id': a.public_id, 'name': a.name, 'bod': a.bod             
    }, 201

@app.route('/authors/<id>/', methods=['PUT'])
def update_author(id):
    data = request.get_json()
    if 'name' not in data:
        return {
            'error': 'Bad Request',
            'message': 'Name needs'
        }, 400

    author = Author.query.filter_by(public_id=id).first_or_404()
    author.name = data['name']
    author.bod = data['bod']
    db.session.commit()
    return jsonify ({
        'id': author.public_id, 'name': author.name, 'bod':author.bod
    })

@app.route('/authors/<id>/', methods=['DELETE'])
def delete_author(id):
    author = Author.query.filter_by(public_id=id).first_or_404()
    db.session.delete(author)
    db.session.commit()
    return {
        'success': 'Data successfully delete'
    }













# # create table default
# db.create_all()
# db.session.commit()