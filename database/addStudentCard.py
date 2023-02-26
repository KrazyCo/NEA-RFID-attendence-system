from loadDatabase import loadDatabase
from sqlite3 import Error

def addStudentCard(cardID, studentID):
    try:
        db = loadDatabase()
        c = db.cursor()
        c.execute(f'''INSERT INTO StudentCards (CardID, StudentID) VALUES ('{cardID}', {studentID})''')
        db.commit()
        db.close()
    except Error as e:
        print(e)

if __name__ == '__main__':
    addStudentCard('72 17 4C 26', 1)
    addStudentCard('28 17 4C 26', 2)


    # addStudentCard('ab3s479s', 2)
    # addStudentCard('ab3s489s', 3)
    # addStudentCard('ab3s499s', 4)