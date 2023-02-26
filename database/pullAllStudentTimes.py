from loadDatabase import loadDatabase
from sqlite3 import Error

def pullAllStudentTimes():
    try:
        db = loadDatabase()
        c = db.cursor()
        studentStatus = []
        c.execute('''SELECT Students.StudentID, StudentIn.CardID, Students.StudentName, StudentIn.Time, "In" FROM StudentIn JOIN StudentCards ON StudentIn.CardID = StudentCards.CardID JOIN Students ON StudentCards.StudentID = Students.StudentID''')
        studentIn = c.fetchall()
        studentStatus.append(studentIn)
        c.execute('''SELECT Students.StudentID, StudentOut.CardID, Students.StudentName, StudentOut.Time, "Out" FROM StudentOut JOIN StudentCards ON StudentOut.CardID = StudentCards.CardID JOIN Students ON StudentCards.StudentID = Students.StudentID''')
        studentOut = c.fetchall()
        studentStatus.append(studentOut)
        db.close()
    except Error as e:
        print(e)
    return studentStatus

if __name__ == '__main__':
    print(pullAllStudentTimes())