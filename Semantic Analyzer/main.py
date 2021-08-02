import sqlite3
from nltk import load_parser, load
from db_creation import DbCreation

# Initialize DbCreation object to create db for the first time
db = DbCreation()
db.execute_sql_script("knowledge_base.sql")

# Load our semanctics file
grammar = load("semantics.fcfg")
cemantics_parser = load_parser("semantics.fcfg")

query = 'who loves book'
trees = list(cemantics_parser.parse(query.split()))
answer = trees[0].label()["SEM"]
answer = [s for s in answer if s]
q = " ".join(answer)
print(q)

sqliteConnection = sqlite3.connect("knowledge_base")
cursor = sqliteConnection.cursor()
records = cursor.fetchall()
for row in records:
    print(row[0])

sqliteConnection.close()