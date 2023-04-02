extends Button

@export var URL = "http://127.0.0.1:3000/posicao_atual"

func _on_Request_button_button_down():
	$HTTPRequest.request(URL)

func _on_http_request_request_completed(_result, _response_code, _headers, _body):
	var output = _body.get_string_from_utf8()
	print(output)
