# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    # Buscamos el archivo 'perfil_2_3_2.html' dentro de la carpeta /templates
    return render_template("perfil_2_3_2.html", estudiante="Elio", nickname="777", id_dev=7582)


if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)