from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.usuario import Usuario

@app.route("/")
def inicio():
    return redirect("/usuarios")

@app.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.obtener_todos()
    return render_template("lista.html", usuarios=usuarios)

@app.route("/usuarios/nuevo")
def formulario_nuevo():
    return render_template("nuevo.html")

@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    datos = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.crear(datos)
    return redirect("/usuarios")

@app.route("/usuarios/<int:id>")
def ver_usuario(id):
    usuario = Usuario.obtener_por_id(id)
    return render_template("ver.html", usuario=usuario)

@app.route("/usuarios/editar/<int:id>")
def formulario_editar(id):
    usuario = Usuario.obtener_por_id(id)
    return render_template("editar.html", usuario=usuario)

@app.route("/usuarios/actualizar/<int:id>", methods=["POST"])
def actualizar_usuario(id):
    datos = {
        "id": id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.actualizar(datos)
    return redirect("/usuarios")

@app.route("/usuarios/eliminar/<int:id>")
def eliminar_usuario(id):
    Usuario.eliminar(id)
    return redirect("/usuarios")