from ideaboard import IdeaBoard  
from interpreter import Interpreter  # Importa la clase Interpreter para interpretar y ejecutar comandos.
from web_server_controller import WebServerController  # Importa la clase WebServerController para controlar el servidor web.
from time import sleep 
import secretos

# Crear instancias de IdeaBoard, Interpreter y WebServerController.
ib = IdeaBoard()
inter = Interpreter()
wsc = WebServerController()

# Función para detener los motores y apagar el LED.
def stop(non):
    ib.pixel = (0,0,0)  
    ib.motor_1.throttle = 0  
    ib.motor_2.throttle = 0

# Función para avanzar hacia adelante.
def forward(non):
    ib.pixel = (0,255,0)
    ib.motor_1.throttle = 0.5  
    ib.motor_2.throttle = 0.5  
    sleep(3)  
    stop(None) 
    sleep(0.5) 

# Función para retroceder.
def backward(non):
    ib.pixel = (150,255,0) 
    ib.motor_1.throttle = -0.5 
    ib.motor_2.throttle = -0.5 
    sleep(3) 
    stop(None)  
    sleep(0.5)

# Función para girar a la izquierda.
def left(non):
    ib.pixel = (50,55,100) 
    ib.motor_1.throttle = -0.5
    ib.motor_2.throttle = 0.5 
    sleep(3) 
    stop(None)
    sleep(0.5)

# Función para girar a la derecha.
def right(non):
    ib.pixel = (50,55,100)
    ib.motor_1.throttle = 0.5
    ib.motor_2.throttle = -0.5
    sleep(3)
    stop(None)
    sleep(0.5)

# Agrega las funciones al intérprete para que puedan ser llamadas a través de comandos.
inter.addFunction('stop', (stop, None))
inter.addFunction('forward', (forward, None))
inter.addFunction('backward', (backward, None))
inter.addFunction('left', (left, None))
inter.addFunction('right', (right, None))

# Configuración del servidor web para servir archivos estáticos y manejar solicitudes.
wsc.add_standard_decorator("/", "index.html", "/")
wsc.add_standard_decorator("/css/reset.css", "reset.css", "/css")
wsc.add_standard_decorator("/css/styles.css", "styles.css", "/css")
wsc.add_standard_decorator("/js/dragAndDrop.js", "dragAndDrop.js", "/js")
wsc.add_standard_decorator("/assets/cenfotec-logo.png", "cenfotec-logo.png", "/assets")
wsc.add_standard_decorator("/assets/crcibernetica-logo.png", "crcibernetica-logo.png", "/assets")
wsc.add_json_response_decorator("/data")

ib.pixel = (0,0,255)  # Enciende el LED en azul al para indicar que esta listo para recibir mensajes.
wsc.execute_server(inter)  # Inicia el servidor web con el intérprete.