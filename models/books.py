from pymongo import MongoClient
from bson.objectid import ObjectId
from . import settings
#import settings
import datetime

from .users import User

client = MongoClient(settings.mongo_st)

db = client.MVC_FM
#print(db)
#import fake_data
#users = db.users
#new_user = users.insert_one(fake_data.gerar_user()).inserted_id
#print(new_user)



#https://www.saraiva.com.br/a-arte-da-guerra----os-treze-capitulos-originais/p
#644597ff42a587b4e0cf1039
#Ano da Edição
#2008
#Autor
#Tzu, Sun
#Editora
#Geração Editorial Ltda
#Idioma
#Português
#ISBN
#978-85-60018-00-0


class Books:

    def __init__(self, book, author, publishing, idiom, isbn, year, _id=None, available=None, loan=None) -> None:
        
        self.book = book
        self.author = author
        self.publishing = publishing
        self.idiom = idiom
        self.isbn = isbn
        self.year = year
        self.available = True
        self.loan = []
    

    def parser(self):

        dicio = {
            'book'          :self.book,
            'author'        :self.author,
            'publishing'    :self.publishing,
            'idiom'         :self.idiom,
            'isbn'          :self.isbn,
            'year'          :self.year
        }

        return dicio
    
    def new_book(self):

        books = db.books
        new_book = books.insert_one(self.parser()).inserted_id

        print(new_book)
    

    @staticmethod
    def show_book(obj_id):

        obj_id = ObjectId(obj_id)
        
        books = db.books
        book = books.find_one({'_id': obj_id})



        return book
    
    @staticmethod
    def show_all_books():

        books = db.books
        lista = books.find()

        return lista


class Read:

    def __init__(self, book, user) -> None:

        self._user = User.show_user(user)
        self._book = Books.show_book(book)
        
        self.loan()

    
    def loan(self):
        
        self.user = User(**self._user)
        self.book = Books(**self._book)

        parser_book = self.book.parser()

        self.user.insert_books_read(parser_book)



if __name__ == '__main__':

    book = '644597ff42a587b4e0cf1039'
    user = '6445bc180fd159ee2d74d9b4'

    a = Read(book, user)
    