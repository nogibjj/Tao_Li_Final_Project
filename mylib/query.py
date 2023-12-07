import sqlite3
from prettytable import PrettyTable

def Query1(main_genre):
    '''Query the top 5 rows of the GroceryDB table'''
    conn = sqlite3.connect("MovieDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Movie_Title, Year, Director, Rating, main_genre FROM MovieDB WHERE main_genre='{main_genre}'")

    column_names = ["Movie Title", "Year", "Director", "Rating", "main_genre"]

    table = PrettyTable(column_names) # initialize table with column names

    for row in cursor.fetchall():
        table.add_row(row) # fetch rows and add them to the table

    print(table)

    conn.close()

    return "Success"