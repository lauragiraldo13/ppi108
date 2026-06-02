from ayudas import *
from jugador import *
from enemigo import *
from archivos import *
from boton import *
from agua import *

mapa1 = './mapas/mapa1/mapa1.tmx'

def cargarmapa1(mapa):
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

                if capa.name == '1borde' or capa.name == '2muros':
                    COLISIONES.add(sprite)
                if capa.name == '0piso':                   
                    FONDO.add(sprite) 
                


                CAMARA.add(sprite)   

class maya:
    sprite = None
    archivo = 'maya'
    imagen = './imagenes/maya/esperando/1.png'
    size = VECTOR((28,47))
    coord = VECTOR((80,600))
    velocidad = 32
    indice = 0
    movimientos = []
    vida = 100

jugador2(maya)

class mama:
    sprite = None
    archivo = 'mama'
    imagen = './imagenes/mama/idle/1.png'
    size = VECTOR((30,50))
    coord = VECTOR((510,500))
    indice = 0
    movimientos = []
    velocidad = VECTOR((32,0))
    distanciaAtaque = 80
    distanciaDetecta = 360
    ataque_cooldown = 0  # Tiempo de espera tras atacar
    atacando = False
    retirada = 0  # Tiempo de retirada en frames
    animacion_ataque_activa = False
    tiempo_animacion_ataque = 0
    duracion_animacion_ataque = 6 

crearEnemigo(mama)

childrenmarch.play(-1)

class textogameover:
    texto = 'Oh! Se desperdicio mucha agua... Perdiste'
    size = 35
    color = negro
    font = fuentePrincipal
    coord = VECTOR(50,50)
    parpadeando = True
    parpadear = pygame.USEREVENT + 1
    pygame.time.set_timer(parpadear,800)

class botonvolver:
    boton = None
    click = False
    texto = 'Volverlo a intentar'
    font = fuentePrincipal
    fontSize = 30
    colorInactivo = azulClaro
    colorActivo = azulOscuro
    colorTexto = blanco
    coord = VECTOR(1150,770)
    size = VECTOR(350,70)
    borde = False
    tipo = 'ttf' # 'ttf' 'system'

def ventana1():
    ventana.fill(cafe)
    emptySprites()

    cargarmapa1(mapa1)
    
    CAMARA.add(maya.sprite)
    CAMARA.add(mama.sprite)

    for gota in aguita:
        cargarAnimacionesAguita(agua,0,gota)
        CAMARA.add(gota)

    camara(maya)
    mover2(maya)

    enemigoAtaca(mama,maya)

    maya.vida = leer_vida()

    if maya.vida > 0 :
        font = pygame.font.SysFont(None,32)
        text = font.render(f"Vida: {maya.vida}", True, blanco)
        ventana.blit(text, (10,10))

    else:
        childrenmarch.stop()
        gameover3.play(-1)
        imagenDead = pygame.image.load('./imagenes/maya/muerto/1.png'). convert_alpha()
        maya.sprite.image = pygame.transform.scale(imagenDead,(30,50))
        intermitenteTextoTTF(textogameover)
        boton(botonvolver)
        
        if click(botonvolver):
            guardar_vida(100)
            gameover3.stop()
            childrenmarch.play(-1)
            Ayudas.actual = 'ventana1'
            botonvolver.click = False

        #guardar_vida(100)