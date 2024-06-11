from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learning_platform.db'
db = SQLAlchemy(app)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teachers', methods=['GET', 'POST'])
def teachers():
    if request.method == 'GET':
        teachers = Teacher.query.all()
        return jsonify([{'id': teacher.id, 'name': teacher.name} for teacher in teachers])
    elif request.method == 'POST':
        data = request.json
        new_teacher = Teacher(name=data['name'])
        db.session.add(new_teacher)
        db.session.commit()
        return jsonify({'message': 'Teacher created successfully'})

@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'GET':
        students = Student.query.all()
        return jsonify([{'id': student.id, 'name': student.name} for student in students])
    elif request.method == 'POST':
        data = request.json
        new_student = Student(name=data['name'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Student created successfully'})

if __name__ == '__main__':
    app.run(debug=True)
