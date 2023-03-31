# Este script constitui um teste no qual as coordenadas, quando indicadas pelo usuário, são armazenadas em um banco de dados

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move')
def move():
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    r = request.form['r']
    j1 = request.form['j1']
    j2 = request.form['j2']
    j3 = request.form['j3']
    j4 = request.form['j4']
    
    # Estabelecendo conexão com a base de dados
    conn = sqlite3.connect('coordenadas.db')
    c = conn.cursor()

    # Inserindo as coordenadas na tabela
    c.execute('INSERT INTO coordinates (x, y, z, r, j1, j2, j3, j4) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (x, y, z, r, j1, j2, j3, j4))

    # Commitar as mudanças e fechar a conexão
    conn.commit()
    conn.close()

    return render_template('display.html', x=x, y=y, z=z, r=r, j1=j1, j2=j2, j3=j3, j4=j4)
    
    '''
    return 'Movendo o robô para as coordenadas X={}, Y={}, Z={}, R={} e angulações J1={}, J2={}, J3={}, J4{}'.format(x, y, z, r, j1, j2, j3, j4)
    '''

if __name__ == '__main__':
    app.run()