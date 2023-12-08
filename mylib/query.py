import sqlite3
from prettytable import PrettyTable

def create_db():
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS GroceryDB
                      (general_name INTEGER PRIMARY KEY,
                      count_products INTEGER,
                      ingred_FPro FLOAT,
                      avg_FPro_products FLOAT,
                      avg_distance_root FLOAT,
                      ingred_normalization_term	FLOAT,
                      semantic_tree_name CHAR,
                      semantic_tree_node CHAR)"""
    )
    conn.commit()
    return "Successfully created table!"

def read_db():
    '''Query the top 5 rows of the GroceryDB table'''
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB")

    column_names = [description[0] for description in cursor.description]

    table = PrettyTable(column_names) # initialize table with column names

    for row in cursor.fetchall():
        table.add_row(row) # fetch rows and add them to the table

    print(table)

    conn.close()

    return "Success"

def Query1():
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM GroceryDB WHERE general_name LIKE '%coffee%'")

    column_names = [description[0] for description in cursor.description]

    table = PrettyTable(column_names) # initialize table with column names

    for row in cursor.fetchall():
        table.add_row(row) # fetch rows and add them to the table

    print(table)

    conn.close()

    return "Success"


def Query2(thresh):
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT general_name FROM GroceryDB WHERE count_products>{thresh}")

    column_names = [description[0] for description in cursor.description]

    table = PrettyTable(column_names) # initialize table with column names

    for row in cursor.fetchall():
        table.add_row(row) # fetch rows and add them to the table

    print(table)

    conn.close()

    return "Success"