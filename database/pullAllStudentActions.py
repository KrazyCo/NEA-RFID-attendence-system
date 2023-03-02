from loadDatabase import loadDatabase
from sqlite3 import Error

def pullAllStudentActions():
    try:
        db = loadDatabase()
        c = db.cursor()
        c.execute('''SELECT StudentIn.CardID, StudentIn.Time, "In" FROM StudentIn''')
        studentIn = c.fetchall()
        c.execute('''SELECT StudentOut.CardID, StudentOut.Time, "Out" FROM StudentOut''')
        studentOut = c.fetchall()
        studentActions = studentIn + studentOut
        db.close()
    except Error as e:
        print(e)
    return studentActions 

if __name__ == '__main__':
    print(pullAllStudentActions())