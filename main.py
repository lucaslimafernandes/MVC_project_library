from flask import Flask, request
from flask import render_template, redirect

from models.users import User
from models.books import Books, Read
from models.fake_data import gerar_user

from controllers.controller import c_index

app = Flask(__name__)


@app.route('/')
def index():
    #return 'MVC: Flask'
    #a = User(**gerar_user())
    ##a = a.parser()
    #print(a)
    #print(a.parser())
    #return render_template('index.html', users=[a.parser()])

    all_users = User.show_all_users()
    all_books = Books.show_all_books()

    return render_template('index.html', users=all_users, books=all_books)


@app.route('/users/new', methods=['POST','GET'])
def new_user():
    if request.method == 'POST':
        user = User(**request.form)
        user.new_user()
        return redirect('/')
    else:
        return render_template('new_user.html')


@app.route('/teste/gerar_user/<number>')
def route_gerar_user(number=1):
    
    for i in range(int(number)):
        u = User(**gerar_user())
        u.new_user()
    return redirect('/')


@app.route('/books/new', methods=['POST','GET'])
def new_book():
    if request.method == 'POST':
        book = Books(**request.form)
        book.new_book()
        return redirect('/')
    else:
        return render_template('new_book.html')

@app.route('/user/new_read/<user_id>', methods=['POST','GET'])
def read_user(user_id=None):
    if request.method == 'POST':
        return redirect('/')

    else:

        user = User.show_user(user_id)
        books = Books.show_all_books()
        return render_template('new_reading.html', template='USER', user=user, books=books)


@app.route('/book/new_read/<book_id>', methods=['POST','GET'])
def read_book(book_id):
    if request.method == 'POST':
        return redirect('/')

    else:

        users = User.show_all_users()
        book = Books.show_book(book_id)
        return render_template('new_reading.html', template='BOOK', users=users, book=book)


@app.route('/save_read', methods=['POST','GET'])
def save_read(user_id=None):
    if request.method == 'POST':
        user = request.form['user']
        book = request.form['book']
        read = Read(book=book, user=user)

    return redirect('/')

