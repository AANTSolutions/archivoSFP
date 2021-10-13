from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
     ForeignKey, event
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base

from archivoSFP.lib import util

engine = create_engine("sqlite:///sfp.db", echo=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Model = declarative_base(name='Model')
Model.query = db_session.query_property()


class Registros(Model):
    __tablename__ = 'test_table'
    id = Column('id', Integer, primary_key=True)
    A = Column('A', String(200))
    B = Column('B',String(200))

    def __init__(self, A, B):
        self.A = A
        self.B = B


lista = util.crea_lista("../prueba.dat")

if __name__ == '__main__':
    new_register = Registros(lista[0],lista[1])
    db_session.add(new_register)
    db_session.commit()