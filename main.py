from ayudas import *
from menuPrincipal import *
from storyboard import *
from pantallaCarga import * 
from ventana1 import *
from ventana2 import *
from gameOver import *

# zona de variables

# zona de funciones
    
#Zona de ejecucion

if __name__ == '__main__':

    #mostrarLetraSistema()
    

    while True:

        Ayudas.EVENTOS = pygame.event.get()

        for evento in Ayudas.EVENTOS:

            if evento.type == QUIT or (evento.type == KEYDOWN and evento.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        eval(Ayudas.actual+'()')

        pygame.display.update()
        Ayudas.DT = RELOJ.tick(FPS)