from flask import Flask, render_template, request, redirect
from data.coordenadas import Coordenada

coordenadas =[
    Coordenada(x="0", y="0", z="0", r="0"),
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
        r= request.form["r"]
    )
    global coordenadas
    coordenadas.append(coords)
    return redirect("/")

@app.route('/godot', methods=["GET", "POST"])
def godot_coords():
    x = coordenadas[(len(coordenadas) - 1)].x
    y = coordenadas[(len(coordenadas) - 1)].y
    z = coordenadas[(len(coordenadas) - 1)].z
    r = coordenadas[(len(coordenadas) - 1)].r
    godotstring = f"{x}/{y}/{z}/{r}"
    print(godotstring)
    return godotstring


app.run(host ="0.0.0.0", port=3000, debug=True)