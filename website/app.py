from flask import Flask, render_template, request, redirect, url_for, flash

import datetime

import sys
sys.path.insert(0, '../database')

from addStudent import addStudent as addStudentDb
from addStudentCard import addStudentCard
from pullAllStudentStatus import pullAllStudentStatus
from pullAllStudentTimes import pullAllStudentTimes
from pullAllStudentCards import pullAllStudentCards
from pullAllStudentActions import pullAllStudentActions
from pullStudentStatus import pullStudentStatus
from pullStudentTimes import pullStudentTimes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeathisisasecretkeyanditsverysecure'

def getReadableTime(time):
    return datetime.datetime.utcfromtimestamp(time).strftime('%H:%M:%S %d-%m-%Y')

@app.route('/')
def index():
    students = pullAllStudentStatus()
    totalStudents = len(students)
    studentsIn = 0
    for student in students:
        if student[2] == 1:
            studentsIn += 1
    return render_template('index.html', students=students, totalStudents=totalStudents, studentsIn=studentsIn)

@app.route('/addStudent', methods=('GET', 'POST'))
def addStudent():
    if request.method == 'POST':
        studentName = request.form['studentName']
        if not studentName:
            flash('Please enter a student name.')
        else:
            addStudentDb(studentName)
    students = pullAllStudentStatus()
    students.reverse()
    return render_template('addStudent.html', students=students)

@app.route('/linkStudentCard', methods=('GET', 'POST'))
def linkStudentCard():
    if request.method == 'POST':
        cardID = request.form['cardID']
        studentID = request.form['studentID']
        if not cardID or not studentID:
            flash('Please enter cardID and studentID.')
        elif not studentID.isnumeric():
            flash('Please enter a valid studentID.')
        elif len(cardID) != 11:
            flash('Please enter a valid cardID.')
        else:
            addStudentCard(cardID, studentID)
    cards = pullAllStudentCards()
    actions = pullAllStudentActions()
    actions.sort(key=lambda x: x[1], reverse=True)
    generatedActions = []
    for action in actions:
        generatedActions.append([action[0], getReadableTime(action[1]), action[2]])
    return render_template('linkStudentCard.html', cards=cards, actions=generatedActions)

@app.route('/seeStudents', methods=('GET', 'POST'))
def seeStudents():
    if request.method == 'POST':
        studentName = request.form['studentName']
        if not studentName:
            students = pullAllStudentStatus()
            return render_template('seeStudents.html', students=students)
        else:
            students = pullStudentStatus(studentName)
            return render_template('seeStudents.html', students=students)
    students = pullAllStudentStatus()
    return render_template('seeStudents.html', students=students)

@app.route('/seeTimes', methods=('GET', 'POST'))
def seeTimes():
    if request.method == 'POST':
        studentID = request.form['studentID']
        if not studentID.isnumeric():
            flash('Please enter a valid studentID.')
            times = pullAllStudentTimes()
        elif studentID:
            times = pullStudentTimes(studentID)
        else:
            times = pullAllStudentTimes()
    else:
        times = pullAllStudentTimes()
    generatedTimes = []
    for type in times:
        tempTimes = []
        for time in type:
            tempTimes.append([time[0], time[1], time[2], getReadableTime(time[3])])
        generatedTimes.append(tempTimes)
    return render_template('seeTimes.html', times=generatedTimes)

@app.route('/rollcall')
def rollcall():
    students = pullAllStudentStatus()
    return render_template('rollcall.html', students=students)

if __name__ == '__main__':
    app.run(host="0.0.0.0")