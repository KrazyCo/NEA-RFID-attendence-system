from loadDatabase import loadDatabase
from sqlite3 import Error

def logStudentAction(cardID, time, action):
    try:
        db = loadDatabase()
        c = db.cursor()
        if action == 'In':
            c.execute(f'''INSERT INTO StudentIn (CardID, Time) VALUES ('{cardID}', {time})''')
            c.execute(f'''UPDATE Students SET CurrentlyIn = True WHERE StudentID = (SELECT StudentID FROM StudentCards WHERE CardID = '{cardID}')''')
        
        elif action == 'Out':
            c.execute(f'''INSERT INTO StudentOut (CardID, Time) VALUES ('{cardID}', {time})''')
            c.execute(f'''UPDATE Students SET CurrentlyIn = False WHERE StudentID = (SELECT StudentID FROM StudentCards WHERE CardID = '{cardID}')''')
        db.commit()
        db.close()
    except Error as e:
        print(e)
    

if __name__ == '__main__':
    logStudentAction('06und48', 123456789, 'In')
    logStudentAction('06u0d48', 123456789, 'Out')
    logStudentAction('06u1d48', 111122221, 'In')
    logStudentAction('06u2d48', 111122221, 'Out')