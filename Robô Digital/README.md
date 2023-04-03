<h2>Simulação de Robô Digital</h2>

<p>O presente diretório é destinado à entrega da atividade referente à simulação de um robô digital.</p>

<h4>Introdução à atividade</h4>

<p>O projeto Robô Digital tem por objetivo a elaboração de uma solução completa de integração entre as Tecnologias de Automação (TA) e as Tecnologias de Informação (TI). Trata-se de uma representação digital para um braço robótico com conexão em tempo real com sua contrapartida no mundo real.</p>

<h4>Estrutura do projeto</h4>

<p>Para a atividade, foi proposta uma estrutura que permite ao usuário manipular a posição do braço robótico via interface e visualizar uma simulação da movimentação do robô na engine GODOT.</p>

* <h5>Front-End</h5>

A interface gráfica por meio da qual é possível definir as coordenadas do robô se encontra na pasta "src/templates". Na interface, são apresentadas duas possibilidades para a manipulação de coordenadas: defini-las manualmente ou utilizar os botões correspondentes a um joystick.

* <h5>Back-End</h5>

O Back-End do projeto, realizado em Flask, pode ser encontrado em "src/app.py" e utiliza os módulos criados em "src/models". O servidor conta com uma rota principal, uma rota correspondente à definição manual de coordenadas, uma rota correspondente ao joystick, uma rota para envio das coordenadas modificadas pelo usuário e uma rota que retorna a última posição armazenada no banco de dados. Além disso, é possível visualizar, no script, a implementação de um banco de dados utilizando SQL Alchemy.

* <h5>Simulação no GODOT</h5>

A pasta "Simulação GODOT" armazena o projeto de simulação desenvolvido, e conta com uma representação 3D do braço robótico. O script contido no projeto constitui um código GDScript, responsável por realizar uma requisição HTTP para a API desenvolvida e concretizar a movimentação do robô baseando-se na última coordenada armazenada no banco de dados.

<h4>Estrutura de pastas</h4>

<br>
:file_folder: &nbsp; Simulação GODOT <br>
:file_folder: &nbsp; src <br>
&nbsp; &nbsp; :file_folder: &nbsp; models <br>
&nbsp; &nbsp; &nbsp; &nbsp; :page_with_curl: &nbsp; base.py <br>
&nbsp; &nbsp; &nbsp; &nbsp; :page_with_curl: &nbsp; coordenadas.py <br>
&nbsp; &nbsp; :file_folder: &nbsp; templates <br>
&nbsp; &nbsp; &nbsp; &nbsp; :page_with_curl: &nbsp; index.html <br>
&nbsp; &nbsp; :page_with_curl: &nbsp; app.py <br>
&nbsp; &nbsp; :page_with_curl: &nbsp; coordenadas.db <br>
:page_with_curl: &nbsp; README.md <br>
