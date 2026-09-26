from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

def conectar():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root", 
        database="usuarios_crud"
    )

@app.route('/')
def index():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()
    conn.close()
    return render_template('index.html', usuarios=usuarios)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido'] 
        email = request.form['email']
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuario (nombre, apellido, email) VALUES (%s, %s, %s)",
            (nombre, apellido, email)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('crear.html')

@app.route('/ver/<id>')
def ver(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE id=%s", (id,))
    usuario = cursor.fetchone()
    conn.close()

    return render_template('ver.html', usuario=usuario)

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):
    conn = conectar()
    cursor = conn.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']  
        email = request.form['email']
        cursor.execute(
            "UPDATE usuario SET nombre=%s, apellido=%s, email=%s WHERE id=%s",
            (nombre, apellido, email, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM usuario WHERE id=%s", (id,))
    usuario = cursor.fetchone()
    conn.close()
    return render_template('editar.html', usuario=usuario)

@app.route('/eliminar/<id>')
def eliminar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuario WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)