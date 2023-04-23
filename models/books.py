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

    def __init__(self, book, author, publishing, idiom, isbn, year) -> None:
        
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

        #obj_id = ObjectId('644597ff42a587b4e0cf1039')
        obj_id = ObjectId(obj_id)
        
        books = db.books
        book = books.find({'_id': obj_id})

        return book
    
        #FAZER A CHAMADO BOOK AQUI


    @staticmethod
    def show_all_books():

        books = db.books
        lista = books.find()

        return lista


class Loan:

    def __init__(self, book, person) -> None:
        self.book = book
        #self.person = person

        user = User.show_user(person)
        print(user)
        print(user[0])
        user = User(**user[0]).parser()

        user_books = user['books']

        print(user_books)


    
    def emprestimo(self):
        pass


if __name__ == '__main__':

    book = '644597ff42a587b4e0cf1039'
    user = '64459bbe39e1ed3c40dfae7f'

    a = Loan(book, user)
    