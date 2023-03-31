# Importando os módulos Flask e SQL Alchemy necessários

from flask import Flask, render_template, request, session, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.coordenadas import Coordenadas
# from data.funcoes import Posicao

# Inicializando uma aplicação Flask
app = Flask(__name__)

# Definindo uma chave secreta
app.secret_key = 'my_secret_key' 

# CRIAÇÃO DO BANCO DE DADOS

engine = create_engine('sqlite:///coordenadas.db')

# Cria uma seção para utilizar o ORM

Session = sessionmaker(bind=engine) # Aqui, temos a CLASSE Session
session_db = Session()# Criando uma seção, uma forma de conversar com o SQLite. Aqui, temos o OBJETO session

# Cria as tabelas se elas não existirem

Base.metadata.create_all(engine)

# Criando rota principal
@app.route('/')
def index(): # Função que inicializa os valores das coordenadas x, y e z do robô[
    
    coordenadas = session_db.query(Coordenadas).all()

    return render_template('index.html', coordenadas=coordenadas)
    # Retorna o template principal, 'index.html'

# ---------------------------------------------------------------------------------------------

# Rota correspondente ao joystick, uma das alternativas para movimentar o robô

@app.route('/joystick', methods=['POST'])
def joystick():

    direction = request.form['direcao'] # Processa o movimento realizado pelo joystick

    # Atribui às variáveis x, y e z o atual valor das coordenadas
    y = request.form.get('y', session.get('y', '0'))
    x = request.form.get('x', session.get('x', '0'))
    z = request.form.get('z', session.get('z', '0'))

    # Realiza verificação para saber se existe um valor atual em cada coordenada
    if y:
        session['y'] = int(y)
    else:
        session['y'] = 0

    if x:
        session['x'] = int(x)
    else:
        session['x'] = 0

    if z:
        session['z'] = int(z)
    else:
        session['z'] = 0

    # Realiza verificação para saber qual foi o input do usuário no joystick e modifica a coordenada
    if direction == 'up':
        session['y'] += 1

    if direction == 'down':
        session['y'] -= 1

    if direction == 'right':
        session['x'] += 1

    if direction == 'left':
        session['x'] -= 1

    if direction == 'front':
        session['z'] += 1

    if direction == 'back':
        session['z'] -= 1
    
    # Obter as coordenadas atualizadas do robô
    x = session.get('x', 0)
    y = session.get('y', 0)
    z = session.get('z', 0)

    registro = Coordenadas(x = x, y = y, z = z)
    session_db.add(registro)
    session_db.commit()

    # Renderiza o template com as coordenadas atualizadas
    coordenadas = session_db.query(Coordenadas).all()
    return render_template('index.html', coordenadas=coordenadas)
        
# # Rota correspondente à atualização das coordenadas do robô, manipuladas pelo usuário
@app.route('/move', methods=['POST'])
def definir_coordenadas():

    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    # Inserindo no banco de dados: ---------------------------------------------------------------------------------

    registro = Coordenadas(x = x, y = y, z = z)
    session_db.add(registro)
    session_db.commit()

    coordenadas = session_db.query(Coordenadas).all() # Retorna uma lista de objetos Coordenadas
    return render_template('index.html', coordenadas=coordenadas)
    
# Mantém a aplicação rodando
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3000, debug=True)