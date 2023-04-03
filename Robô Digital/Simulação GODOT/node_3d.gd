extends Node3D

# Declaração das variáveis que serão utilizadas posteriormente
var URL = "http://127.0.0.1:3000/posicao_atual"
var coordenada_x
var coordenada_y
var coordenada_z
var ponta_robo
var posicao_atual = []

# Função para armazenamento do nodo referente ao robô
func _ready():
	ponta_robo = get_node("Ponta_RigidBody3D")
	print(ponta_robo)

# Função para envio da requisição HTTP a partir do botão "Alterar posição"
func _on_request_button_pressed():
	$CanvasLayer/Request_button/HTTPRequest.request(URL)

# Função para a movimentação do robô a partir da coordenada enviada pela requisição
func _on_http_request_request_completed(_result, _response_code, _headers, body):
	
	# Variável que armazena a string de coordenadas recebida via requisição
	posicao_atual = body.get_string_from_utf8()
	
	# Teste para segmentação das coordenadas da posição atual
	print(posicao_atual.get_slice("/", 0), posicao_atual.get_slice("/", 1), posicao_atual.get_slice("/", 2))
	
	# Atribuindo às variáveis x, y e z suas respectivas coordenadas, a partir da segmentação do valor recebido
	coordenada_x = float(posicao_atual.get_slice("/", 0))
	coordenada_y = float(posicao_atual.get_slice("/", 1))
	coordenada_z = float(posicao_atual.get_slice("/", 2))
	
	# Definição da posição inicial do robô na simulação
	ponta_robo.position = (Vector3(0,0,0))
	
	# Movimentação do robô para as coordenadas correspondentes
	ponta_robo.translate(Vector3((coordenada_x/10), (coordenada_y/10), (coordenada_z)/10))
