from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__)  # En app se encuentra nuestro servidor web de Flask


# La barra (el slash) se conoce como la página de inicio (página home).
# Vamos a definir para esta ruta, el comportamiento a seguir.
@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all()  # Consultamos y almacenamos todas las tareas de la base de datos
    # Ahora en la variable todas_las_tareas se tienen almacenadas todas las tareas. Vamos a entregar esta variable al
    # template index.html
    return render_template("index.html", lista_de_tareas=todas_las_tareas)  # Se carga el template index.html


@app.route('/crear-tarea', methods=['POST'])
def crear():
    # tarea es un objeto de la clase Tarea (una instancia de la clase)
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecha=False)  # id no
    # es necesario asignarlo manualmente, porque la primary key se genera automaticamente
    db.session.add(tarea)  # Añadir el objeto de Tarea a la base de datos
    db.session.commit()  # Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('home')) # Esto nos redirecciona a la función home()


@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).delete() # Se busca
    # dentro de la base de datos, aquel registro cuyo id coincida con el aportado por
    # el parametro de la ruta. Cuando se encuentra se elimina
    db.session.commit() # Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('home')) # Esto nos redirecciona a la función home()
    # y si todo ha ido bien, al refrescar, la tarea eliminada ya no aparecera en el listado


@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first() # Se obtiene la
    # tarea que se busca
    tarea.hecha = not(tarea.hecha) # Guardamos en la variable booleana de la tarea, su contrario
    db.session.commit() # Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('home')) # Esto nos redirecciona a la función home()

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)  # Creamos el modelo de datos
    app.run(debug=True)  # El debug=True hace que cada vez que reiniciemos el
    # servidor o modifiquemos código, el servidor de Flask se reinicie solo