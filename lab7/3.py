import pygame
pygame.init()
width = 640
height = 480
radius = 25
speed = 20
x = width/2
y = height/2
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Perfect Circle")
c = pygame.image.load("pcircle.jpg")
pygame.display.set_icon(c)
white = [255,255,255]
red = [255,0,0]
clock = pygame.time.Clock()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 640 - 2*radius : x += speed 
    if keys[pygame.K_LEFT] and x > 20 + radius: x -= speed
    if keys[pygame.K_UP] and y > 20 + radius:  y -= speed
    if keys[pygame.K_DOWN] and y < 480 - 2*radius: y += speed
    
    
    screen.fill(white)
    ball = pygame.draw.circle(screen,red,(x,y),radius)
    clock.tick(60)
    pygame.display.flip()