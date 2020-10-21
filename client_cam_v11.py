import io
import time
import picamera
import socketio
import base64



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
    camera.capture("snapshot.jpg")
    camera.stop_preview() 
    camera.close()

img_file = "snapshot.jpg"
data = base64.b64encode(open(img_file,"rb").read())              # convert to base64 format

print('envio la imagen - metodo imagen')
soquete.emit('testNew', data )

# pick an image file you have in the working directory
# or give full path
#b64 = base64.encodestring(open(img_file,"rb").read())
#try:
#    print('Entre en try!')
#    print('envio la imagen - metodo image')
#    soquete.emit('image', b64 )
    # Python2
    #print("rainbow_jpg_b64='''\\\n" + b64 + "'''")
#except TypeError:
    # Python3
#    print('Entre en error!')
    #print("rainbow_jpg_b64='''\\\n" + b64.decode("utf8") + "'''")




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



