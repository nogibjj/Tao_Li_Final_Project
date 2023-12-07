import sqlite3
import csv
import os

def load(dataset="movie.csv"):
    '''Transform and load the data into local SQLite3 database'''
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("MovieDB.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS MovieDB")
    cursor.execute("CREATE TABLE GroceryDB (Movie_Title, Year, Director, Actors, Rating, Runtime(Mins), Censor, Total_Gross, main_genre, side_genre)")
    cursor.executemany("INSERT INTO GroceryDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?)", payload)

    conn.commit()
    conn.close()

    return "MovieDB.db"