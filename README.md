# Intérprete Iconográfico

Este es un proyecto de la Universidad CENFOTEC, en colaboración con CrCibernética, para controlar la placa [IdeaBoard](https://www.crcibernetica.com/crcibernetica-ideaboard/), que contiene un ESP32, a través de programación iconográfica. Está destinado a contenidos educativos, especialmente para ejercicios de robótica utilizando el [Sumobot](https://github.com/Universidad-Cenfotec/Sumobot) y otros robots desarrollados por la universidad. La Universidad CENFOTEC invierte tiempo y recursos en el desarrollo de contenidos Open Source. Apoye las actividades de la universidad y comparta cualquier modificación de forma abierta.

Este proyecto consiste en un sistema que permite controlar un robot de forma remota a través de una interfaz web iconográfica. El sistema está compuesto por dos partes principales: un emisor basado en JavaScript para la interfaz de usuario y un receptor basado en CircuitPython para el control del robot.

**Investigadores:** Jeffry Valverde (CENFOTEC), Tomás de Camino Beck (CENFOTEC), Bentley Born (CrCibernética)

## Descripción

### Emisor

El emisor es una aplicación web que permite a los usuarios arrastrar y soltar íconos en un área específica y enviarlos al receptor. La interfaz incluye:

- Un área de arrastre para seleccionar íconos.
- Un área de soltado para ordenar los íconos.
- Campos de entrada para la dirección IP y el puerto del receptor.
- Un botón para enviar e iniciar el movimiento del robot.
- Un botón flotante para limpiar el área de soltado.

### Receptor

El receptor es un servidor CircuitPython que corre en el robot. Este servidor recibe los comandos enviados por la interfaz web y los ejecuta utilizando una placa IdeaBoard y un intérprete de comandos.

## Instrucciones

1. Renombrar `secretos_ejemplo.py` a `secretos.py`.
2. Configurar las credenciales de WiFi en las variables de entorno `CIRCUITPY_WIFI_SSID` y `CIRCUITPY_WIFI_PASSWORD`.
3. Configurar el hostname de su dispositivo.
4. Reiniciar el dispositivo.

## Uso

### Configuración del Emisor

1. Abre la interfaz web en un navegador y conecta a `hostname.local`.
2. Arrastra y suelta los íconos deseados en el área de soltado.
3. Haz clic en "Play" para enviar los comandos al receptor.

### Configuración del Receptor

1. Asegúrate de que la IdeaBoard esté conectada a la red WiFi.
2. El servidor escuchará en el puerto especificado (por defecto 80).
---

# Licencia de Software Abierta y No Comercial

**Versión 1.0**

Esta licencia establece los términos bajo los cuales se puede utilizar, modificar y distribuir el software licenciado.

## 1. Concesión de Licencia

Sujeto a los términos y condiciones de esta licencia, se concede al usuario una licencia mundial, libre de regalías y no exclusiva para usar, copiar, modificar y distribuir el software licenciado, únicamente para fines no comerciales.

## 2. Uso No Comercial

El código proporcionado solo puede ser utilizado para fines no comerciales. Cualquier uso comercial del software licenciado está expresamente prohibido sin el consentimiento previo por escrito del titular de los derechos de autor.

## 3. Distribución de Modificaciones

Si el usuario modifica el software licenciado, debe:
- Indicar claramente que se han realizado modificaciones.
- Compartir las modificaciones bajo los mismos términos de esta licencia.
- Incluir una copia de esta licencia con cualquier distribución de las modificaciones.

## 4. Propiedad Intelectual

El titular de los derechos de autor conserva todos los derechos, títulos e intereses sobre el software licenciado. Esta licencia no concede al usuario ningún derecho sobre marcas registradas, nombres comerciales, logotipos, u otros derechos de propiedad intelectual del titular de los derechos de autor.

