import pygame

from ayudas import *

pygame.font.init()

class Ventanaemergente:
    show = False
    size = VECTOR(300,400)
    coord = VECTOR(ANCHO//2 - size.x // 2, ALTO//2 - size.y // 2)
    titulo = 'titulo'
    mensaje = 'mensaje'

def emergente(emergente, boton):

    # Fuente
    font = pygame.font.SysFont("simsun", 24)

    aceptar = pygame.Rect(
    emergente.coord.x + (emergente.size.x - 100) // 2,  # Centrado horizontalmente
    emergente.coord.y + emergente.size.y - 50,  # Parte inferior del popup
    100,  # Ancho del botón
    30)    # Alto del botón

    for evento in Ayudas.EVENTOS:
        if evento.type == pygame.MOUSEBUTTONDOWN and emergente.show:
            mouse_pos = pygame.mouse.get_pos()

            if aceptar.collidepoint(mouse_pos):
                emergente.show = False  # Cierra el popup
                boton.click = False 
                

    if emergente.show:
        # Fondo del popup (con borde)
        pygame.draw.rect(ventana, gris, (emergente.coord.x, emergente.coord.y, emergente.size.x, emergente.size.y))
        pygame.draw.rect(ventana, negro, (emergente.coord.x, emergente.coord.y, emergente.size.x, emergente.size.y), 2)
        
        # Título y mensaje del popup (centrados)
        titulo = font.render(emergente.titulo , True, blanco)
        ventana.blit(titulo, (emergente.coord.x + (emergente.size.x - titulo.get_width()) // 2, emergente.coord.y + 20))
        
        menssage = font.render(emergente.mensaje , True, blanco)
        ventana.blit(menssage, (emergente.coord.x + (emergente.size.x - menssage.get_width()) // 2, emergente.coord.y + 70))
        menssage = font.render(emergente.mensaje2 , True, blanco)
        ventana.blit(menssage, (emergente.coord.x + (emergente.size.x - menssage.get_width()) // 2, emergente.coord.y + 250))
        menssage = font.render(emergente.mensaje3 , True, blanco)
        ventana.blit(menssage, (emergente.coord.x + (emergente.size.x - menssage.get_width()) // 2, emergente.coord.y + 275))
        menssage = font.render(emergente.mensaje4 , True, blanco)
        ventana.blit(menssage, (emergente.coord.x + (emergente.size.x - menssage.get_width()) // 2, emergente.coord.y + 300))
        menssage = font.render(emergente.mensaje5 , True, blanco)
        ventana.blit(menssage, (emergente.coord.x + (emergente.size.x - menssage.get_width()) // 2, emergente.coord.y + 325))
        
        
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