from ayudas import *
from imagenes import *
from boton import*

class fondoPiso2:
    size = VECTOR(ANCHO, ALTO)
    coord = VECTOR(0,0)
    archivo = pygame.image.load(piso2).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0

class botonRegresar2:
    boton = None
    click = False
    texto = 'REGRESAR'
    font = fuentePrincipal
    fontSize = 30
    colorInactivo = azulClaro
    colorActivo = azulOscuro
    colorTexto = blanco
    coord = VECTOR(ANCHO-230,ALTO-80)
    size = VECTOR(220,50)
    borde = False
    tipo = 'ttf' #'system' 

def planta2():
    imagen(fondoPiso2)
    boton(botonRegresar2)

    if click(botonRegresar2):
        Ayudas.actual = 'menuPrincipal'
        botonRegresar2.click = False