extends Button
@export var URL = "http://127.0.0.1:3000"

func _on_Request_button_button_down():
	$HTTPRequest.cancel_request()
	$HTTPRequest.request(URL)

func _on_http_request_request_completed(result, response_code, headers, body):
	var output = $body.get_string_from_utf8()
	print(output)
	$HTTPRequest.cancel_request()
