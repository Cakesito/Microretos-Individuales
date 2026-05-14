from flask import Flask

app = Flask(__name__)

@app.route("/validar/<int:codigo>")
def validar(codigo):
    if codigo == 2008:
        return "<h1>Acceso concedido a Elio</h1>"
    
    return "<h1>Código erróneo</h1><p>Inténtelo de nuevo.</p>"

if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)