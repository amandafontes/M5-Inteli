extends Button

@export var URL = "http://127.0.0.1:3000/posicao_atual"
var Ponta_robo
var Posicao

func _ready():
	Ponta_robo = get_node("RigidBody3D")
	print(Ponta_robo)

func _on_Request_button_button_down():
	$HTTPRequest.request(URL)

func _on_http_request_request_completed(_result, _response_code, _headers, _body):
	var output = _body.get_string_from_utf8()
	print(output)
	
	Ponta_robo.position = (Vector3(0, 0, 0))
	Ponta_robo.translate = (Vector3(float(output.get_slice(",", 0)), float(output.get_slice(",", 1)), float(output.get_slice(",", 2))))
