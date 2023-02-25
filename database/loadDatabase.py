import sqlite3
from sqlite3 import Error
from pathlib import Path

# find current dir for file stuff


def loadDatabase():
    currDir = str(Path(__file__).parent.absolute()).replace("\\", "/")
    try:
        conn = sqlite3.connect(currDir+'/studentDatabase.db')
        c = conn.cursor()
    except Error as e:
        print(e)
        return None
    
    c.execute('''CREATE TABLE IF NOT EXISTS Students (StudentID INTEGER PRIMARY KEY, StudentName TEXT NOT NULL, CurrentlyIn BOOLEAN)''')
    c.execute('''CREATE TABLE IF NOT EXISTS StudentIn (InID INTEGER PRIMARY KEY, CardID TEXT NOT NULL, Time INTEGER NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS StudentOut (OutID INTEGER PRIMARY KEY, CardID TEXT NOT NULL, Time INTEGER NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS StudentCards (CardID TEXT PRIMARY KEY, StudentID INTEGER NOT NULL)''')
    return conn

if __name__ == '__main__':
    db = loadDatabase()
    c = db.cursor()
    try:
        c.execute('''INSERT INTO Students (StudentName, CurrentlyIn) VALUES ('John', False)''')
        c.execute('''INSERT INTO StudentIn (CardID, Time) VALUES ('06und48', 123456789)''')
        c.execute('''INSERT INTO StudentOut (CardID, Time) VALUES ('06und481', 12345766789)''')
        c.execute('''INSERT INTO StudentCards (CardID, StudentID) VALUES ('ab3s459s', 1)''')
    except Error as e:
        print(e)
    db.commit()
    db.close()


# c = db.cursor()
# c.execute('''INSERT INTO Students (StudentName, CurrentlyIn) VALUES ('John', True)''')
# # c.execute('''INSERT INTO StudentIn (CardID, Time) VALUES ('06und48', 123456789)''')
# # c.execute('''INSERT INTO StudentOut (CardID, Time) VALUES ('06und481', 12345766789)''')
# # c.execute('''INSERT INTO StudentCards (CardID, StudentID) VALUES ('ab3s459s', 1)''')