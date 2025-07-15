import duckdb

db = duckdb.connect()

print(db.sql('select now()'))
