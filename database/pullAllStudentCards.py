from loadDatabase import loadDatabase
from sqlite3 import Error

def pullAllStudentCards():
    try:
        db = loadDatabase()
        c = db.cursor()
        c.execute('''SELECT StudentCards.CardID, StudentCards.StudentID, Students.StudentName FROM StudentCards JOIN Students ON StudentCards.StudentID = Students.StudentID''')
        # select all records from StudentCards table and join with Students table to get StudentName
        studentCards = c.fetchall()
        db.close()
    except Error as e:
        print(e)
    return studentCards # returns 2 dimensional list

if __name__ == '__main__':
    print(pullAllStudentCards())