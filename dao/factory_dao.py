import sqlite3
from utils import distance
def dict_factory(cursor,row):
    d={}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_factory(name, longitude, latitude):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO factory (name, longitude, latitude) VALUES (?, ?, ?)
    ''', (name, float(longitude), float(latitude), ))
    conn.commit()
    factory_id = cursor.lastrowid

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()
    return read_factory(factory_id)

def get_nearest_factory(longitude, latitude):
    allFactory = get_all_factory()
    nearestFactory = allFactory[0]
    nearestDistance = distance.haversine(float(latitude), float(longitude), nearestFactory["latitude"], nearestFactory["longitude"])
    nearestFactory["distance"] = nearestDistance
    for factory in allFactory:
        currentDistance = distance.haversine(float(latitude), float(longitude), factory["latitude"], factory["longitude"])
        if currentDistance < nearestDistance:
            nearestFactory = factory
            nearestFactory["distance"] = currentDistance

    return nearestFactory

def get_all_factory():
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM factory')
    factory = cursor.fetchall()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()
    return factory
    
def read_factory(factoryId):
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM factory WHERE factoryId = ?', (factoryId,))
    factory = cursor.fetchone()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()
    return factory

def update_factory(factoryId, name=None, longitude=None, latitude=None):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    if name and longitude and latitude:
        cursor.execute('''
            UPDATE factory SET name = ?, longitude = ?, latitude = ? WHERE factoryId = ?
        ''', (name, longitude, latitude, factoryId))
    elif name:
        cursor.execute('''
            UPDATE factory SET name = ? WHERE factoryId = ?
        ''', (name, factoryId))
    conn.commit()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()

    return read_factory(factoryId)
