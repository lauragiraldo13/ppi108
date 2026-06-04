from ayudas import *
from imagenes import *
from boton import*
from emergente import *
from entradadetexto import *
from emergente2 import *

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
    coord = VECTOR(100,ALTO-460)
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
    coord = VECTOR(MEDIO_ANCHO-100,550)
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
    coord = VECTOR(MEDIO_ANCHO+495,750)
    size = VECTOR(50,50)
    borde = False
    tipo = 'ttf' #'system' 

class ventanaEmergenteInfo:
    show = False
    size = VECTOR(400,500)
    coord = VECTOR(MEDIO_ANCHO+320,230)
    titulo = 'INFO'
    mensaje = 'Proyecto Académico'
    mensaje2 = 'Elaborado por:'
    mensaje3 = 'Laura Cristina Giraldo Monsalve'
    mensaje4 = 'Camila Osorio Suarez'
    mensaje5 = 'Santiago Vanegas Henao'

class ingreseUsuario:
    entrada = None
    click = False
    texto = ""
    font = arial
    fontSize = 30
    colorInactivo = azulOscuro
    colorActivo = negro
    eventoCursor = pygame.USEREVENT + 1
    pygame.time.set_timer(eventoCursor,500)
    coord = VECTOR(MEDIO_ANCHO-115,450)
    size = VECTOR(230,50)
    password = False

class pedirUsuario:
    texto = "Nombre de usuario:"
    size = 25
    color = negro
    font = candara
    coord = VECTOR(MEDIO_ANCHO-100,420)
    parpadeando = True
    parpadear = pygame.USEREVENT + 1
    pygame.time.set_timer(parpadear,800)

def menuPrincipal():
    imagen(fondoPrincipal)
    imagen(logoPrincipal)
    imagen(imagenMaya)
    boton(botonInfo)
    entrada(ingreseUsuario)
    mostrarTextoSistema(pedirUsuario)
    boton(botonJugar)

    if click (botonJugar):
        if ingreseUsuario.texto == '':
            Ventanaemergente2.titulo = 'Usuario inválido'
            Ventanaemergente2.mensaje = 'Debes ingresar un nombre de usuario!'
            Ventanaemergente2.show = True
        else:
            Ayudas.actual = 'ventana1'
            Ayudas.usuario = ingreseUsuario.texto
            resetear(ingreseUsuario)
            botonJugar.click = False

        emergente2(Ventanaemergente2, botonJugar)

    
       

    '''if click(botonPlanta1):
        Ayudas.actual = 'storyboard'
        botonPlanta1.click = False

    if click(botonPlanta2):
        Ayudas.actual = 'ventana2'
        botonPlanta2.click = False '''

    if click(botonInfo):
        ventanaEmergenteInfo.show = True
    
    emergente(ventanaEmergenteInfo, botonInfo)
    
    