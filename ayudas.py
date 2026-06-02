import pygame, sys, os

from pygame.locals import *

from pytmx.util_pygame import load_pygame

import math

pygame.init()

pygame.font.init()
import pygame.freetype

FPS = 30

RELOJ = pygame.time.Clock()

TILESIZE = 32

ANCHO_MUNDO = TILESIZE*72 #(4608)

ALTO_MUNDO = TILESIZE*32 #(2304)

info = pygame.display.Info()

ventana = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN | pygame.SCALED)

ANCHO, ALTO = size = ventana.get_size()

MEDIO_ANCHO = ANCHO//2

MEDIO_ALTO = ALTO//2

pygame.display.set_caption('Aqui va el titulo de la ventana')

class Ayudas:
    pygame.init()
    EVENTOS = pygame.event.get()
    DT = 0
    actual = 'menuPrincipal'
    usuario = ''
    ACCION = 'ninguna'

# PALETA DE COLORES:
negro = (0,0,0)
blanco = (255,255,255)
gris = "#4D4545"
colorPrincipal = '#2D734D'
azul = (0,0,255)
azulClaro = "#82CED6"
azulOscuro = "#6CAEB8"
cafe = "#76603A"
cafecito = '#784330'
verde = "#88A959"

# TIPOS DE FUENTES:
simsun = 'simsun'
fuentePrincipal = './fuentes/almondMocca.otf'
letradumb2 = './fuentes/2Dumb.ttf'
letradumb3 = './fuentes/3Dumb.ttf'
letravt3r = './fuentes/VT3R.ttf'
letrasilk = './fuentes/silkscreen.ttf'
arial = 'arial'
candara = 'candara'



# LISTA DE IMAGENES:
maya = './imagenes/maya.png'
logoPrincipal = './imagenes/logo.png'
fondoP = './imagenes/fondop.png'
tablero = './imagenes/tablero.png'
fondoGM = './imagenes/gameOver.png'
piso1 = './imagenes/casa1.png'
piso2 = './imagenes/casa2.png'
mision = './imagenes/mision.png'


# ARCHIVOS PLANOS:
usuarios = './archivos/usuarios.txt'

# SONIDOS:
gameover3 = pygame.mixer.Sound('./sonidos/gameover3.ogg')
arr = pygame.mixer.Sound('./sonidos/arr.wav')
childrenmarch = pygame.mixer.Sound('./sonidos/childrenmarch.mp3')
VECTOR = pygame.math.Vector2 

def mostrarLetraSistema():
    letras = pygame.font.get_fonts()
    for l in letras:
        print(l)

def mostrarTextoSistema(texto):
    letra = pygame.freetype.SysFont(texto.font,texto.size)
    ventana.blit(letra.render(str(texto.texto),
                                  texto.color)[0],
                                  (texto.coord.x,texto.coord.y))    

def mostrarTextoTTF(texto):
    letra = pygame.freetype.Font(texto.font,texto.size)
    ventana.blit(letra.render(str(texto.texto),
                                  texto.color)[0],
                                  (texto.coord.x,texto.coord.y))  
    
def mostrarTextoLargoSistema(texto):
    letra = pygame.freetype.SysFont(texto.font,texto.size)
    y = texto.coord.y
    for linea in texto.texto:
        ventana.blit(letra.render(str(linea),
                                    texto.color)[0],
                                    (texto.coord.x,y))
        y += 30        

