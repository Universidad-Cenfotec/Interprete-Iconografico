'''
***************************************************
  Universidad CENFOTEC invierte tiempo y recursos en el desarrollo de 
  contenidos Open Source.  Apoye las actividades de la Universidad,
  y cualqueir modificación compártla de forma abierta

  Desarrollado por Jeffry Valverde y Bentley Born
  MIT license, all text above must be included in any redistribution
 ****************************************************
'''

import mdns
import socketpool
import wifi
import secretos
from adafruit_httpserver import Server, Request, JSONResponse, POST, FileResponse

# Clase para manejar el servidor local
class WebServerController:
    def __init__(self):
        self.decorators = []

    # Método para añadir un decorador estándar que sirve archivos
    def add_standard_decorator(self, route_name, file_name, folder_name):
        self.decorators.append(["add_standard_decorator", route_name, file_name, folder_name])
        
    # Método para añadir un decorador que maneja respuestas JSON en rutas POST
    def add_json_response_decorator(self, route_name):
        self.decorators.append(["add_json_response_decorator", route_name])
        
    # Método para configurar y ejecutar el servidor
    def execute_server(self, interpreter):        
        # Conecta a la red WiFi
        print(f"Connecting to {secretos.CIRCUITPY_WIFI_SSID}...")
        wifi.radio.connect(secretos.CIRCUITPY_WIFI_SSID, secretos.CIRCUITPY_WIFI_PASSWORD)
        print(f"Connected to {secretos.CIRCUITPY_WIFI_SSID}...")

        # Crea un pool de sockets y un servidor HTTP
        pool = socketpool.SocketPool(wifi.radio)
        server = Server(pool, debug=False)
        puerto = 80

        # Configura el servidor mDNS
        mdns_server = mdns.Server(wifi.radio)
        mdns_server.hostname = secretos.HOSTNAME
        mdns_server.advertise_service(service_type="_http", protocol="_tcp", port=puerto)

        # Itera sobre los decoradores y añade las rutas al servidor
        for decorator in self.decorators:
            if decorator[0] == "add_standard_decorator":
                route_name, file_name, folder_name = decorator[1], decorator[2], decorator[3]
                
                @server.route(route_name)
                def base(request: Request, file_name=file_name, folder_name=folder_name):
                    return FileResponse(request, file_name, folder_name)
                    
            elif decorator[0] == "add_json_response_decorator":
                route_name = decorator[1]
                
                @server.route(route_name, [POST], append_slash=True)
                def api(request: Request):
                    if request.method == POST:
                        try:
                            uploaded_object = request.json()
                        except ValueError:
                            return JSONResponse(request, {"message": "Invalid JSON format"}, status_code=400)

                        recibido = uploaded_object["dato"]
                        print(recibido)  # Debug
                        interpreter.execute(recibido)

                        headers = {"Access-Control-Allow-Origin": "*"}
                        return JSONResponse(request, {"message": "Object received", "object": uploaded_object}, headers=headers)
                    return JSONResponse(request, {"message": "Method not allowed"}, status_code=405)
            else:
                print('Function not found')
        
        # Imprime la URL del servidor y lo inicia
        print("http://" + mdns_server.hostname + ".local/")
        server.serve_forever(str(wifi.radio.ipv4_address), port=puerto)
