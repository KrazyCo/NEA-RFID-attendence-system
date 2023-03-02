from loadDatabase import loadDatabase
from sqlite3 import Error

def pullAllStudentActions():
    try:
        db = loadDatabase()
        c = db.cursor()
        c.execute('''SELECT StudentIn.CardID, StudentIn.Time, "In" FROM StudentIn''') # no linking records used
        studentIn = c.fetchall()
        c.execute('''SELECT StudentOut.CardID, StudentOut.Time, "Out" FROM StudentOut''') # no linking records used
        studentOut = c.fetchall()
        studentActions = studentIn + studentOut # only need 2 dimensional list
        db.close()
    except Error as e:
        print(e)
    return studentActions 

if __name__ == '__main__':
    print(pullAllStudentActions())