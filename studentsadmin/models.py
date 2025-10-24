from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "students"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    curso = db.Column(db.String(100))
    carrera = db.Column(db.String(100))
    facultad = db.Column(db.String(100))