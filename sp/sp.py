import pygame, time, sys
from pygame.locals import *
fondo = (255, 255, 255)
altoX = 200
anchoY = 1024
inc = 1
posiX = 300 - 90
posiY = 20
sp1 = pygame.image.load("sp1.png")
sp2 = pygame.image.load("sp2.png")
sp3 = pygame.image.load("sp3.png")

ss1 = pygame.image.load("uno.png")
ss2 = pygame.image.load("dos.png")
ss3 = pygame.image.load("tres.png")

ss1 = pygame.transform.scale(ss1,[50,70])
ss2 = pygame.transform.scale(ss2,[50,70])
ss3 = pygame.transform.scale(ss3,[50,70])
pantalla = pygame.display.set_mode((anchoY, altoX))
sprite = [sp1, sp2, sp3]
p2 = [ss1, ss2, ss3]
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    cont = 0
    while (cont < 3):
        pantalla.fill(fondo)
        pantalla.blit(sprite[cont],[posiX, posiY])
        pantalla.blit(p2[cont],[posiX + 400, posiY + 100])
        print(sprite[0], p2[0])
        cont+=1
        pygame.display.update()
        time.sleep(.3)