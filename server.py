from flask import Flask, request
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
import base
from mahasiswa import Mahasiswa

app = Flask(__name__)

engine = create_engine("mysql+mysqldb://root:4Dm1n_2020@localhost:3306/belajar")
base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def hello_world():
    return 'Selamat datang di tutorial Flask'


@app.route('/input',methods=['POST'])
def input_mahasiswa():
    if request.method == 'POST':
        mhs = Mahasiswa()
        mhs.nama = request.form['nama']
        mhs.nim = request.form['nim']
        mhs.alamat = request.form['alamat']
        try:

            session.add(mhs)
            session.commit()
        except exc.SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            return error

    return "Oke"