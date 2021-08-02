import sqlite3
from nltk import load_parser, load
from db_creation import DbCreation

# Initialize DbCreation object to create db for the first time
db = DbCreation()
db.execute_sql_script("knowledge_base.sql")

# Load our semanctics file
print("Loading grammar..\n")
grammar = load("semantics.fcfg")
cemantics_parser = load_parser("semantics.fcfg")

# query = "who love book"
input_query = str(input("Examples of questions you can make to the NLP: 'who loves books', 'who gave dog', 'who hates cat'..\nEnter tour question: "))
trees = list(cemantics_parser.parse(input_query.split()))
answer = trees[0].label()["SEM"]
answer = [s for s in answer if s]
q = " ".join(answer)

sqliteConnection = sqlite3.connect("knowledge_base.db")
cursor = sqliteConnection.cursor()
cursor.execute(q + ";")
records = cursor.fetchall()
for row in records:
    print(row[0])

sqliteConnection.close()