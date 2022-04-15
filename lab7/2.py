import pygame
pygame.init()
screen = pygame.display.set_mode((1200,750))
q = pygame.image.load("qazaq.jpg")
screen.blit(q,(0,0))
pygame.display.update()
pygame.display.set_caption("QAZAQ FM")
i = pygame.image.load("qrep.jpg")
pygame.display.set_icon(i)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RSHIFT]:
        pygame.mixer.music.load("Sagyndym_seni.mp3")
        pygame.mixer.music.play()
    if keys[pygame.K_RIGHT]: 
        pygame.mixer.music.load("BarinenDeSenSulu.mp3")
        pygame.mixer.music.play()
    if keys[pygame.K_RALT]:   
        pygame.mixer.music.load("Bakyt_kushagynda.mp3")
        pygame.mixer.music.play()
    if keys[pygame.K_SPACE]:
        pygame.mixer.music.pause()
    if keys[pygame.K_LSHIFT]:
        pygame.mixer.music.unpause()
 
    pygame.display.flip()