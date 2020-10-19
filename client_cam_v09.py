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
# camera.resolution = (1920, 1080)
# camera.brightness = 30
camera.start_preview()
# camera.annotate_size = 120 
# camera.annotate_foreground = Color('black')
# camera.annotate_background = Color('white')
# camera.annotate_text = " I am what I am " 
time.sleep(2)
# camera.capture("snapshot.jpg")
camera.capture("snapshot.png")
camera.stop_preview()

print('Convierto la imagen a string')

# Intento de envio de imagen 1
#file_data = open("snapshot.jpg", 'rb').read()
#soquete.emit('imagen', {'filename': "snapshot.jpg", 'data': file_data})

# Intento de envio de imagen 2
# soquete.emit('imagen', 'asdasdasdasdasdasdasdasdasdasdasdasdasdasdasd')
# print('Intento enviando la imagen realmente')
# import base64
# with open("snapshot.jpg", "rb") as image:
#    b64string = base64.b64encode(image.read())
# print('Voy a enviar')
# soquete.emit('imagen', {'data': b64string } )

# Intento de envio de imagen 3
import base64
with open("snapshot.png", "rb") as image:
    str = base64.b64encode(image.read())
    print(str)
soquete.emit('imagen', str )

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
def testOtro():
    print('I received a testOtro!')

@soquete.event
def test():
    print('I received a message!')

@soquete.event
def okFile():
    print("Envio de imagen")



