import pymysql
from flask_app.config.myconnection import get_connection

class Usuario:
    def __init__(self, datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.email = datos["email"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]

    @classmethod
    def obtener_todos(cls):
        conexion = get_connection()
        with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM usuarios;")
            resultados = cursor.fetchall()
        conexion.close()
        return [cls(fila) for fila in resultados]
    
    @classmethod
    def crear(cls, datos):
        conexion = get_connection()
        query = """
            INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        with conexion.cursor() as cursor:
            cursor.execute(query, datos)
            conexion.commit()
            ultimo_id = cursor.lastrowid
        conexion.close()
        return ultimo_id 
    
    @classmethod
    def obtener_por_id(cls, id):
        conexion = get_connection()
        with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE id = %s;", (id,))
            resultado = cursor.fetchone()
        conexion.close()
        return cls(resultado) if resultado else None

    @classmethod
    def actualizar(cls, datos):
        conexion = get_connection()
        query = """
            UPDATE usuarios
            SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s,
                updated_at = NOW()
            WHERE id = %(id)s;
        """
        with conexion.cursor() as cursor:
            cursor.execute(query, datos)
            conexion.commit()
        conexion.close()

    @classmethod
    def eliminar(cls, id):
        conexion = get_connection()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM usuarios WHERE id = %s;", (id,))
            conexion.commit()
        conexion.close()