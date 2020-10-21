import io
import time
import picamera
import socketio



# standard Python
soquete = socketio.Client()

print("intentanto conectar")

soquete.connect('http://66.97.46.179:3003')

# print('El sid es', soquete.sid)

print('Pruebo enviando un msj de test')
soquete.emit('test', 'ESTE MENSAJE VIENE DE PYTHON! ah y juan se la come')

print('obtengo imagen de la camera')
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture("snapshot.jpeg")
    camera.stop_preview()
    
import base64
with open("snapshot.jpeg", "wb") as fh:
    print('envio la imagen')
    soquete.emit('imagen', fh.write(base64.decodebytes('base64')) )


print('Pruebo enviando un msj de test 22')
#soquete.emit('test', {'probando': 'desde python'})
soquete.emit('test', 'ESTE MENSAJE VIENE DE PYTHON! ah y juan se la come')
#soquete.emit()



print("conectado")
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



