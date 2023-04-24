from flask import Flask
from flask import render_template

from models.users import User
from models.books import Books
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




