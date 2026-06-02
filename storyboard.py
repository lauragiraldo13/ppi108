from ayudas import *
from imagenes import *
from progreso import *
from boton import*


class fondoprincipal3:
    size = VECTOR(ANCHO,ALTO)
    coord = VECTOR(10,10)
    archivo = pygame.image.load(mision).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0

class botoncomenzar:
    boton = None
    click = False
    texto = 'Comenzar...'
    font = fuentePrincipal
    fontSize = 30
    colorInactivo = azulClaro
    colorActivo = azulOscuro
    colorTexto = negro
    coord = VECTOR(MEDIO_ANCHO-138,MEDIO_ALTO+349)
    size = VECTOR(350,80)
    borde = False
    tipo = 'ttf'

'''class texto:
    texto = ["Realiza acciones inteligentes",
             "para ahorrar agua en casa y",
             "cuidar nuestro planeta"]
    size = 20
    color = negro
    font = arial
    coord = VECTOR(10,120)
    contador = 0
    velocidad = 1
    actual = 0
    linea = texto[actual]
    listo = False'''


def storyboard():
    imagen(fondoprincipal3)
    boton(botoncomenzar)
    #mostrarTextoSistemaMaquinaDeEscribir(texto)
    
    if click (botoncomenzar):

        Ayudas.actual = 'pantallaCarga'
        botoncomenzar.click = False