from flask import Flask, Response, request, jsonify
import sqlite3


app = Flask(__name__)

"""
Autenticación Básica

Pregunta: Escriba una aplicación Flask que implemente autenticación básica utilizando un middleware. La aplicación debe tener una ruta protegida que solo pueda ser accesible después de autenticarse.
"""


def check_auth(username, password):
    username = "admin"
    password = "admin123"
    return username and password


def auth():
    return Response("Ingresa tus credenciales para continuar")


def requires_auth(func):
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return auth()
        return func(*args, **kwargs)
    return decorated


@app.route('/')
def public_route():
    return "Public page."


@app.route('/secret')
@requires_auth
def secret_route():
    return "Protected resource!"


"""
Consultas a Base de Datos

Pregunta: Escriba una ruta en Flask que acepte una solicitud GET con un parámetro de consulta 'user_id' y devuelva la información del usuario desde una base de datos SQLite.
"""


@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    if user_id is None:
        return jsonify({"error": "user_id is required"}), 400

    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({"error": "user_id must be an integer"}), 400

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cur.fetchone()
    conn.close()

    if user is None:
        return jsonify({"error": "User not found"}), 404

    user_info = {
        "id": user[0],
        "username": user[1],
        "email": user[2]
    }

    return jsonify(user_info)


if __name__ == "__main__":
    app.run(debug=True)
