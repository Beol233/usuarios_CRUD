from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.usuario import Usuario


@app.route("/")
def inicio():
    return redirect("/usuarios")


@app.route("/usuarios")
def usuarios():
    lista_usuarios = Usuario.obtener_todos()
    return render_template("lista.html", usuarios=lista_usuarios)


@app.route("/usuarios/nuevo")
def nuevo():
    return render_template("nuevo.html")


@app.route("/usuarios/crear", methods=["POST"])
def crear():
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "correo": request.form["correo"],
        "contraseña": request.form["contraseña"]
    }

    Usuario.crear(data)
    return redirect("/usuarios")


@app.route("/usuarios/<int:id>")
def ver(id):
    usuario = Usuario.obtener_por_id(id)
    return render_template("ver.html", usuario=usuario)


@app.route("/usuarios/editar/<int:id>")
def editar(id):
    usuario = Usuario.obtener_por_id(id)
    return render_template("editar.html", usuario=usuario)


@app.route("/usuarios/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    data = {
        "id": id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "correo": request.form["correo"],
        "contraseña": request.form["contraseña"]
    }

    Usuario.actualizar(data)
    return redirect("/usuarios")


@app.route("/usuarios/eliminar/<int:id>")
def eliminar(id):
    Usuario.eliminar(id)
    return redirect("/usuarios")