from loadDatabase import loadDatabase
from sqlite3 import Error

def pullAllStudentTimes():
    try:
        db = loadDatabase()
        c = db.cursor()
        studentStatus = []
        c.execute('''SELECT Students.StudentID, StudentIn.CardID, Students.StudentName, StudentIn.Time, "In" FROM StudentIn JOIN StudentCards ON StudentIn.CardID = StudentCards.CardID JOIN Students ON StudentCards.StudentID = Students.StudentID''')
        # get student ID, card ID, student name, time, and "In" from StudentIn table, linking through StudentCards table to the Students table for names and studentID
        studentIn = c.fetchall()
        studentStatus.append(studentIn) # append 2D list of studentIn to studentStatus to create 3D list
        c.execute('''SELECT Students.StudentID, StudentOut.CardID, Students.StudentName, StudentOut.Time, "Out" FROM StudentOut JOIN StudentCards ON StudentOut.CardID = StudentCards.CardID JOIN Students ON StudentCards.StudentID = Students.StudentID''')
        # get student ID, card ID, student name, time, and "Out" from StudentOut table, linking through StudentCards table to the Students table for names and studentID
        studentOut = c.fetchall()
        studentStatus.append(studentOut) # append 2D list of studentOut to studentStatus to create new index in 3D list
        db.close()
    except Error as e:
        print(e)
    return studentStatus # return 3D list of all entries in both StudentIn and StudentOut tables

if __name__ == '__main__':
    print(pullAllStudentTimes())