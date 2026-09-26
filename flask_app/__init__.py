from flask import Flask

app = Flask(__name__)
app.secret_key = "clave_secreta"

from flask_app.controllers import usuarios