import pygame


canvas = pygame.display.set_mode((500,500))

x=0
y=0
ydir = 0
xdir = 0

while(True):
    x = x+1*xdir
    y= y+1*ydir
    canvas.fill((0,0,0))
    pygame.draw.rect(canvas,(250,0,0), (x,y,10,10))
    pygame.display.update()
    temp = input()
    if temp=="1":
        ydir = -1
        xdir=0
    elif temp =='2':
        ydir = 1
        ydir=0
    if temp=="":
        xdir=0
        ydir=0
    temp=""
    

