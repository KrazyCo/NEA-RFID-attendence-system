from loadDatabase import loadDatabase
from sqlite3 import Error

def pullStudentTimes(studentID):
    try:
        db = loadDatabase()
        c = db.cursor()
        studentStatus = []
        c.execute(f'''SELECT Students.StudentID, StudentIn.CardID, Students.StudentName, StudentIn.Time, "In" FROM StudentIn JOIN StudentCards ON StudentIn.CardID = StudentCards.CardID JOIN Students ON StudentCards.StudentID = Students.StudentID WHERE Students.StudentID = {studentID}''')
        # get student ID, card ID, student name, time, and "In" from StudentIn table for every record that links to given StudentID, linking through StudentCards table to the Students table for names and studentID
        studentIn = c.fetchall()
        studentStatus.append(studentIn)
        c.execute(f'''SELECT Students.StudentID, StudentOut.CardID, Students.StudentName, StudentOut.Time, "Out" FROM StudentOut JOIN StudentCards ON StudentOut.CardID = StudentCards.CardID JOIN Students ON StudentCards.StudentID = Students.StudentID WHERE Students.StudentID = {studentID}''')
        # get student ID, card ID, student name, time, and "Out" from StudentOut table for every record that links to given StudentID, linking through StudentCards table to the Students table for names and studentID
        studentOut = c.fetchall()
        studentStatus.append(studentOut)
        db.close()
    except Error as e:
        print(e)
    return studentStatus

if __name__ == '__main__':
    print(pullStudentTimes(1))




    # print(pullStudentTimes(0))