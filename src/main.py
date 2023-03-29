from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

#Instanciando e configurando o app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coordenada.db'
# Intanciando a db do SqlAlchemy
db = SQLAlchemy(app)

#Criando a db do SQLAlchemy pelos comandos de Shell do Flask
@app.cli.command()
def createdb():
    db.create_all()

# Criando a classe que sera usada como base para a tabela do SQLAlchemy
class Coordenada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    z = db.Column(db.Float)
    r = db.Column(db.Float)
    def __init__(self, x, y, z, r) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.r = r


@app.before_first_request
def create_tables():
    db.create_all()
    coords = Coordenada(x=0.0, y=0.0, z=0.0, r=0.0)
    db.session.add(coords)
    db.session.commit()

#Definindo a pagina principal da nossa aplicacao Web
@app.route("/")
def index():
    global coordenadas
    # Puxando todos os dados escritos na tabela da DB
    coordenadas = Coordenada.query.all()
    return render_template("index.html", coordenadas=coordenadas)

# Definindo a rota de submit do botao da pagina principal da aplicacao Web para armazenar as cordenadas no banco
@app.route('/coords', methods=["POST"])
def enviar_coords():
    #Instanciando na classe da tabela da DB
    coords = Coordenada(
        x = request.form["x"],
        y = request.form["y"],
        z = request.form["z"],
        r = request.form["r"]
    )
    # Adicionando e enviando os dados para a tabela da DB
    db.session.add(coords)
    db.session.commit()
    return redirect("/")

# Rota para enviar os dados para o godot(Simulacao 3D)
@app.route('/godot', methods=["GET", "POST"])
def godot_coords():
    # Retomando todas as informacoes da tabela da DB
    coordenadas = Coordenada.query.all()
    # Pegando somente a ultima e separando suas colunas em variaveis
    x = coordenadas[-1].x
    y = coordenadas[-1].y
    z = coordenadas[-1].z
    r = coordenadas[-1].r
    # Adicionando todas essas 4 variaveis em uma mesma string
    godot_string = f"{x}/{y}/{z}/{r}"
    print(godot_string)
    # Retornando para exibicao e enviar para o godot
    return godot_string

# Iniciando o servidor web
if __name__ == "__main__":
    app.run(host ="0.0.0.0", port=3000, debug=True)