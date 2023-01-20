import pygame
from sys import exit
from Cuadrado import Cuadrado

pygame.init()
anchoV = 400    # Se define el ancho de la ventana
altoV = 400
tamPant = (anchoV,altoV)
pantalla = pygame.display.set_mode(tamPant)

reloj = pygame.time.Clock() # Se define la variable reloj manejador de refresco de pantalla

cRojo = Cuadrado(100,100,40,(255,50,50),"rojo")
cAzul = Cuadrado(100,150,40,(50,20,255),"azul")
listaC = []
listaC.append(cRojo)
listaC.append(cAzul)
while True:
    pygame.Surface.fill(pantalla,(0,0,0),None)
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for cuadro in listaC:
        if cuadro.nombre == 'rojo':
            xIni = 1
            yIni = 3
        else:
            xIni = 10
            yIni = 3
            pass
        pygame.draw.rect(pantalla, cuadro.color, (cuadro.posX, cuadro.posY, cuadro.tam,cuadro.tam)) # (Superficie en la cual dibuja, color, (objeto rect{x,y, tamx, tamy} ))
        #Actualizar posicion de los cuadrados
        cuadro.posX = cuadro.posX + (xIni*cuadro.velx)
        cuadro.posY = (cuadro.posY*cuadro.vely)
        cuadro.comprobarL(400,400)
        pass
    pygame.display.update()
    reloj.tick(30) # Define la tasa de 60 FPS
    pass