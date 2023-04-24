from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.son import SON
#import settings
import datetime
from . import settings

client = MongoClient(settings.mongo_st)

db = client.MVC_FM
#print(db)
#import fake_data
#users = db.users
#new_user = users.insert_one(fake_data.gerar_user()).inserted_id
#print(new_user)


class User:

    def __init__(self, name, iana_id, address, phone_number, email, job, date, _id=None, date_in=None, status=None, debtor=None, books=None) -> None:
        
        self.name = name
        self.iana_id = iana_id
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.job = job
        self.date = date
        self.date_in = datetime.datetime.now()
        self.status = True
        self.debtor = False
        self.books = []
        self._id = _id
    

    def parser(self):

        dicio = {
            'name'          :self.name,
            'iana_id'       :self.iana_id , 
            'address'       :self.address , 
            'phone_number'  :self.phone_number , 
            'email'         :self.email , 
            'job'           :self.job , 
            'date'          :self.date ,
            'date_in'       :self.date_in ,
            'status'        :self.status ,
            'debtor'        :self.debtor ,
            'books'         :self.books
        }

        return dicio
    
    def new_user(self):


        users = db.users
        new_user = users.insert_one(self.parser()).inserted_id        

        print(new_user)
    

    def insert_books_read(self, new_values):
        
        users = db.users
        #self.new_values = new_values
        #newvalues = { "$set": { 'company': "sony" } }
        
        users.update_one({'_id':self._id}, {"$push": {'books': new_values}}).upserted_id






    @staticmethod
    def show_user(obj_id):

        #obj_id = ObjectId('644486b973018a1d84eb1437')
        obj_id = ObjectId(obj_id)
        
        users = db.users
        user = users.find_one({'_id': obj_id})

        return user



    @staticmethod
    def show_all_users():

        users = db.users
        lista = users.find()

        return lista



    @staticmethod
    def delete_all_users():

        users = db.users
        dele = users.drop()


