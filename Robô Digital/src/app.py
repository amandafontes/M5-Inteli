# Importando os módulos Flask necessários
from flask import Flask, render_template, request, session, redirect, url_for
#from data.funcoes import Posicao

# Inicializando uma aplicação Flask
app = Flask(__name__)

# Definindo uma chave secreta
app.secret_key = 'my_secret_key' 

'''
posicoes =[
    Posicao(x="100", y="100", z="100", r="100", j1="100", j2="100", j3="100", j4="100")
]
'''

# Criando rota principal
@app.route('/')
def index(): # Função que inicializa os valores das coordenadas x, y e z do robô

    x = session.get('x', None)
    y = session.get('y', None)
    z = session.get('z', None)
    # r = session.get('r', None)
    # j1 = session.get('j1', None)
    # j2 = session.get('j2', None)
    # j3 = session.get('j3', None)
    # j4 = session.get('j4', None)

    return render_template('index.html', x=x, y=y, z=z, r=r, j1=j1, j2=j2, j3=j3, j4=j4) # Retorna o template principal, 'index.html'

# Rota correspondente ao joystick, uma das alternativas para movimentar o robô
@app.route('/joystick', methods=['POST'])
def joystick():

    direction = request.form['direcao'] # Processa o movimento realizado pelo joystick

    session['y'] = int(session['y'])
    session['x'] = int(session['x'])
    session['z'] = int(session['z'])

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
        session['z'] -+ 1
    
    # Obter as coordenadas atuais do robô
    x = session.get('x', 0)
    y = session.get('y', 0)
    z = session.get('z', 0)

    # Renderiza o template com as coordenadas atualizadas
    return render_template('index.html', x=x, y=y, z=z)
        
# Rota correspondente à atualização das coordenadas do robô, manipuladas pelo usuário
@app.route('/move', methods=['POST'])
def move():

    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    # r = request.form['r']
    # j1 = request.form['j1']
    # j2 = request.form['j2']
    # j3 = request.form['j3']
    # j4 = request.form['j4']

    # Armazenando as coordenadas em session variables
    session['x'] = x
    session['y'] = y
    session['z'] = z 
    # session['r'] = r
    # session['j1'] = j1
    # session['j2'] = j2
    # session['j3'] = j3
    # session['j4'] = j4

    # Redirecionando para o URL principal
    return redirect('/')
    
    '''
    return 'Movendo o robô para as coordenadas X={}, Y={}, Z={}, R={} e angulações J1={}, J2={}, J3={}, J4{}'.format(x, y, z, r, j1, j2, j3, j4)
    '''

# Mantém a aplicação rodando
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3000, debug=True)