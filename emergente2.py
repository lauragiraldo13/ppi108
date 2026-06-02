import pygame

from ayudas import *

pygame.font.init()

class Ventanaemergente2:
    show = False
    size = VECTOR(400,200)
    coord = VECTOR(ANCHO//2 - size.x // 2, ALTO//2 - size.y // 2)
    titulo = 'titulo'
    mensaje = 'mensaje'

def emergente2(emergente2,boton):

    # Fuente
    font = pygame.font.SysFont("candara", 24)

    aceptar = pygame.Rect(
    emergente2.coord.x + (emergente2.size.x - 100) // 2,  # Centrado horizontalmente
    emergente2.coord.y + emergente2.size.y - 50,  # Parte inferior del popup
    100,  # Ancho del botón
    30)    # Alto del botón

    for evento in Ayudas.EVENTOS:
        if evento.type == pygame.MOUSEBUTTONDOWN and emergente2.show:
            mouse_pos = pygame.mouse.get_pos()

            if aceptar.collidepoint(mouse_pos):
                emergente2.show = False  # Cierra el popup
                boton.click = False

                

    if emergente2.show:
        # Fondo del popup (con borde)
        pygame.draw.rect(ventana, gris, (emergente2.coord.x, emergente2.coord.y, emergente2.size.x, emergente2.size.y))
        pygame.draw.rect(ventana, negro, (emergente2.coord.x, emergente2.coord.y, emergente2.size.x, emergente2.size.y), 2)
        
        # Título y mensaje del popup (centrados)
        titulo = font.render(emergente2.titulo , True, blanco)
        ventana.blit(titulo, (emergente2.coord.x + (emergente2.size.x - titulo.get_width()) // 2, emergente2.coord.y + 20))
        
        menssage = font.render(emergente2.mensaje , True, blanco)
        ventana.blit(menssage, (emergente2.coord.x + (emergente2.size.x - menssage.get_width()) // 2, emergente2.coord.y + 70))
        
        # Botón "Aceptar" (con efecto hover)
        mouse_pos = pygame.mouse.get_pos()
        button_color = azulClaro if aceptar.collidepoint(mouse_pos) else azulOscuro
        
        pygame.draw.rect(ventana, button_color, aceptar, border_radius=5)
        pygame.draw.rect(ventana, negro, aceptar, 2, border_radius=5)  # Borde del botón
        
        # Texto del botón (centrado)
        boton_aceptar = font.render("Aceptar", True, blanco)
        ventana.blit(
            boton_aceptar,
            (
                aceptar.centerx - boton_aceptar.get_width() // 2,
                aceptar.centery - boton_aceptar.get_height() // 2
            )
        )            

