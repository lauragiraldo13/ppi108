from ayudas import *
from imagenes import *
from progreso import *

class fondoPrincipal2:
    size = VECTOR(ANCHO, ALTO)
    coord = VECTOR(0,0)
    archivo = pygame.image.load(tablero).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0

class textoBarra:
    texto = 'Cargando........'
    size = 30
    color = negro
    font = fuentePrincipal
    coord = VECTOR(MEDIO_ANCHO-98,ALTO-50)
    contador = 0
    velocidad = 3

class barraProgreso:
    size = VECTOR(600,48)
    coord = VECTOR(MEDIO_ANCHO-300,ALTO-60)
    color = cafecito
    progress = 0
    progress_increment = 1
    completed = False

def pantallaCarga():
    imagen(fondoPrincipal2)
    progreso(barraProgreso)
    mostrarTextoTTFMaquinaDeEscribir(textoBarra)

    if barraProgreso.completed:
        Ayudas.actual = 'ventana1'
        barraProgreso.completed = False
        barraProgreso.progress = 0