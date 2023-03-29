from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coordenada.db'
db = SQLAlchemy(app)
@app.cli.command()
def createdb():
    db.create_all()

class Coordenada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    z = db.Column(db.Float)
    r = db.Column(db.Float)

@app.route("/")
def index():
    global coordenadas
    coordenadas = Coordenada.query.all()
    return render_template("index.html", coordenadas=coordenadas)

@app.route('/coords', methods=["POST"])
def enviar_coords():
    coords = Coordenada(
        x= request.form["x"],
        y= request.form["y"],
        z= request.form["z"],
        r= request.form["r"]
    )
    db.session.add(coords)
    db.session.commit()
    return redirect("/")

@app.route('/godot', methods=["GET", "POST"])
def godot_coords():
    coordenadas = Coordenada.query.all()
    x = coordenadas[-1].x
    y = coordenadas[-1].y
    z = coordenadas[-1].z
    r = coordenadas[-1].r
    godotstring = f"{x}/{y}/{z}/{r}"
    print(godotstring)
    return godotstring

app.run(host ="0.0.0.0", port=3000, debug=True)