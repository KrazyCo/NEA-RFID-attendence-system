from loadDatabase import loadDatabase
from sqlite3 import Error

def pullStudentStatus(query):
    try:
        db = loadDatabase()
        c = db.cursor()
        if isinstance(query, str):
            c.execute(f'''SELECT StudentID, StudentName, CurrentlyIn FROM Students WHERE StudentName LIKE '%{query}%' ''')
        elif isinstance(query, int):
            c.execute(f'''SELECT StudentID, StudentName, CurrentlyIn FROM Students WHERE StudentID = {query} ''')
        studentStatus = c.fetchall()
        db.close()
    except Error as e:
        print(e)
    return studentStatus

if __name__ == '__main__':
    print(f"{pullStudentStatus('J') = }")
    print(f"{pullStudentStatus(1) = }")