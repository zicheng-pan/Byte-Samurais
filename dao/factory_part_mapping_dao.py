import sqlite3
from utils import distance
def dict_factory(cursor,row):
    d={}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_factory_part(factoryId, partId):
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM factory_parts_mapping WHERE factoryId = ? and partId = ?', (factoryId, partId))
    factory = cursor.fetchone()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()
    return factory

def get_all_factory_parts(factoryId):
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM factory_parts_mapping WHERE factoryId = ?', (factoryId,))
    factory = cursor.fetchall()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()
    return factory

def create_factory_part(factoryId, partId, quantity):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO factory_parts_mapping (factoryId, partId, quantity) VALUES (?, ?, ?)
    ''', (factoryId, partId, int(quantity)))
    conn.commit()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()
    return get_factory_part(factoryId, partId)

def update_factory_part(factoryId, partId, quantity):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE factory_parts_mapping SET quantity = ? WHERE factoryId = ? and partId = ?
    ''', (int(quantity), factoryId, partId))

    conn.commit()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()

    return get_factory_part(factoryId, partId)
