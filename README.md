## Selamat datang di Flask & SQLAlchemy Tutorial ###  
Di sini, kita akan belajar mengenal Rest API dengan Flask dan Object Relational Mapping (ORM) di Python dengan SQLAlchemy

### Prasyarat ###  
1. Python 3
1. git
1. MySQL database

### Instalasi SQL Alchemy ###  
```commandline
pip3 install sqlalchemy
```



Untuk memastikan bahwa SQLAlchemy sudah terinstall, silakan buka terminal. Kemudian, jalankan perintah berikut:  
```commandline
python3
import sqlalchemy
sqlalchemy.__version__
```

maka, akan muncul versi dari SQLAlchemy.

### Instalasi Flask ###
```commandline
pip3 install flask
```  

Kemudian, buat file baru dengan nama **server.py** dan taruh di 
dalam directory projectmu. Copy-paste kode berikut:  
```buildoutcfg
from flask import Flask
app = Flask(__name__)  

@app.route('/')
def hello_world():
    return 'Hello world!'
```

Buka terminal, ketik perintah:  
### Linux ###
```commandline
export FLASK_APP=server.py
```

### Windows ###  
```commandline
setx FLASK_APP "server.py"
```

Buka terminal, masuk ke directory project, jalankan perintah berikut:  
```commandline
flask run
```

### Deklarasi Base class ### 
Apa itu Base class?  
Base class adalah class yang menjadi object pemetaan dengan database. 
Semua class yang dipetakan ke table dari database harus merupakan turunan dari Base class.
Buatlah sebuah file dengan nama **base.py**, isinya sebagai berikut:  
```buildoutcfg
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```

### Membuat class dari salah satu table ###
Di dalam database project ini hanya ada satu tabel, yaitu mahasiswa. Tabel ini berisi tiga kolom yaitu nim, nama, dan alamat.  
Untuk membuat class Mahasiswa, copy-paste kode berikut:  
```buildoutcfg
from sqlalchemy import *
from base import Base

class Mahasiswa(Base):
    __tablename__ = 'mahasiswa'

    nim = Column(String, primary_key=True)
    nama = Column(String)
    alamat = Column(String)
```

### Koneksi database dengan SQLAlchemy ###

Untuk koneksi dengan MySQL cukuplah sederhana, yaitu dengan membuat instance dari create_engine SQLAlchemy. Contohnya:  
```buildoutcfg
engine = create_engine("mysql+mysqldb://<dbuser>:<dbpass>@<host>:<post>/<nama_databasemu>")
base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
```

### Routing dengan Flask ###
Agar routing bisa diakses baik melalui browser atau client apapun, setiap function harus memiliki annotation route. Contohnya adalah:  
```buildoutcfg
@app.route('/')
def hello_world():
    return 'Selamat datang di tutorial Flask'
```

Route ('/) merupakan basic route atau route default dari Flask. Ketika Anda mengetik http://localhost:<port>, maka yang dijalankan adalah route ini.  

### Menjalankan Flask dengan port tertentu ###
Default port Flask adala 5000. Ketika menjalankan perintah `flask run`, maka yang dijalankan oleh Flask adalah http://127.0.0.1:5000. 
Namun, apabila Flask ingin dijalankan port custom, perintahnya adalah  
```commandline
flask run --port=2021
```

### Menerima HTTP POST Request ### 
Di sini, saya contohkan bagaimana menambah data via Flask ke SQLAlchemy. Contohnya:  
```buildoutcfg
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
```

POST Request yang dicontohkan adalah menggunakan **x-www-form-urlencoded**  
Anda bisa simulasikan POST Request ini dengan Postman, Insomnia, atau perintah CURL berikut:  
```buildoutcfg
curl --location --request POST 'http://localhost:2021/input' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'nim=123123' \
--data-urlencode 'nama=testing' \
--data-urlencode 'alamat=abc'
```

# --- Selamat Belajar --- #