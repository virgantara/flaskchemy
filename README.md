## Selamat datang di Flask & SQLAlchemy Tutorial ###  
Di sini, kita akan belajar mengenal Rest API dengan Flask dan Object Relational Mapping (ORM) di Python dengan SQLAlchemy

### Prasyarat ###  
1. Python 3
1. git
1. MySQL database

### Instalasi SQL Alchemy ###  
`
pip3 install sqlalchemy
`

Untuk memastikan bahwa SQLAlchemy sudah terinstall, silakan buka terminal. Kemudian, jalankan perintah berikut:  

`python3`  
`import sqlalchemy`    
`sqlalchemy.__version__`    

maka, akan muncul versi dari SQLAlchemy.

### Instalasi Flask ###
`
pip3 install flask
`  

Kemudian, buat file baru dengan nama **server.py** dan taruh di 
dalam directory projectmu. Copy-paste kode berikut:  
```
from flask import Flask
app = Flask(__name__)  

@app.route('/')
def hello_world():
    return 'Hello world!'
```

Buka terminal, ketik perintah:  
### Linux ###
```
export FLASK_APP=server.py
```

### Windows ###  
```
setx FLASK_APP "server.py"
```

Buka terminal, masuk ke directory project, jalankan perintah berikut:  
```
flask run
```

### P