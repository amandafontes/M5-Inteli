# Importando os módulos Flask necessários
from flask import Flask, render_template, request, session, redirect, url_for

# Inicializando uma aplicação Flask
app = Flask(__name__)

# Definindo uma chave secreta
app.secret_key = 'my_secret_key' 

# Criando rota principal
@app.route('/')
def index():

    x = session.get('x', None)
    y = session.get('y', None)
    z = session.get('z', None)
    r = session.get('r', None)
    j1 = session.get('j1', None)
    j2 = session.get('j2', None)
    j3 = session.get('j3', None)
    j4 = session.get('j4', None)

    return render_template('index.html', x=x, y=y, z=z, r=r, j1=j1, j2=j2, j3=j3, j4=j4) # Retorna o template principal, 'index.html'

# Rota correspondente à atualização das coordenadas do robô, manipuladas pelo usuário
@app.route('/move', methods=['POST'])
def move():

    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    r = request.form['r']
    j1 = request.form['j1']
    j2 = request.form['j2']
    j3 = request.form['j3']
    j4 = request.form['j4']

    # Armazenando as coordenadas em session variables
    session['x'] = x
    session['y'] = y
    session['z'] = z 
    session['r'] = r
    session['j1'] = j1
    session['j2'] = j2
    session['j3'] = j3
    session['j4'] = j4

    # Redirecionando para o URL principal
    return redirect('/')
    
    '''
    return 'Movendo o robô para as coordenadas X={}, Y={}, Z={}, R={} e angulações J1={}, J2={}, J3={}, J4{}'.format(x, y, z, r, j1, j2, j3, j4)
    '''

# Mantém a aplicação rodando
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3000, debug=True)