from flask import Flask, render_template, request, redirect
from data.coordenadas import Coordenada

coordenadas =[
    Coordenada(x="0", y="0", z="0", r="0", j1="0", j2="0", j3="0", j4="0"),
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", coordenadas=coordenadas)

@app.route('/coords', methods=["POST"])
def enviar_coords():
    coords = Coordenada(
        x= request.form["x"],
        y= request.form["y"],
        z= request.form["z"],
        r= request.form["r"],
        j1= request.form["j1"],
        j2= request.form["j2"],
        j3= request.form["j3"],
        j4= request.form["j4"]
    )
    global coordenadas
    coordenadas.append(coords)
    return redirect("/")


app.run(host ="0.0.0.0", port=3000, debug=True)