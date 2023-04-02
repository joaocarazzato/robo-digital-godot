# Robô digital simulado com Godot
A ideia desse projeto é simular a ação de um braço robótico através da engine de jogos nomeada [Godot](https://godotengine.org), utilizando um front-end feito em HTML, CSS e [Jinja](https://palletsprojects.com/p/jinja/), com um backend desenvolvido com [Flask](https://flask.palletsprojects.com/en/2.2.x/) e [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/) para o banco de dados salvando as coordenadas digitadas.

![image](https://user-images.githubusercontent.com/99187756/229372279-f4ffa384-c9bf-44e2-9018-9a5f6c331ee0.png)


# Back-end
O nosso back-end foi descrito em Python com a biblioteca Flask e uma conexão com um banco de dados desenvolvido em Flask-SQLAlchemy, podemos encontrar esse código no arquivo **src/main.py**.

Nas linhas 5 a 8 temos a configuração e instancias necessárias para começar o desenvolvimento:
```
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coordenada.db'
db = SQLAlchemy(app)
```
Em seguida em **@app.cli.command()**, temos uma função caso queira criar um banco de dados diretamente pelo shell do Flask, caso não queria, existe uma função mais a baixo que fará isso automaticamente, instanciada em **@app.before_first_request** .

Das linhas 15 a 26, temos o modelo do nosso banco de dados, passando como valores necessários **x, y, z e r**, que quando quisermos adicionar algum valor ao banco de dados, primeiro precisaremos citar a classe e passar os valores dentro dela, criando um objeto.

Das linhas 37 a 73, temos as rotas que usaremos para exibir nosso HTML **(@app.route("/"))**, fazer chamadas ao banco de dados **(@app.route('/godot'))** e adicionar dados ao banco de dados **(@app.route('/coords'))**.

Por fim, temos nas linhas 76 e 77 a execução da nossa aplicação Flask.

# Front-end
O nosso front-end exige somente uma página, que nos permite enviar as informações das coordenadas nos campos digitáveis e apresenta quantas vezes executamos as requisições e os últimos valores registrados. É de simples utilização, então essa pequena descrição já deve ser suficiente.

# Simulação
A simulação foi feita com a ferramenta de jogos 3D da engine de jogos chamada de [Godot em sua versão 4.0.1](https://godotengine.org/download/windows/), sendo necessária para nossa simulação funcionar. Ao executar o projeto, encontraremos dois cubos e uma esfera, que se locomoverão a partir dos dados impostos no front-end e usando de guia a ponta da garra. Clicando no botão de **"Get Pos"**, é executado a requisição necessária para locomover esses blocos, segue um video de demonstração da simulação:

https://user-images.githubusercontent.com/99187756/229372291-3e03334f-dcf8-4f0b-9321-47b8c5cf189b.mp4
