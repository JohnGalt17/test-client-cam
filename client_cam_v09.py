import io
import time
import picamera
import socketio

# standard Python
soquete = socketio.Client()

print("intentanto conectar")

soquete.connect('http://66.97.46.179:3003')

print('El sid es', soquete.sid)

print('Pruebo enviando un msj de test')
soquete.emit('test', 'ESTE MENSAJE VIENE DE PYTHON! ah y juan se la come')

print('Pruebo enviando un msj a testOtro')
soquete.emit('testOtro', 'testOtro testOtro testOtro testOtro testOtro testOtro')

print('obtengo imagen de la camera')

camera = picamera.PiCamera()
camera.start_preview()
camera.capture("snapshot.jpg")
camera.stop_preview()

print('Convierto la imagen a string')

# Intento de envio de imagen 1
#file_data = open("snapshot.jpg", 'rb').read()
#soquete.emit('imagen', {'filename': "snapshot.jpg", 'data': file_data})

# Intento de envio de imagen 2
import base64
with open("snapshot.jpg", "rb") as image:
    b64string = base64.b64encode(image.read())
print('Voy a enviar')
soquete.emit('imagen', {'data': b64string } )


print('Pruebo enviando un msj de test de vuelta')
soquete.emit('test', 'ESTE MENSAJE VIENE DE PYTHON! ah y juan se la come 2222222222222')

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

@soquete.event
def testOtro(data):
    print('I received a message!', data)

@soquete.event
def test(data):
    print('I received a message!', data)

@soquete.event
def okFile():
    print("Envio de imagen")



