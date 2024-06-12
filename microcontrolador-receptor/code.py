import os
import socketpool
import wifi
from adafruit_httpserver import Server, Request, JSONResponse, POST
from ideaboard import IdeaBoard
from interpreter import Interpreter
from time import sleep

ib = IdeaBoard()
inter = Interpreter()

# define functions (using non just to get a None parameter)
def stop(non):
    # detiene los motores
    ib.pixel = (0,0,0)
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
    
def forward(non):
    # Mueve el robot hacia adelante
    # por tiempo 3, a velocidad speed = [0,5]    
    ib.pixel = (0,255,0)
    ib.motor_1.throttle = 0.5
    ib.motor_2.throttle = 0.5
    sleep(3)
    stop(None)
    
def backward(non):
    # Mueve el robot hacia atrás
    # por tiempo 3, a velocidad speed = [0,5]    
    ib.pixel = (150,255,0)
    ib.motor_1.throttle = -0.5
    ib.motor_2.throttle = -0.5
    sleep(3)
    stop(None)
    
def left(non):
    # Mueve el robot hacia la izquierda
    # por tiempo 3, a velocidad speed = [0,5]    
    ib.pixel = (50,55,100)
    ib.motor_1.throttle = -0.5
    ib.motor_2.throttle = 0.5
    sleep(3)
    stop(None)
    
def right(non):
    # Mueve el robot hacia la derecha
    # por tiempo 3, a velocidad speed = [0,5]    
    ib.pixel = (50,55,100)
    ib.motor_1.throttle = 0.5
    ib.motor_2.throttle = -0.5
    sleep(3)
    stop(None)
    
# add functions to interpreter ('name', (function, parameter))
inter.addFunction('stop',(stop,None))
inter.addFunction('forward',(forward,None))
inter.addFunction('backward',(backward,None))
inter.addFunction('left',(left,None))
inter.addFunction('right',(right,None))

print(f"Connecting to {os.getenv("CIRCUITPY_WIFI_SSID")}...")
wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
print(f"Connected to {os.getenv("CIRCUITPY_WIFI_SSID")}")

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, debug=False)
puerto = 80

@server.route("/data", [POST], append_slash=True)
def api(request: Request):
    if request.method == POST:
        # Parse JSON data from the request body
        try:
            uploaded_object = request.json()
        except ValueError:
            return JSONResponse(request, {"message": "Invalid JSON format"}, status_code=400)

        # Print the received object to the console
        print("Recibido:", uploaded_object["dato"])
        recibido = uploaded_object["dato"]
        inter.execute(recibido)

        # Add the necessary CORS headers
        headers = {"Access-Control-Allow-Origin": "*"}  # Permitir todas las solicitudes CORS

        # Return a JSON response indicating success
        return JSONResponse(request, {"message": "Object received", "object": uploaded_object}, headers=headers)
    return JSONResponse(request, {"message": "Method not allowed"}, status_code=405)

# Manejador de ruta para solicitudes OPTIONS
@server.route("/data", ["OPTIONS"], append_slash=True)
def options(request: Request):
    # Agregar los encabezados CORS necesarios para las solicitudes OPTIONS
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type",
    }
    return JSONResponse(request, {}, headers=headers)

print("Server: " + str(wifi.radio.ipv4_address))
print("Puerto: " + str(puerto))
server.serve_forever(str(wifi.radio.ipv4_address), port=puerto)