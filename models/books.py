from pymongo import MongoClient
from bson.objectid import ObjectId
import settings
import datetime

from users import User

client = MongoClient(settings.mongo_st)

db = client.MVC_FM
#print(db)
#import fake_data
#users = db.users
#new_user = users.insert_one(fake_data.gerar_user()).inserted_id
#print(new_user)



#https://www.saraiva.com.br/a-arte-da-guerra----os-treze-capitulos-originais/p
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

        #obj_id = ObjectId('644486b973018a1d84eb1437')
        obj_id = ObjectId(obj_id)
        
        users = db.books
        user = users.find({'_id': obj_id})

        return user


    @staticmethod
    def show_all_books():

        users = db.books
        lista = users.find()

        return lista


class Loan:

    def __init__(self, book, person) -> None:
        self.book = book
        self.person = person



    
    def emprestimo(self):
        pass