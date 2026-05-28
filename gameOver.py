from ayudas import *
from imagenes import *
from boton import *

class fondoGameOver:
    size = VECTOR(ANCHO, ALTO)
    coord = VECTOR(0,0)
    archivo = pygame.image.load(fondoGM).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0

class textoGame:
    texto = 'GAME'
    size = 100
    color = blanco
    font = fuentePrincipal
    coord = VECTOR(MEDIO_ANCHO-165,MEDIO_ALTO-60)

class textoOver:
    texto = 'OVER'
    size = 100
    color = blanco
    font = fuentePrincipal
    coord = VECTOR(MEDIO_ANCHO-156,MEDIO_ALTO+15)

class botonReintentar:
    boton = None
    click = False
    texto = 'REINTENTAR'
    font = fuentePrincipal
    fontSize = 30
    colorInactivo = azulClaro
    colorActivo = azulOscuro
    colorTexto = blanco
    coord = VECTOR(MEDIO_ANCHO-110,ALTO - 100)
    size = VECTOR(220,50)
    borde = False
    tipo = 'ttf' #'system' 

def pantallaGameOver():
    imagen(fondoGameOver)
    mostrarTextoTTF(textoGame)
    mostrarTextoTTF(textoOver)
    boton(botonReintentar)

    if click(botonReintentar):
        Ayudas.actual = 'ventana1'
        botonReintentar.click = False