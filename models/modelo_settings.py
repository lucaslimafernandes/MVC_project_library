import urllib.parse


username = urllib.parse.quote_plus('username')
password = urllib.parse.quote_plus('password')

host = urllib.parse.quote_plus('localhost')
port = urllib.parse.quote_plus('27017')


mongo_st = f'mongodb://{username}:{password}@{host}:{port}/mydbone'

