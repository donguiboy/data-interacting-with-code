# pylint: disable=missing-docstring, C0103
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()
rows = db.fetchall()

def directors_count(db): #DONE
    query = "SELECT COUNT(id) FROM directors"
    db.execute(query)
    results = db.fetchall()
    for row in results:
        return row[0]

def directors_list(db): #incomplete
    # return the list of all the directors sorted in alphabetical order
    query= "SELECT name FROM directors ORDER BY name ASC"
    db.execute(query)
    results = db.fetchall()
    names =[]
    for row in results:
        names.append(row[0])
    return names

def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query= """SELECT title FROM movies m
    WHERE UPPER(m.title) like "%LOVE'%" OR
    UPPER(m.title) like "%LOVE %" OR
    UPPER(m.title) like "% LOVE" OR
    UPPER(m.title) like "%LOVE." OR
    UPPER(m.title) like "%LOVE,%" OR
    UPPER(m.title) like "LOVE"
    ORDER BY title"""

    db.execute(query)
    results = db.fetchall()
    names =[]
    for row in results:
        names.append(row[0])
    return names

def directors_named_like_count(db, name): #DONE
    # return the number of directors which contain a given word in their name
    query = f'SELECT COUNT(name) FROM directors WHERE Upper(name) LIKE "%{name}%"'
    db.execute(query)
    results = db.fetchall()
    for row in results:
        return row[0]

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = f'SELECT title, minutes FROM movies WHERE minutes >= {int(min_length)} ORDER BY title ASC'
    db.execute(query)
    results = db.fetchall()
    names = []
    for row in results:
        names.append(row[0])
    return names
