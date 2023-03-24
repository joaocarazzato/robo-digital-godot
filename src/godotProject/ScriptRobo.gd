extends Node

var URL = "http://127.0.0.1:3000/godot"

var Ponta
var Pos
var rng = RandomNumberGenerator.new()
var http = []
var output = []

func _ready():
	Ponta = get_node("PontaGarra_RigidBody3D")
	print(Ponta)

func _on_button_pressed():
	$CanvasLayer/HTTPRequest.request(URL)


func _on_http_request_request_completed(_result, _response_code, _headers, body):
	output = body.get_string_from_utf8()
	print("output: ", output)
	print("Output Array: ", output.get_slice("/", 0), ", ", output.get_slice("/", 1), ", ", output.get_slice("/", 2), ", ", output.get_slice("/", 3))
	Ponta.position = (Vector3(0, 0, 0))
	Ponta.translate((Vector3((float(output.get_slice("/", 0))/10), (float(output.get_slice("/", 1))/10), (float(output.get_slice("/", 2))/10))))
	pass # Replace with function body.
