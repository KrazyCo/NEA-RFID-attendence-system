from loadDatabase import loadDatabase
from sqlite3 import Error

def pullAllStudentStatus():
    try:
        db = loadDatabase()
        c = db.cursor()
        c.execute('''SELECT StudentID, StudentName, CurrentlyIn FROM Students''')
        studentStatus = c.fetchall()
        db.close()
    except Error as e:
        print(e)
    return studentStatus

if __name__ == '__main__':
    print(pullAllStudentStatus())