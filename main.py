from flask import Flask
from flask import render_template

from models.users import User
from models.fake_data import gerar_user

app = Flask(__name__)


@app.route('/')
def root():
    #return 'MVC: Flask'
    #a = User(**gerar_user())
    ##a = a.parser()
    #print(a)
    #print(a.parser())
    #return render_template('index.html', users=[a.parser()])

    all_users = User.show_all_users()

    return render_template('index.html', users=all_users)


