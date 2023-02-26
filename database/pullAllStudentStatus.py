from loadDatabase import loadDatabase
from sqlite3 import Error

def pullAllStudentStatus():
    try:
        db = loadDatabase()
        c = db.cursor()
        c.execute('''SELECT StudentID, StudentName, CurrentlyIn FROM Students''') # select all students in Students table
        studentStatus = c.fetchall() # fetch all students in Students table into 2D list
        db.close()
    except Error as e:
        print(e)
    return studentStatus # return 2D list of all students in Students table

if __name__ == '__main__':
    print(pullAllStudentStatus())