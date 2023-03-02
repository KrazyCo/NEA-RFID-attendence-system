from flask import Flask, render_template, request, redirect, url_for, flash

import sys
sys.path.insert(0, '../database')

from addStudent import addStudent
from addStudentCard import addStudentCard
from pullAllStudentStatus import pullAllStudentStatus
from pullAllStudentTimes import pullAllStudentTimes
from pullStudentStatus import pullStudentStatus
from pullStudentTimes import pullStudentTimes

app = Flask(__name__)

@app.route('/')
def index():
    students = pullAllStudentStatus()
    return render_template('index.html', students=students)

@app.route('/addStudent')
def addStudent():
    students = pullAllStudentStatus()
    return render_template('addStudent.html', students=students)

@app.route('/linkStudentCard')
def linkStudentCard():
    students = pullAllStudentStatus()
    return render_template('linkStudentCard.html', students=students)

@app.route('/seeStudents')
def seeStudents():
    students = pullAllStudentStatus()
    return render_template('seeStudents.html', students=students)

@app.route('/seeTimes')
def seeTimes():
    students = pullAllStudentStatus()
    return render_template('seeTimes.html', students=students)

@app.route('/rollcall')
def rollcall():
    students = pullAllStudentStatus()
    return render_template('rollcall.html', students=students)

if __name__ == '__main__':
    app.run()