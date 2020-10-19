import io
import time
import picamera
import socketio
import base64



# standard Python
soquete = socketio.Client()

print("intentanto conectar")

soquete.connect('http://66.97.46.179:3003')

print('El sid es', soquete.sid)

print('Pruebo enviando un msj de test')
soquete.emit('test', 'ESTE MENSAJE VIENE DE PYTHON! ah y juan se la come')

print('obtengo imagen de la camera')

camera = picamera.PiCamera()
camera.start_preview()
camera.capture("snapshot.jpg")
camera.stop_preview()

print('Voy a mandar la imagen de la camera')


# Intento de envio de imagen 1
#file_data = open("snapshot.jpg", 'rb').read()
#soquete.send('imagen', {'filename': "snapshot.jpg", 'data': file_data})

# Intento de envio de imagen 2
with open("snapshot.jpg", "rb") as image:
    b64string = base64.b64encode(image.read())
soquete.send('imagen', {'data': b64string} )


print('Pruebo enviando un msj de test 22')
#soquete.emit('test', {'probando': 'desde python'})
soquete.emit('test', 'ESTE MENSAJE VIENE DE PYTHON! ah y juan se la come')
#soquete.emit()

print("saliendo")
soquete.disconnect()


@soquete.event
def message(data):
    print('I received a message!')

@soquete.event
def connect():
    print("I'm connected!")

@soquete.event
def connect_error():
    print("The connection failed!")

@soquete.event
def disconnect():
    print("I'm disconnected!")



