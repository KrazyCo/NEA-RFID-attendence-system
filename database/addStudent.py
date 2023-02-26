from loadDatabase import loadDatabase
from sqlite3 import Error

def addStudent(name): # name is a string
    try:
        db = loadDatabase()
        c = db.cursor()
        c.execute(f'''INSERT INTO Students (StudentName, CurrentlyIn) VALUES ('{name}', False)''') # insert student name and currentlyIn into Students table - currentlyIn is False by default
        db.commit()
        db.close()
    except Error as e:
        print(e)

if __name__ == '__main__':
    addStudent('John')
    addStudent('Jane')
    addStudent('Jill')
    addStudent('Jack')