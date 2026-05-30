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
        (22,20)
    )
)

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/2.png'),
        (36,42)
    )
)

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/3.png'),
        (49,43)
    )
)

animacion_agua.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/agua/4.png'),
        (60,42)
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

aguita = [copiaragua(agua) for _ in range(20)]

for gota in aguita:
    gota.rect.x = random.randint(TILESIZE, ANCHO_MUNDO-TILESIZE)
    gota.rect.y = random.randint(TILESIZE, ALTO_MUNDO-TILESIZE)
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
