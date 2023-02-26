from loadDatabase import loadDatabase
from sqlite3 import Error

def addStudent(name):
    try:
        db = loadDatabase()
        c = db.cursor()
        c.execute(f'''INSERT INTO Students (StudentName, CurrentlyIn) VALUES ('{name}', False)''')
        c.execute(f'''SELECT StudentID FROM Students WHERE StudentName = '{name}' ''')
        studentID = c.fetchone()[0]
        db.commit()
        db.close()
    except Error as e:
        print(e)
    return studentID

if __name__ == '__main__':
    print(f"{addStudent('James') = }")
    print(f"{addStudent('John') = }")
    print(f"{addStudent('Jane') = }")
    print(f"{addStudent('Jill') = }")