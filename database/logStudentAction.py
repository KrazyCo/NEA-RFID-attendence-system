from loadDatabase import loadDatabase # loads the loadDatabase function
from sqlite3 import Error # file doesn't need the full sqlite3 library, just the Error class, as db objects are created in loadDatabase

def logStudentAction(cardID, time, action): # cardID is a string, time is an int, action is a string
    try: # stops program from crashing if there is an error, and prints a nice error message instead
        db = loadDatabase() # loads the database
        c = db.cursor() # creates a cursor object to execute SQL commands
        if action == 'In':
            c.execute(f'''INSERT INTO StudentIn (CardID, Time) VALUES ('{cardID}', {time})''') # inserts the cardID and time into the StudentIn table
            c.execute(f'''UPDATE Students SET CurrentlyIn = True WHERE StudentID = (SELECT StudentID FROM StudentCards WHERE CardID = '{cardID}')''') # updates the CurrentlyIn column in the Students table to True if there is a linked student
        
        elif action == 'Out':
            c.execute(f'''INSERT INTO StudentOut (CardID, Time) VALUES ('{cardID}', {time})''') # inserts the cardID and time into the StudentOut table
            c.execute(f'''UPDATE Students SET CurrentlyIn = False WHERE StudentID = (SELECT StudentID FROM StudentCards WHERE CardID = '{cardID}')''') # updates the CurrentlyIn column in the Students table to False if there is a linked student
        db.commit() # commits the changes to the database
        db.close() # closes the database
    except Error as e: # catches the error and prints it to the console
        print(e)
    

if __name__ == '__main__':
    # logStudentAction('72 17 4C 26', 1672743971, 'In')

    logStudentAction('72 17 4C 26', 123456789, 'In')
    logStudentAction('72 17 4C 26', 123456789, 'Out')
    logStudentAction('28 17 4C 26', 111122221, 'In')
    logStudentAction('28 17 4C 26', 111122221, 'Out')
    logStudentAction('93 17 4C 26', 111122221, 'In')
    logStudentAction('93 17 4C 26', 111122221, 'Out')