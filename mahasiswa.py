from sqlalchemy import *
from base import Base


class Mahasiswa(Base):
    __tablename__ = 'mahasiswa'

    nim = Column(String, primary_key=True)
    nama = Column(String)
    alamat = Column(String)