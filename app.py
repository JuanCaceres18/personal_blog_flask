from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient

app = Flask(__name__)

# Me logueo
cliente = MongoClient("mongodb+srv://juanpablocaceres8:ABHLk6maymXfClXE@devjuan.sqnvynj.mongodb.net/")
# Busco la base de datos
app.db = cliente.blog
# Lista con las entradas
entradas = [entrada for entrada in app.db.contenido.find({})]
print(entradas)

# Rutas
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Obtengo lo que se introdujo en los inputs
        titulo = request.form.get("title")
        entry_content = request.form.get("content")
        fecha_formato = datetime.datetime.today().strftime("%d-%m-%Y")
        parametros = {"titulo": titulo, "contenido": entry_content, "fecha": fecha_formato}
        entradas.append(parametros)
        # Lo inserto en la base de datos
        app.db.contenido.insert_one(parametros)

    return render_template("index.html", entradas=entradas)

if __name__ == "__main__":
    app.run(debug=True)