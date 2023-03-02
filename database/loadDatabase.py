import sqlite3 # need full library to create the database connection
from sqlite3 import Error
from pathlib import Path # used to get the current directory

def loadDatabase():
    currDir = str(Path(__file__).parent.absolute()).replace("\\", "/") # Get the current directory
    try:
        conn = sqlite3.connect(currDir+'/studentDatabase.db') # Connect to the database
        c = conn.cursor() # Create a cursor to create tables if needed
    except Error as e:
        print(e)
        return None # Return None if there is an error, after printing the error
    
    c.execute('''CREATE TABLE IF NOT EXISTS Students (StudentID INTEGER PRIMARY KEY, StudentName TEXT NOT NULL, CurrentlyIn BOOLEAN)''') # Create the Students table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS StudentIn (InID INTEGER PRIMARY KEY, CardID TEXT NOT NULL, Time INTEGER NOT NULL)''') # Create the StudentIn table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS StudentOut (OutID INTEGER PRIMARY KEY, CardID TEXT NOT NULL, Time INTEGER NOT NULL)''') # Create the StudentOut table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS StudentCards (CardID TEXT PRIMARY KEY, StudentID INTEGER NOT NULL)''') # Create the StudentCards table if it doesn't exist
    return conn # Return the connection to the database so the rest of the program can edit the database

if __name__ == '__main__':
    db = loadDatabase()
    db.close()


    # try:
    #     c.execute('''INSERT INTO Students (StudentName, CurrentlyIn) VALUES ('John', False)''')
    #     c.execute('''INSERT INTO StudentIn (CardID, Time) VALUES ('06und48', 123456789)''')
    #     c.execute('''INSERT INTO StudentOut (CardID, Time) VALUES ('06und481', 12345766789)''')
    #     c.execute('''INSERT INTO StudentCards (CardID, StudentID) VALUES ('ab3s459s', 1)''')
    # except Error as e:
    #     print(e)
# c = db.cursor()
# c.execute('''INSERT INTO Students (StudentName, CurrentlyIn) VALUES ('John', True)''')
# # c.execute('''INSERT INTO StudentIn (CardID, Time) VALUES ('06und48', 123456789)''')
# # c.execute('''INSERT INTO StudentOut (CardID, Time) VALUES ('06und481', 12345766789)''')
# # c.execute('''INSERT INTO StudentCards (CardID, StudentID) VALUES ('ab3s459s', 1)''')