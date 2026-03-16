import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db=sqlite3.connect(os.path.join(BASE_DIR,"bookscollection.db"))
cursor=db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT  INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
