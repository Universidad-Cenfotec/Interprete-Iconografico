# Interprete Iconografico

Este es un proyecto de Universidad CENFOTEC, con colaboración de CrCibernética para controlar a través de programación iconográfica la placa [IdeaBoard](https://www.crcibernetica.com/crcibernetica-ideaboard/), que contiene un ESP32, para contenidos educativos, especialmente para ejercicios de robótica utilizando el [Sumobot](https://github.com/Universidad-Cenfotec/Sumobot) y otros robots que desarrolla la universidad.  Universidad CENFOTEC invierte tiempo y recursos en el desarrollo de contenidos Open Source. Apoye las actividades de la universidad y comparta cualquier modificación de forma abierta.

Este proyecto consiste en un sistema que permite controlar un robot de forma remota a través de una interfaz web iconográfica. El sistema está compuesto por dos partes principales: un emisor basado en JavaScript para la interfaz de usuario y un receptor basado en CircuitPython para el control del robot.

*Investigadores:* Jeffry Valverde (CENFOTEC), Tomás de Camino Beck (CENFOTEC), Bentley Born (CrCibernética)

# Descripción
## Emisor
El enviador es una aplicación web que permite a los usuarios arrastrar y soltar iconos en un área específica y enviarlos al receptor. La interfaz incluye:

Un área de arrastre para seleccionar iconos.
Un área de soltar para ordenar los iconos.
Campos de entrada para la dirección IP y el puerto del receptor.
Un botón para enviar e iniciar el movimiento del robot.
Un botón flotante para limpiar el área de soltar.

## Receptor
El receptor es un servidor CircuitPython que corre en el robot. Este servidor recibe los comandos enviados por la interfaz web y los ejecuta utilizando una placa IdeaBoard y un intérprete de comandos.

# Instrucciones:
Renombrar "secretos_ejemplo.py" a "secretos.py"
Configura las credenciales de WiFi en las variables de entorno CIRCUITPY_WIFI_SSID y CIRCUITPY_WIFI_PASSWORD.
Configurar el hostname de su dispositivo.
Reiniciar el dispositivo.

# Uso
## Configuración del Enviador:
Abre la interfaz web en un navegador y conectar a "hostname".local
Arrastra y suelta los iconos deseados en el área de soltar.
Haz clic en "Play" para enviar los comandos al receptor.

## Configuración del Receptor:
Asegúrate de que la IdeaBoard esté conectada a la red WiFi.
El servidor escuchará en el puerto especificado (por defecto 80).
