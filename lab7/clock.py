import pygame
import datetime

pygame.init();
W, H = 700, 525

sc = pygame.display.set_mode((700, 525))

clock = pygame.time.Clock()

img = pygame.image.load('mainclock.png').convert_alpha()
lefthand = pygame.image.load('leftarm.png').convert_alpha()
righthand = pygame.image.load('rightarm.png').convert_alpha()



img = pygame.transform.scale(img, (img.get_width()//2, img.get_height()//2))
righthand = pygame.transform.scale(righthand, (righthand.get_width()//2, righthand.get_height()//2))
lefthand = pygame.transform.scale(lefthand, (lefthand.get_width()//2, lefthand.get_height()//2))


rh_rect = righthand.get_rect(center=(W//2, H//2))
lh_rect = lefthand.get_rect(center=(W//2,H//2))
rh_rect.center = lh_rect.center

sc.blit(img, (0, 0))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(); 
    
    time = datetime.datetime.now()    
    minuteTime = time.minute
    secondTime = time.second

    #minute
    angle1 = -minuteTime*6 - 54 #6 is degree
    leg1 = pygame.transform.rotate(righthand, angle1)
    rect1 = leg1.get_rect()
    rect1.center = rh_rect.center

    #second
    angle2 = -secondTime*6 #6 is degree
    leg2 = pygame.transform.rotate(lefthand, angle2)
    rect2 = leg2.get_rect()
    rect2.center = lh_rect.center

    #output
    sc.blit(img, (0, 0))
    sc.blit(leg1, rect1)
    sc.blit(leg2, rect2)
    

    pygame.display.flip()
    clock.tick(60)