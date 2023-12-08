import sqlite3
import csv
import os

def load(dataset="GroceryDB_IgFPro.csv"):
    '''Transform and load the data into local SQLite3 database'''
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS GroceryDB")
    cursor.execute("CREATE TABLE GroceryDB (id,general_name, count_products, ingred_FPro, avg_FPro_products, avg_distance_root, ingred_normalization_term, semantic_tree_name, semantic_tree_node)")
    cursor.executemany("INSERT INTO GroceryDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)

    conn.commit()
    conn.close()

    return "GroceryDB.db"