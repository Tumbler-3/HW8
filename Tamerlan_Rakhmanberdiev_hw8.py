import sqlite3
from sqlite3 import Error

def connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql_table):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_table)
    except Error as e:
        print(e)


def create_products(conn):
    try:
        sql = '''
        INSERT INTO products (product_title, price, quantity) 
        VALUES ("Aston water", 12, 600), ("Ios water", 24, 300), ("West coffee", 119.49, 155), ("Freshy water", 25, 553),
        ("Qera soda", 44.99, 200), ("Aston juice", 114, 190), ("Qera juice", 180, 600), ("Ciocco soda", 49.99, 300),
        ("Coslo coffee", 60.44, 300), ("Ios coffee", 50, 340), ("Chiocco coffee", 34.99, 100), ("East water", 30, 100),
        ("Boom soda", 34.23, 150), ("Boom juice", 100, 350), ("Ohio soda", 33.49, 243)
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(e)


def update_quantity(conn, product):
    try:
        sql = '''
        UPDATE products SET quantity = ? WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def update_price(conn, product):
    try:
        sql = '''
        UPDATE products SET price = ? WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def delete(conn, id):
    try:
        sql = '''
        DELETE FROM products WHERE id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)


def select_all(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM products''')

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)


def select_products_by_price(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)


def select_products_by_name(conn, name):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql,(name,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)


db_name = 'hw.db'
sql_table = '''CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE(8, 2) NOT NULL DEFAULT 0.0,
    quantity INT(5) NOT NULL DEFAULT 0)'''

conn = connection(db_name)

if conn != None:
    create_table(conn, sql_table)
    create_products(conn)

    update_price(conn, (100.33, 4))

    update_quantity(conn, (133, 3))

    #select_all(conn)
    #delete(conn, 15)
    #select_products_by_price(conn)
    #select_products_by_name(conn, "%water%")
    