import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from dotenv import load_dotenv
from models import db, Student

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = "clave_super_secreta"
    
    # Configuración de la base de datos MySQL usando variables de entorno
    user = os.getenv("DB_USER")
    pwd = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    name = os.getenv("DB_NAME")
    
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{user}:{pwd}@{host}/{name}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Inicializar SQLAlchemy con la app
    db.init_app(app)
    
    # Crear todas las tablas
    with app.app_context():
        db.create_all()
    
    # 🔹 Ruta principal (index)
    @app.route('/')
    def index():
        mostrar_tabla = session.get('mostrar_tabla', False)
        estudiantes = Student.query.order_by(Student.id).all()
        return render_template('index.html', estudiantes=estudiantes, mostrar_tabla=mostrar_tabla)
    
    # 🔹 Ruta para agregar estudiante
    @app.route('/agregar', methods=['GET', 'POST'])
    def agregar():
        if request.method == 'POST':
            nombre = request.form['nombre']
            edad = request.form['edad']
            curso = request.form['curso']
            carrera = request.form['carrera']
            facultad = request.form['facultad']
            
            try:
                nuevo_estudiante = Student(
                    nombre=nombre,
                    edad=edad,
                    curso=curso,
                    carrera=carrera,
                    facultad=facultad
                )
                db.session.add(nuevo_estudiante)
                db.session.commit()
                flash("Estudiante agregado exitosamente", "success")
                session['mostrar_tabla'] = True
                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                flash(f"Error al agregar estudiante: {e}", "error")
                return redirect(url_for('agregar'))
        
        return render_template('agregar.html')
    
    # 🔹 Ruta para editar estudiante
    @app.route('/editar/<int:id>', methods=['GET', 'POST'])
    def editar(id):
        estudiante = Student.query.get_or_404(id)
        
        if request.method == 'POST':
            try:
                estudiante.nombre = request.form['nombre']
                estudiante.edad = request.form['edad']
                estudiante.curso = request.form['curso']
                estudiante.carrera = request.form['carrera']
                estudiante.facultad = request.form['facultad']
                
                db.session.commit()
                flash("Estudiante actualizado exitosamente", "success")
                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                flash(f"Error al actualizar estudiante: {e}", "error")
        
        return render_template('editar.html', estudiante=estudiante)
    
    # 🔹 Ruta para eliminar estudiante
    @app.route('/eliminar/<int:id>')
    def eliminar(id):
        try:
            estudiante = Student.query.get_or_404(id)
            db.session.delete(estudiante)
            db.session.commit()
            flash("Estudiante eliminado exitosamente", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error al eliminar estudiante: {e}", "error")
        
        return redirect(url_for('index'))
    
    # 🔹 Ruta para salir
    @app.route('/salir', methods=['POST'])
    def salir():
        session.pop('mostrar_tabla', None)
        return redirect(url_for('index'))
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)