import sqlite3
from pprint import pprint

with sqlite3.connect('hwssqqll_db.sqlite3') as connection:
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    # query = """
    #     CREATE TABLE IF NOT EXISTS author(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #     name TEXT NOT NULL
    #     )
    # """
    # cursor.execute(query)
    #
    # query = """
    #     CREATE TABLE IF NOT EXISTS books(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #     title TEXT NOT NULL,
    #     author_id INTEGER,
    #     FOREIGN KEY (author_id) REFERENCES author(id)
    #     )
    # """
    # cursor.execute(query)

    # values = ['Parasolka', 4]
    # query = """
    #     INSERT INTO books(title, author_id)
    #     VALUES(?, ?)
    # """
    # cursor.execute(query, values)

    # query = """
    #     SELECT title, name
    #     FROM books
    #     JOIN author
    #     ON books.author_id = author.id
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())

    # query = """
    #     SELECT title, name
    #     FROM books
    #     LEFT JOIN author
    #     ON books.author_id = author.id
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())

    # query = """
    #     SELECT title, name, author_id     FULL OUTER AND RIGHT JOINs IS NOT WORKING
    #     FROM books                        FULL OUTER AND RIGHT JOINs IS NOT WORKING
    #     FULL JOIN author                  FULL OUTER AND RIGHT JOINs IS NOT WORKING
    #     ON books.author_id = author.id    FULL OUTER AND RIGHT JOINs IS NOT WORKING
    # """                                   FULL OUTER AND RIGHT JOINs IS NOT WORKING
    # result = cursor.execute(query)        FULL OUTER AND RIGHT JOINs IS NOT WORKING
    # pprint(result.fetchall())             FULL OUTER AND RIGHT JOINs IS NOT WORKING, Why?? IDK
