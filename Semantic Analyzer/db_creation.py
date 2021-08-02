import sqlite3

class DbCreation():

    # Function that reads SQL queries from a file
    def execute_sql_script(self, sql_filename: str):
        
        connection = sqlite3.connect('knowledge_base.db')
        # Open & read the file as a single buffer
        file = open(sql_filename, "r")
        sql_file = file.read()
        file.close()

        # Add diffrent commands in a list. All SQL commands split on ';'
        sql_queries = sql_file.split(";")
        
        # Execute
        for query in sql_queries:
            try:
                connection.executescript(query)
            except sqlite3.OperationalError as err:
                print("Command of creating db skipped: {}\n".format(err))