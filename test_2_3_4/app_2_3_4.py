from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    # Creamos una lista de diccionarios con datos de prueba
    mis_favoritos = [
        {"nombre": "Arroz chaufa", "motivo": "Diversidad de sabores"},
        {"nombre": "Ají de gallina", "motivo": "Pollo, arroz y crema"},
        {"nombre": "Picarones", "motivo": "Sabor dulce"}
    ]
    # Enviamos la lista completa a la plantilla con el nombre 'items'
    return render_template("lista_2_3_4.html", items=mis_favoritos)

if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)