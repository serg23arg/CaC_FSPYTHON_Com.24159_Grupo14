from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')
app = Flask(__name__, template_folder = template_dir)

@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM form_contacto")
    miResultado = cursor.fetchall()

    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]

    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))

    cursor.close()

    return render_template('index.html', data=insertarObjectos)

@app.route('/mensaje', methods=['POST'])
def agregarMensaje():
    fecha = request.form['fecha']
    motivo = request.form['motivo']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    whatsapp = request.form['whatsapp']
    mensaje = request.form['mensaje']
    adjunto = request.form['adjunto']
    tc = request.form['tc']

    if fecha and motivo and nombre and apellido and email and whatsapp and mensaje and adjunto and tc:
        cursor = db.database.cursor()
        sql = "INSERT INTO form_contacto (Fecha, Motivo, Nombre, Apellido, E_mail, Whatsapp, Mensaje, Adjunto, TC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (fecha, motivo, nombre, apellido, email, whatsapp, mensaje, adjunto, tc)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/borrar/<string:id>')
def borrar(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM form_contacto WHERE Id = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))


@app.route('/editar/<string:id>', methods=['POST'])
def edit(id):
    fecha = request.form['fecha']
    motivo = request.form['motivo']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    whatsapp = request.form['whatsapp']
    mensaje = request.form['mensaje']
    adjunto = request.form['adjunto']
    tc = request.form['tc']
    observaciones = request.form['observaciones']

    if fecha and motivo and nombre and apellido and email and whatsapp and mensaje and adjunto and tc and observaciones:
        cursor = db.database.cursor()
        sql = "UPDATE form_contacto SET Fecha = %s, Motivo = %s, Nombre = %s, Apellido = %s, E_mail = %s, Whatsapp = %s, Mensaje = %s, Adjunto = %s, TC = %s,  Observaciones = %s WHERE Id = %s"
        data = (fecha, motivo, nombre, apellido, email, whatsapp, mensaje, adjunto, tc, observaciones, id,)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)
