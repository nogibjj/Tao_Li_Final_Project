import sqlite3
import json

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

def read_db(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB LIMIT 5")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print("Table read")
    return "Success"

def Query1(grocery, json_str=True):
    conn = sqlite3.connect("GroceryDB.db")
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    cursor = conn.cursor()
    rows = cursor.execute(f"SELECT * FROM GroceryDB WHERE general_name LIKE '%{grocery}%'").fetchall()

    # column_names = [description[0] for description in cursor.description]

    # table = PrettyTable(column_names) # initialize table with column names

    # for row in cursor.fetchall():
    #     table.add_row(row) # fetch rows and add them to the table

    # print(table)

    for row in rows:
        print(row)
    print("rows retrieved, success!")

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps([dict(ix) for ix in rows]) # create JSON

def Query2(count, son_str=True):
    conn = sqlite3.connect("GroceryDB.db")
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    cursor = conn.cursor()
    rows = cursor.execute(f"SELECT general_name FROM GroceryDB WHERE count_products>{count}").fetchall()

    # column_names = [description[0] for description in cursor.description]

    # table = PrettyTable(column_names) # initialize table with column names

    # for row in cursor.fetchall():
    #     table.add_row(row) # fetch rows and add them to the table

    # print(table)

    for row in rows:
        print(row)
    print("rows retrieved, success!")

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps([dict(ix) for ix in rows]) # create JSON