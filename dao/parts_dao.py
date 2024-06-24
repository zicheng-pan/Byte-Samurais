import sqlite3
def dict_factory(cursor,row):
    d={}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_part(name):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO parts (name, delete_flag) VALUES (?, 0) ', (name, ))
    conn.commit()
    part_id = cursor.lastrowid

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()
    return read_part(part_id)

def get_all_part():
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM parts')
    parts = cursor.fetchall()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()
    return parts
    
def read_part(partId):
    conn = sqlite3.connect('test.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM parts WHERE partId = ?', (partId,))
    part = cursor.fetchone()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()
    return part

def update_part_delete_flag(partId, delete_flag):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE parts SET delete_flag = ? WHERE partId = ?
    ''', (delete_flag, partId))
    conn.commit()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()

def update_part(partId, name=None):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE parts SET name = ? WHERE partId = ?
    ''', (name, partId))
    conn.commit()

    # 关闭Cursor:
    cursor.close()
    # 关闭Connection:
    conn.close()

    return read_part(partId)

def delete_part(partId):
    update_part_delete_flag(partId, 1)

def reactive_part(partId):
    update_part_delete_flag(partId, 0)

