from ayudas import *
from pygame.sprite import Sprite
import random

class agua:
    sprite = None
    archivo = 'agua'
    imagen = './imagenes/agua/1.png'
    size = VECTOR((22,20))
    coord = VECTOR((32,64))
    velocidad = VECTOR((0,0))
    indice = 0
    movimientos = []

def crearagua(jugador):

    sprite = Sprite()
    imagen = pygame.image.load(jugador.imagen).convert_alpha()
    sprite.image = pygame.transform.scale(imagen,(jugador.size.x,jugador.size.y))
    sprite.rect = sprite.image.get_rect() 
    sprite.rect.x = jugador.coord.x
    sprite.rect.y = jugador.coord.y  

    jugador.sprite = sprite

crearagua(agua)

animacion_agua = []

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/1.png'),
        (16,26)
    )
)

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/2.png'),
        (17,26)
    )
)

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/3.png'),
        (20,26)
    )
)

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/4.png'),
        (23,26)
    )
)

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/5.png'),
        (19,26)
    )
)

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/6.png'),
        (24,26)
    )
)

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/7.png'),
        (23,26)
    )
)

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/8.png'),
        (23,26)
    )
)


agua.movimientos.append(animacion_agua)

def copiaragua(jugador):
    sprite = Sprite()
    imagen = pygame.image.load(jugador.imagen).convert_alpha()
    sprite.image = pygame.transform.scale(imagen,(jugador.size.x,jugador.size.y))
    sprite.rect = sprite.image.get_rect() 
    sprite.rect.x = jugador.coord.x
    sprite.rect.y = jugador.coord.y  

    return sprite

# Posiciones fijas de las 4 gotas
posiciones_agua = [
    (284, 84), #fuenteexterior
    (175, 483), #canillaexterior
    (930, 176), #lavaloza
    (1130, 515), #lavadora
    (1375, 540), #bañera
    (1470, 180), #fuentepatio
    (1595, 370) #fuenteexterior
]

aguita = []

for x, y in posiciones_agua:
    gota = copiaragua(agua)

    gota.rect.x = x
    gota.rect.y = y

    aguita.append(gota)
    AGUITA.add(gota)

def cargarAnimacionesAguita(jugador, animacion, sprite):
    """Carga y actualiza la animación del jugador"""
    
    # Validaciones
    if not jugador.movimientos or animacion >= len(jugador.movimientos):
        return
    
    animaciones = jugador.movimientos[animacion]
    
    if not animaciones:
        return
    
    # Mover a la siguiente imagen
    jugador.indice = moverAnimacionesAguita(animaciones, jugador.indice)
    sprite.image = animaciones[jugador.indice]  

def moverAnimacionesAguita(animaciones, actual):
    """Avanza al siguiente frame de la animación"""
    
    if actual < len(animaciones) - 1:
        return actual + 1
    else:
        return 0     
