
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Aplicacion desplegada correctamente en Render!"

@app.route("/info")
def informacion():
    return "Esta aplicacion utiliza Python y Flask."

if __name__ == "__main__":
    app.run()
