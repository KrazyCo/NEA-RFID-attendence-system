from loadDatabase import loadDatabase
from sqlite3 import Error

def pullStudentStatus(query):
    try:
        db = loadDatabase()
        c = db.cursor()
        if isinstance(query, str): # if query is a string
            c.execute(f'''SELECT StudentID, StudentName, CurrentlyIn FROM Students WHERE StudentName LIKE '{query}%' ''') # select all students in Students table where StudentName starts with query
        elif isinstance(query, int): # if query is an integer
            c.execute(f'''SELECT StudentID, StudentName, CurrentlyIn FROM Students WHERE StudentID = {query} ''') # select student in Students table where StudentID is query
        studentStatus = c.fetchall()
        db.close()
    except Error as e:
        print(e)
    return studentStatus

if __name__ == '__main__':
    print(f"{pullStudentStatus('Ch') = }")


    # print(f"{pullStudentStatus('Ja') = }")