def mostrarTextoSistemaMaquinaDeEscribir(texto):
    letra = pygame.freetype.SysFont(texto.font,texto.size)
    if texto.contador < texto.velocidad * len(texto.texto):
        texto.contador += 1
  
    ventana.blit(letra.render(str(texto.texto[0:texto.contador//texto.velocidad]),
                                  texto.color)[0],
                                  (texto.coord.x,texto.coord.y))

def mostrarTextoTTFMaquinaDeEscribir(texto):
    letra = pygame.freetype.Font(texto.font,texto.size)
    if texto.contador < texto.velocidad * len(texto.texto):
        texto.contador += 1
  
    ventana.blit(letra.render(str(texto.texto[0:texto.contador//texto.velocidad]),
                                  texto.color)[0],
                                  (texto.coord.x,texto.coord.y)) 

def mostrarTextoLargoSistemaMaquinaDeEscribir(texto):
    letra = pygame.freetype.SysFont(texto.font,texto.size)

    if texto.contador < texto.velocidad * len(texto.linea):
        texto.contador += 1
    elif texto.contador >= texto.velocidad * len(texto.linea):
        texto.listo = True

    for evento in Ayudas.EVENTOS:
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RETURN and texto.listo and texto.actual < len(texto.texto)-1:
                texto.actual += 1
                texto.listo = False
                texto.linea = texto.texto[texto.actual]
                texto.contador = 0

    ventana.blit(letra.render(str(texto.linea[0:texto.contador//texto.velocidad]),
                                  texto.color)[0],
                                  (texto.coord.x,texto.coord.y))

def intermitenteTextoSistema(texto):
    for evento in Ayudas.EVENTOS:
        if evento.type == texto.parpadear:
            texto.parpadeando = not texto.parpadeando
    if texto.parpadeando:
        mostrarTextoSistema(texto)

def intermitenteTextoTTF(texto):
    for evento in Ayudas.EVENTOS:
        if evento.type == texto.parpadear:
            texto.parpadeando = not texto.parpadeando
    if texto.parpadeando:
        mostrarTextoTTF(texto)   

def error(mensaje):

    ancho = 300
    alto = 300
    
    tablero = pygame.Surface((ancho,alto))  
    tablero.fill(blanco)
    
    font = pygame.freetype.SysFont('Arial', 24)
    paso = 10

    for texto in mensaje:
        text_surface = font.render(texto,negro)[0]
        tablero.blit(text_surface, (10, paso))
        paso += 30

    ventana.blit(tablero,
                 (ANCHO//2-tablero.get_width()//2, 
                  ALTO//2-tablero.get_height()//2))

    
class textoError:
    texto = []
    inicio = pygame.time.get_ticks()
    tiempo = 100 #10segundos

def mostrarTextoError(mensaje):
    segundos = (pygame.time.get_ticks() - mensaje.inicio)/mensaje.tiempo
    if segundos < mensaje.tiempo:
        error(mensaje.texto)

class textoInfo:
    texto = ['',
             '',
             '']

def info(mensaje):

    ancho = 300
    alto = 300
    
    tablero = pygame.Surface((ancho,alto))  
    tablero.set_alpha(64)
    tablero.fill((220,20,60))
    
    font = pygame.freetype.SysFont('Arial', 24)
    paso = 10

    for texto in mensaje:
        text_surface = font.render(texto,negro)[0]
        tablero.blit(text_surface, (10, paso))
        paso += 30

    ventana.blit(tablero,
                 (ANCHO//2-tablero.get_width()//2, 
                  ALTO//2-tablero.get_height()//2))


# LISTAS DE SPRITES:
SPRITES = pygame.sprite.Group()

PLATAFORMAS = pygame.sprite.Group()

CAMARA = pygame.sprite.Group()

COLISIONES = pygame.sprite.Group()   

FONDO = pygame.sprite.Group()

PORTAL = pygame.sprite.Group()

OBJETOS = pygame.sprite.Group()

BASURAS = pygame.sprite.Group()

CHERRIES = pygame.sprite.Group()

ROTAN = pygame.sprite.Group()

GIRAN = pygame.sprite.Group()

INCLINADAS1 = pygame.sprite.Group()

INCLINADAS2 = pygame.sprite.Group()

AGUITA = pygame.sprite.Group()

offset = VECTOR((0,0))

def emptySprites():
    SPRITES.empty()
    PLATAFORMAS.empty()
    CAMARA.empty()
    COLISIONES.empty()
    PORTAL.empty()
    INCLINADAS1.empty()
    INCLINADAS2.empty()
    AGUITA.empty()

def camara(jugador):
    offset.x = jugador.sprite.rect.centerx-MEDIO_ANCHO
    offset.y = jugador.sprite.rect.centery-MEDIO_ALTO
    
    sprites_fondo = [s for s in CAMARA if s in COLISIONES or s in FONDO]
    sprites_otros = [s for s in CAMARA if s not in sprites_fondo]
    
    for sprite in sprites_fondo:
        offset_pos = sprite.rect.topleft - offset
        ventana.blit(sprite.image, offset_pos)
    
    sprites_ordenados = sorted(sprites_otros, key=lambda s: s.rect.bottom - offset.y)

    for sprite in sprites_ordenados:
        offset_pos = sprite.rect.topleft-offset
        if sprite in ROTAN:
            sprite_x = offset_pos.x + 25 * math.cos(math.radians(sprite.angulo))
            sprite_y = offset_pos.y + 25 * math.sin(math.radians(sprite.angulo))
            ventana.blit(sprite.image,(sprite_x, sprite_y))
        elif sprite in GIRAN:
            imagen_rotada = pygame.transform.rotate(sprite.image,sprite.angulo)
            ventana.blit(imagen_rotada,imagen_rotada.get_rect(center=(offset_pos.x,offset_pos.y)))   
        else:
            ventana.blit(sprite.image,offset_pos) 

def mapa(mapa):
    datos_mapa = load_pygame(mapa)
    
    # Cache para tiles escalados (evita recalcular el mismo tile)
    tile_cache = {}
    
    for capa in datos_mapa.visible_layers:
        if hasattr(capa, 'data'):
            for x, y, surf in capa.tiles():
                if surf is None:
                    continue
                
                # Obtener el ID único del tile (o usar la imagen misma como clave)
                tile_key = (surf.get_width(), surf.get_height(), id(surf))
                
                # Escalar solo si no está en caché
                if tile_key not in tile_cache:
                    tile_cache[tile_key] = pygame.transform.scale(surf, (TILESIZE, TILESIZE))
                
                # Usar la imagen escalada de la caché
                resized_image = tile_cache[tile_key]
                
                # Crear sprite (reconsiderar si necesitas un Sprite para cada tile)
                sprite = pygame.sprite.Sprite()
                sprite.image = resized_image
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = x * TILESIZE
                sprite.rect.y = y * TILESIZE

                if capa.name == 'borde' or capa.name == 'muros':
                    COLISIONES.add(sprite)

                if capa.name == 'piso':
                    FONDO.add(sprite)

                CAMARA.add(sprite)

    if 'objetos' in [layer.name for layer in datos_mapa.layers]:            
        for objeto in datos_mapa.get_layer_by_name('objetos'):
            sprite = pygame.sprite.Sprite()
            sprite.image = objeto.image
            resized_image = pygame.transform.scale(sprite.image,(128,128))
            sprite.image = resized_image
            sprite.rect = sprite.image.get_rect() 
            sprite.rect.x = objeto.x*2
            sprite.rect.y = objeto.y*2
            CAMARA.add(sprite)            

# LISTA DE MAPAS:
mapa1 = './mapas/mapa1/mapa1.tmx'      
mapa2 = './mapas/mapa2/mapa2.tmx'       

'''
class barrasalud:
    coord = VECTOR(10,10)
    size = VECTOR(300,30)
    salud = 100
    max = 100
    colorFondo = 
    colorFrente = 
'''
    
def barradesalud(barra):

    salud = barra.salud /barra.max

    pygame.draw.rect(ventana, barra.colorFondo, (barra.coord.x,barra.coord.y,barra.size.x,barra.size.y))
    pygame.draw.rect(ventana, barra.colorFrente, (barra.coord.x,barra.coord.y,barra.size.x*salud,barra.size.y))


class Temporizador:
    inicio = pygame.time.get_ticks()
    duracion = 5

def reiniciarTemporizador(t):
    t.inicio = pygame.time.get_ticks()    