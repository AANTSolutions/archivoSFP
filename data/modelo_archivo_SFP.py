from typing import List
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, insert
from sqlalchemy import inspect


def create_table(_engine, column_names:List[str]):
    """


    :param column_names:
    :return:
    """
    _meta = MetaData()
    _parameters = ["test_table", _meta, Column("id", Integer, primary_key = True)]
    _columns = [Column(_name,String) for _name in column_names]
    _parameters.extend(_columns)
    _new_table = Table(*tuple(_parameters))
    _meta.create_all(_engine)


if __name__ == '__main__':
    engine = create_engine("sqlite:///sfp.db", echo=True)
    create_table(engine,["A", "B"])
    # ins = insert('test_table').values(id='1',A='a',B='b')
    # engine.execute('INSERT INTO "test_table" '
    #                '(id,A,B) '
    #                'VALUES (2,"aa","bb")')
    inspector = inspect(engine)
    tablas = inspector.get_table_names()

    print(tablas)
