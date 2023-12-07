from mylib.extract import extract
from mylib.query import Query1, Query2
from mylib.transform_load import load

print("Extracting data...")
extract()

print("Loading data...")
load()

print("Querying data...")
Query1()
print()
Query2()
print()