from nltk import load_parser, load
import sqlite3

# Load our semanctics file
grammar = load('semantics.fcfg')

# show_cfg('semanctics.fcfg')
cemantics_parser = load_parser('semantics.fcfg')

query = 'who loves book'
trees = list(cemantics_parser.parse(query.split()))

answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)

sqliteConnection = sqlite3.connect('knowledge_db')
cursor = sqliteConnection.cursor()
cursor.execute(q + ";")
records = cursor.fetchall()
for row in records:
    print(row[0])

sqliteConnection.close()