# Importando os módulos Flask e SQL Alchemy necessários

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.coordenadas import Coordenadas
import os

# Inicializando uma aplicação Flask
app = Flask(__name__)

# Definindo uma chave secreta
app.secret_key = 'my_secret_key' 

# Criando um banco de dados SQLite

engine = create_engine('sqlite:///coordenadas.db')

# Cria uma seção para utilizar o ORM

Session = sessionmaker(bind=engine) # Aqui, temos a CLASSE Session
session_db = Session()# Criando uma seção, uma forma de conversar com o SQLite. Aqui, temos o OBJETO session

# Cria as tabelas se elas não existirem

Base.metadata.create_all(engine)

# Definindo a posição inicial do robô

def inicializar_posicao():

    num_registros = session_db.query(Coordenadas).count()

    if num_registros == 0:
        posicao_inicial = Coordenadas(x = 0, y = 0, z = 0)

        session_db.add(posicao_inicial)
        session_db.commit()

inicializar_posicao()

# Criando rota principal
@app.route('/')
def index(): # Função que inicializa os valores das coordenadas x, y e z do robô[
    
    coordenadas = session_db.query(Coordenadas).all()

    return render_template('index.html', coordenadas=coordenadas)
    # Retorna o template principal, 'index.html'

# Rota correspondente ao joystick, uma das alternativas para movimentar o robô

@app.route('/joystick', methods=['POST'])
def joystick():
    
    direction = request.form['direcao'] # Processa o movimento realizado pelo joystick

    # Atribui às variáveis x, y e z o atual valor das coordenadas
    posicao_atual = session_db.query(Coordenadas).order_by(Coordenadas.id.desc()).first()
    x = posicao_atual.x
    y = posicao_atual.y
    z = posicao_atual.z
    
    # Realiza verificação para saber qual foi o input do usuário no joystick e modifica a coordenada
    if direction == 'up':
        y += 1

    if direction == 'down':
        y -= 1

    if direction == 'right':
        x += 1

    if direction == 'left':
        x -= 1

    if direction == 'front':
        z += 1

    if direction == 'back':
        z -= 1

    nova_posicao = Coordenadas(x = x, y = y, z = z)
    session_db.add(nova_posicao)
    session_db.commit()

    # Renderiza o template com as coordenadas atualizadas
    coordenadas = session_db.query(Coordenadas).all()
    return render_template('index.html', coordenadas=coordenadas)

# Rota correspondente à atualização das coordenadas do robô, manipuladas pelo usuário
@app.route('/move', methods=['POST'])
def definir_coordenadas():

    x = int(request.form['x'])
    y = int(request.form['y'])
    z = int(request.form['z'])

    # Set initial values to 0 if not already set

    session['x'] = session.get('x', 0)
    session['y'] = session.get('y', 0)
    session['z'] = session.get('z', 0)
    
    # Inserindo no banco de dados: ---------------------------------------------------------------------------------

    registro = Coordenadas(x = x, y = y, z = z)
    session_db.add(registro)
    session_db.commit()

    coordenadas = session_db.query(Coordenadas).all() # Retorna uma lista de objetos Coordenadas
    return render_template('index.html', coordenadas=coordenadas)

# Rota para resetar a posição do robô
@app.route('/reset', methods=['POST'])
def resetar_coordenadas():

    session_db.query(Coordenadas).delete()
    session_db.commit()

    registro = Coordenadas(x = 0, y = 0, z = 0)
    session_db.add(registro)
    session_db.commit()

    coordenadas = session_db.query(Coordenadas).all()
    return render_template('index.html', coordenadas=coordenadas)

# Rota para retornar a última posição do robô
@app.route('/posicao_atual', methods=['GET'])
def retornar_posicao():
    
    posicao_atual = session_db.query(Coordenadas).order_by(Coordenadas.id.desc()).first()

    if posicao_atual is not None:
        coordenada = {"x": posicao_atual.x, "y": posicao_atual.y, "z": posicao_atual.z}
    else:
        coordenada = {"x": 0, "y": 0, "z": 0}

    return jsonify(coordenada)

# Mantém a aplicação rodando
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3000, debug=True)