from ayudas import *
from imagenes import *
from boton import*
from emergente import *

class fondoPrincipal:
    size = VECTOR(ANCHO, ALTO)
    coord = VECTOR(0,0)
    archivo = pygame.image.load(fondoP).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0

class logoPrincipal:
    size = VECTOR(800,500)
    coord = VECTOR(MEDIO_ANCHO-400,-80)
    archivo = pygame.image.load(logoPrincipal).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0

class imagenMaya:
    size = VECTOR(280,460)
    coord = VECTOR(10,ALTO-460)
    archivo = pygame.image.load(maya).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0

class botonJugar:
    boton = None
    click = False
    texto = 'JUGAR'
    font = fuentePrincipal
    fontSize = 30
    colorInactivo = azulClaro
    colorActivo = azulOscuro
    colorTexto = blanco
    coord = VECTOR(MEDIO_ANCHO-100,420)
    size = VECTOR(200,70)
    borde = False
    tipo = 'ttf' #'system' 

'''class botonPlanta1:
    boton = None
    click = False
    texto = 'PLANTA 1'
    font = fuentePrincipal
    fontSize = 30
    colorInactivo = azulClaro
    colorActivo = azulOscuro
    colorTexto = blanco
    coord = VECTOR(ANCHO-210,ALTO-110)
    size = VECTOR(200,50)
    borde = False
    tipo = 'ttf' #'system

class botonPlanta2:
    boton = None
    click = False
    texto = 'PLANTA 2'
    font = fuentePrincipal
    fontSize = 30
    colorInactivo = azulClaro
    colorActivo = azulOscuro
    colorTexto = blanco
    coord = VECTOR(ANCHO-210,ALTO-60)
    size = VECTOR(200,50)
    borde = False
    tipo = 'ttf' #'system' '''

class botonInfo:
    boton = None
    click = False
    texto = 'i'
    font = fuentePrincipal
    fontSize = 30
    colorInactivo = azulClaro
    colorActivo = azulOscuro
    colorTexto = blanco
    coord = VECTOR(MEDIO_ANCHO-25,520)
    size = VECTOR(50,50)
    borde = False
    tipo = 'ttf' #'system' 

class ventanaEmergenteInfo:
    show = False
    size = VECTOR(400,500)
    coord = VECTOR(ANCHO//2 - size.x // 2, ALTO//2 - size.y // 2)
    titulo = 'INFO'
    mensaje = 'Proyecto Academico'
    mensaje2 = 'Elaborado por:'
    mensaje3 = 'Laura Cristina Giraldo Monsalve'
    mensaje4 = 'Camila Osorio Suarez'
    mensaje5 = 'Santiago Vanegas Henao'

def menuPrincipal():
    imagen(fondoPrincipal)
    imagen(logoPrincipal)
    imagen(imagenMaya)
    boton(botonJugar)
    boton(botonInfo)
    #boton(botonPlanta1)
    #boton(botonPlanta2)

    if click(botonJugar):
        Ayudas.actual = 'storyboard'
        botonJugar.click = False

    '''if click(botonPlanta1):
        Ayudas.actual = 'ventana1'
        botonPlanta1.click = False

    if click(botonPlanta2):
        Ayudas.actual = 'ventana2'
        botonPlanta2.click = False '''

    if click(botonInfo):
        ventanaEmergenteInfo.show = True
    
    emergente(ventanaEmergenteInfo, botonInfo)